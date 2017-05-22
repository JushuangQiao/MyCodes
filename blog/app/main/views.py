# coding=utf-8

import logging
from flask import render_template, session, url_for, redirect, request, abort
from flask import make_response, flash
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditAdminForm, PostForm, CommentForm
from .. import db
from ..models.models import User, Role, Permission, Post, Comment, AnonymousUser
from ..decorators import admin_required, permission_required
from blog.app.models.manager import UserManager, PostManager

logging.basicConfig(filename='running_error.log')


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    form = PostForm()
    if current_user.is_anonymous:
        return redirect(url_for('main.show_all'))
    try:
        if UserManager.can(current_user, Permission.WRITE_ARTICLES) and form.validate_on_submit():
            PostManager.add_post(body=form.body.data, author=current_user)
            return redirect(url_for('main.home'))
    except Exception, e:
        logging.error('func: home writing failed:{0}'.format(e))
        abort(500)
    try:
        page = request.args.get('page', 1, type=int)
        pagination = Post.query.filter_by(author_id=current_user.id).order_by(Post.timestamp.desc()).paginate(
            page, per_page=10, error_out=False)
        posts = pagination.items
        return render_template('main/home.html', form=form, posts=posts, pagination=pagination)
    except Exception, e:
        print e
        logging.error('func: home failed:{0}'.format(e))
        abort(500)


@main.route('/user/<username>', methods=['GET', 'POST'])
def user(username='World'):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    show_followed = False
    try:
        if current_user.is_authenticated:
            show_followed = bool(request.cookies.get('show_followed', ''))
        if show_followed:
            query = current_user.followed_posts
        else:
            query = Post.query
        pagination = query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)
        posts = pagination.items
        return render_template('main/user.html', posts=posts, user=user,
                               show_followed=show_followed, pagination=pagination)
    except Exception, e:
        logging.error('func:user error:{0}'.format(e))
        abort(500)


@main.route('/user/<username>/details')
@login_required
def user_detail(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/user_detail.html', user=user)


@main.route('/user/<username>/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = EditProfileForm()
    try:
        if form.validate_on_submit():
            UserManager.edit_profile(current_user, form)
            flash(u'您的资料已更改')
            return redirect(url_for('main.user_detail', username=username))
        return render_template('main/edit_profile.html', form=UserManager.get_profile(current_user, form))
    except Exception, e:
        logging.error('func:edit_profile error:{0}'.format(e))
        return render_template('main/edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditAdminForm(user=user)
    try:
        if form.validate_on_submit():
            UserManager.edit_profile_admin(user, form)
            flash(u'资料已更改')
            return redirect(url_for('main.user_detail', username=user.username))
        form = UserManager.get_profile_admin(current_user, form)
        return render_template('main/edit_profile.html', form=form, user=user)
    except Exception, e:
        logging.error('func: edit_profile_admin error:{0}'.format(e))
        return render_template('main/edit_profile.html', form=form, user=user)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    posts = Post.query.get_or_404(id)
    form = CommentForm()
    try:
        if form.validate_on_submit():
            comment = Comment(body=form.body.data, post=posts, author=current_user._get_current_object())
            db.session.add(comment)
            return redirect(url_for('main.post', id=posts.id, page=-1))
        page = request.args.get('page', 1, type=int)
        if page == -1:
            page = (posts.comments.count() - 1) / 10 + 1
        pagination = posts.comments.order_by(Comment.timestamp.asc()).paginate(
            page, per_page=10, error_out=False)
        comments = pagination.items
        return render_template('main/post.html', posts=[posts], form=form, pagination=pagination, comments=comments)
    except Exception, e:
        logging.error('func: post error:{0}'.format(e))
        abort(500)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and not UserManager.can(current_user, Permission.ADMINISTER):
        abort(403)
    form = PostForm()
    try:
        if form.validate_on_submit():
            post.body = form.body.data
            db.session.add(post)
            return redirect(url_for('main.post', id=post.id))
        form.body.data = post.body
        return render_template('main/edit_post.html', form=form)
    except Exception, e:
        logging.error('func: edit_post error:{0}'.format(e))


@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('main.user_detail', username=username))
    if current_user.is_following(user):
        return redirect(url_for('main.user_detail', username=username))
    current_user.follow(user)
    return redirect(url_for('main.user_detail', username=username))


@main.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('main.user_detail', username=username))
    if not current_user.is_following(user):
        return redirect(url_for('main.user_detail', username=username))
    current_user.unfollow(user)
    return redirect(url_for('main.user_detail', username=username))


@main.route('/followers/<username>')
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followers.paginate(page, per_page=10, error_out=False)
    follows = [{'user': item.follower, 'timestamp': item.timestamp}
               for item in pagination.items]
    return render_template('main/followers.html', user=user, title=u"关注",
                           endpoint='.followers', pagination=pagination,
                           follows=follows)


@main.route('/followed-by/<username>')
def followed_by(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followed.paginate(
        page, per_page=10, error_out=False)
    follows = [{'user': item.followed, 'timestamp': item.timestamp}
               for item in pagination.items]
    return render_template('main/followers.html', user=user, title=u"粉丝",
                           endpoint='.followed_by', pagination=pagination,
                           follows=follows)


@main.route('/all')
# @login_required
def show_all():
    if current_user.is_anonymous:
        page = request.args.get('page', 1, type=int)
        query = Post.query
        pagination = query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)
        posts = pagination.items
        return render_template('main/all_posts.html', posts=posts, pagination=pagination)
    else:
        resp = make_response(redirect(url_for('main.user', username=current_user.username)))
        resp.set_cookie('show_followed', '', max_age=30*24*60*60)
        return resp


@main.route('/followed')
@login_required
def show_followed():
    resp = make_response(redirect(url_for('main.user', username=current_user.username)))
    resp.set_cookie('show_followed', '1', max_age=30*24*60*60)
    return resp


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate():
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    comments = pagination.items
    return render_template('main/moderate.html', comments=comments, pagination=pagination, page=page)


@main.route('/moderate/enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_enable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)
    return redirect(url_for('main.moderate', page=request.args.get('page', 1, type=int)))


@main.route('/moderate/disable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_disable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = True
    db.session.add(comment)
    return redirect(url_for('main.moderate', page=request.args.get('page', 1, type=int)))
