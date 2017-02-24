# coding=utf-8

import unittest
from app.models.models import User


class TestUserModel(unittest.TestCase):

    def test_password_setter(self):
        u = User('test')
        self.assertTrue(u.password_hash is not None)

    def test_no_paaword_getter(self):
        u = User('test')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User('test')
        self.assertTrue(u.verify_password('123456'))
        self.assertFalse(u.verify_password('test'))

    def test_password_salts_are_random(self):
        self.assertFalse(User('a').password_hash == User('b').password_hash)
