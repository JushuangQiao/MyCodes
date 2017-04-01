# coding=utf-8

from flask import render_template, session, url_for, redirect, request, abort
from flask_login import login_required, current_user
# from setting import Config
from . import main
from .forms import ProfileForm, EditAdminForm, PostForm
from .. import db
from ..models.models import User, Role, Permission, Post
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination)


@main.route('/user/<username>', methods=['GET', 'POST'])
def user(username='World'):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('main/user.html', user=user, posts=posts, pagination=pagination)


@main.route('/user/<username>/details')
def user_detail(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/user_detail.html', user=user)


@main.route('/user/<username>/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.real_name = form.real_name.data
        current_user.age = form.age.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        # flash(u'您的资料已更改')
        print current_user.about_me
        return redirect(url_for('main.user_detail', username=current_user.username))
    form.real_name = current_user.real_name
    form.age = current_user.age
    form.location = current_user.location
    form.about_me = current_user.about_me
    return render_template('main/edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        # user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.real_name = form.real_name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        # flash('The profile has been updated.')
        return redirect(url_for('main.user', name=user.username))
    form.email.data = user.email
    form.username.data = user.username
    # form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.real_name.data = user.real_name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('main/edit_profile.html', form=form, user=user)
