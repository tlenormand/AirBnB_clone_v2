#!/usr/bin/python3
""" """
from os import getenv
from tests.test_models.test_base_model import test_basemodel
from models.user import User

storageType = getenv("HBNB_TYPE_STORAGE")


class test_User(test_basemodel):
    """ """
    @classmethod
    def setUpClass(self):
        """le setup de test_User"""
        self._path_list.append("tests/test_models/test_user.py")
        self._path_list.append("models/user.py")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.first_name, None)
        else:
            self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.last_name, None)
        else:
            self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.email, None)
        else:
            self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.password, None)
        else:
            self.assertEqual(type(new.password), str)
