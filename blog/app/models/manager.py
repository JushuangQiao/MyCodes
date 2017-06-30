# coding=utf-8

import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
import bleach
from markdown import markdown
from .. import login_manager
from datetime import datetime
from .models import User, Follow, Permission, Post, Role
from . import db


class RoleManager(object):

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT | Permission.FOLLOW | Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.COMMENT | Permission.FOLLOW | Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for role in roles:
            r = Role.query.filter_by(name=role).first()
            if r is None:
                r = Role(name=role)
            r.permissions = roles[role][0]
            r.default = roles[role][1]
            db.session.add(r)
        db.session.commit()


class UserManager(object):

    @staticmethod
    def add_user(param):
        user = User()
        try:
            user.username = param.username.data
            user.password = generate_password_hash(str(param.password.data))
            user.email = param.email.data
            db.session.add(user)
            UserManager.follow(user, user)
            db.session.add(user)
        except Exception, e:
            logging.error('class: UserManager failed {0}'.format(e))

    @staticmethod
    def verify_password(param):
        try:
            user = User.query.filter_by(email=param.email.data).first()
            if user is not None and check_password_hash(user.password, str(param.password.data)):
                login_user(user, param.remember_me.data)
                return user
            return False
        except Exception, e:
            logging.error('class: UserManager failed {0}'.format(e))

    @staticmethod
    def change_password(user, param):
        try:
            user.password = generate_password_hash(str(param.password.data))
            db.session.add(user)
        except Exception, e:
            logging.error('class: UserManager failed {0}'.format(e))

    @staticmethod
    def generate_fake(count=32):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = User(email=forgery_py.internet.email_address(),
                     username=forgery_py.internet.user_name(True),
                     password=forgery_py.lorem_ipsum.word(),
                     real_name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    @staticmethod
    def can(user, permissions):
        if user.is_anonymous:
            return False
        return user.role is not None and (user.role.permissions & permissions) == permissions

    @staticmethod
    def is_administrator(user):
        return UserManager.can(user, Permission.ADMINISTER)

    @staticmethod
    def ping(user):
        user.last_seen = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def edit_profile(user, param):
        user.real_name = param.real_name.data
        user.age = param.age.data
        user.location = param.location.data
        user.about_me = param.about_me.data
        db.session.add(user)

    @staticmethod
    def get_profile(user, param):
        param.real_name.data = user.real_name
        param.age.data = user.age
        param.location.data = user.location
        param.about_me.data = user.about_me
        return param

    @staticmethod
    def edit_profile_admin(user, param):
        user.email = param.email.data
        user.username = param.username.data
        user.role_id = Role.query.get(param.role.data).id
        user.real_name = param.real_name.data
        user.location = param.location.data
        user.about_me = param.about_me.data
        db.session.add(user)

    @staticmethod
    def get_profile_admin(user, param):
        param.email.data = user.email
        param.username.data = user.username
        param.role.data = user.role_id
        param.real_name.data = user.real_name
        param.location.data = user.location
        param.about_me.data = user.about_me
        return param

    @staticmethod
    def get_user_by_name(username):
        user = User.query.filter_by(username=username).first()
        return user if user else False

    @staticmethod
    def get_user_by_email(email):
        user = User.query.filter_by(email=email).first()
        return user if user else False

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(str(user_id)))

    @staticmethod
    def follow(user, followed):
        if not UserManager.is_following(user, followed):
            f = Follow(user.id, followed.id)
            user.followed.append(f)

    @staticmethod
    def unfollow(user, followed):
        f = user.followed.filter_by(followed_id=followed.id).first()
        if f:
            user.followed.remove(f)

    @staticmethod
    def is_following(user, followed):
        return user.followed.filter_by(followed_id=followed.id).first() is not None

    @staticmethod
    def is_followed_by(user, followed):
        return user.followers.filter_by(follower_id=followed.id).first() is not None

    @staticmethod
    def followed_posts(user):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id).filter(Follow.follower_id == user.id)
'''
    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id, _external=True),
            'username': self.username,
            'member_since': self.member_since,
            'last_seen': self.last_seen,
            'posts': url_for('api.get_user_posts', id=self.id, _external=True),
            'followed_posts': url_for('api.get_user_followed_posts',
                                      id=self.id, _external=True),
            'post_count': self.posts.count()
        }
        return json_user
    '''


class PostManager(object):

    @staticmethod
    def add_post(title=None, body=None, author=None):
        try:
            post = Post(title=title, body=body, author_id=author.id)
            db.session.add(post)
            db.session.commit()
        except Exception, e:
            logging.error('class PostManager add_post failed:{0}'.format(e))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags,
                                                       strip=True))

    @staticmethod
    def generate_fake(count=32):
        from sqlalchemy.exc import IntegrityError
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(title=forgery_py.name.title(), body=forgery_py.lorem_ipsum.sentences(randint(1, 5)),
                     timestamp=forgery_py.date.date(True),
                     author_id=u)
            db.session.add(p)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

db.event.listen(Post.body, 'set', PostManager.on_changed_body)
