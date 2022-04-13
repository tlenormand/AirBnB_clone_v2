#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from tests.test_requirements import TestRequirements
from console import HBNBCommand
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from unittest.mock import patch
from models import storage
import io
import unittest
from console import HBNBCommand
from io import StringIO
import console
import pycodestyle
import shutil
import os
import ast


class test_console(TestRequirements, unittest.TestCase):
    """ Class to test the console method """
    list_function = [
        "create",
        "show",
        "destroy",
        "all",
        "count",
        "update",
    ]
    list_class = [
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    ]

    @classmethod
    def setUpClass(self):
        """le setup de console"""
        # self._path_list.append("tests/test_city.py")
        self._path_list.append("console.py")

    def test_all_show_BaseModel(self):
        for key_class in self.list_class:
            for key in range(3):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(f"create {key_class}")
                existing_id = f.getvalue().replace("\n", "")
                dict_valid_test = [
                    f'show {key_class} "{existing_id}"',
                    f'show {key_class} "{existing_id}" etcetc',
                    f'show {key_class} {existing_id} etcetc',
                ]
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(dict_valid_test[key])
                output = f.getvalue()
                self.assertTrue(output)
                self.assertEqual(
                    f'{key_class}.{existing_id}',
                    f"{storage._FileStorage__objects[f'{key_class}.{existing_id}'].__class__.__name__}.{storage._FileStorage__objects[f'{key_class}.{existing_id}'].id}"
                )

    def test_prompt(self):
        """
        Test the prompt
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """
        Check the case of empty line
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_UnknowCommand(self):
        """
        Test an unknow command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("fdfdf")
            self.assertEqual("*** Unknown syntax: fdfdf", f.getvalue().strip())