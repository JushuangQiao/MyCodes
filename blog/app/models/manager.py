# coding=utf-8

import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from blog.app import login_manager
from datetime import datetime
from flask import current_app, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .models import User, Follow, Permission, Post
from . import db


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

    '''
    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def ping(self):
        last_seen = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('ascii')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

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
