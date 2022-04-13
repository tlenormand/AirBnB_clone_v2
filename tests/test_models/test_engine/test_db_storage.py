#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from tests.test_requirements import TestRequirements


class test_dbstorage(TestRequirements, unittest.TestCase):
    """ Class to test the db_storage method """
    @classmethod
    def setUpClass(self):
        """le setup de db_storage"""
        # self._path_list.append("tests/test_city.py")
        self._path_list.append("models/engine/db_storage.py")
