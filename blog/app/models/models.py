# coding=utf-8

from datetime import datetime
from flask import current_app, url_for
from flask_login import UserMixin, AnonymousUserMixin
from ..exceptions import ValidationError
from . import *
from .. import login_manager


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    default = Column(Boolean, default=False, index=True)
    permissions = Column(Integer)
    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<role {0}>'.format(self.name)


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = Column(Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = Column(Integer, db.ForeignKey('users.id'), primary_key=True)
    timestamp = Column(DateTime(), default=datetime.utcnow)

    def __init__(self, *args):
        self.follower_id = args[0]
        self.followed_id = args[1]


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    password = Column(String(128))
    email = Column(String(64), unique=True, index=True)
    age = Column(Integer, nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    real_name = Column(String(64))
    location = Column(String(64))
    about_me = Column(Text())
    member_since = Column(DateTime(), default=datetime.utcnow)
    last_seen = Column(DateTime(), default=datetime.utcnow)
    posts = relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    followed = db.relationship('Follow', foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic', cascade='all, delete-orphan')
    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, username=None, password=None, email=None, age=None, role_id=None, real_name=None,
                 location=None, about_me=None, member_since=None, last_seen=None):
        self.username = username
        self.email = email
        self.age = age
        self.password = password
        self.role_id = Role.query.filter_by(default=True).first().id if role_id is None else int(role_id)
        self.real_name = real_name
        self.location = location
        self.about_me = about_me
        self.member_since = member_since
        self.last_seen = last_seen

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

    def __repr__(self):
        return '<user {0}>'.format(self.username)


class AnonymousUser(AnonymousUserMixin):
    pass

login_manager.anonymous_user = AnonymousUser


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    body = Column(Text)
    body_html = Column(Text)
    timestamp = Column(DateTime(), index=True, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship('Comment', backref='post', lazy='dynamic')

    def to_json(self):
        json_post = {
            'url': url_for('api.get_post', id=self.id, _external=True),
            'title': self.title,
            'body': self.body,
            'body_html': self.body_html,
            'timestamp': self.timestamp,
            'author': url_for('api.get_user', id=self.author_id,
                              _external=True),
            'comments': url_for('api.get_post_comments', id=self.id,
                                _external=True),
            'comment_count': self.comments.count()
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        return Post(body=body)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    body_html = Column(Text)
    timestamp = Column(DateTime(), index=True, default=datetime.utcnow)
    disabled = Column(Boolean)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
