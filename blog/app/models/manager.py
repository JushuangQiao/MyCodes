# coding=utf-8

import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from blog.app import login_manager
from datetime import datetime
from flask import current_app, url_for
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

    @staticmethod
    def get_profile_admin(user, param):
        param.email.data = user.email
        param.username.data = user.username
        param.role.data = user.role_id
        param.real_name.data = user.real_name
        param.location.data = user.location
        param.about_me.data = user.about_me
        return param

'''
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(followed=user)
            self.followed.append(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            self.followed.remove(f)

    def is_following(self, user):
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        return self.followers.filter_by(follower_id=user.id).first() is not None

    @property
    def followed_posts(self):
        return Post.query.join(Follow, Follow.followed_id == Post.author_id).filter(Follow.follower_id == self.id)

    @staticmethod
    def add_follow_self():
        for user in User.query.all():
            if not user.is_following(user):
                user.follow(user)
                db.session.add(user)
                db.session.commit()

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
    def add_post(body=None, author=None):
        try:
            post = Post(body=body, author_id=author.id)
            print post.body, post.author_id
            db.session.add(post)
            db.session.commit()
        except Exception, e:
            logging.error('class PostManager add_post failed:{0}'.format(e))

    @staticmethod
    def generate_fake(count=32):
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(body=forgery_py.lorem_ipsum.sentences(randint(1, 5)),
                     timestamp=forgery_py.date.date(True),
                     author_id=u)
            db.session.add(p)
            db.session.commit()
