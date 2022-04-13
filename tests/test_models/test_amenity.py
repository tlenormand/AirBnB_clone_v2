#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ test class amenity """
    @classmethod
    def setUpClass(self):
        """le setup de test_Amenity"""
        # self._path_list.append("tests/test_city.py")
        self._path_list.append("models/amenity.py")

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
