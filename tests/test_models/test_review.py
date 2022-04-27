#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from os import getenv

storageType = getenv("HBNB_TYPE_STORAGE")


class test_review(test_basemodel):
    """ """
    @classmethod
    def setUpClass(self):
        """le setup de test_review"""
        self._path_list.append("tests/test_models/test_review.py")
        self._path_list.append("models/review.py")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.place_id, None)
        else:
            self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        if storageType == "db":
            self.assertEqual(new.text, None)
        else:
            self.assertEqual(type(new.text), str)
