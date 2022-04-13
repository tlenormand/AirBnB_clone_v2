#!/usr/bin/python3
"""
module that contain the superclass TestRequirements

Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_requirements.py
"""

import pycodestyle
import inspect
from importlib.machinery import SourceFileLoader
import re


class TestRequirements(object):
    """
    class that test for requirements

    Functions:
        test_conformance: test conformance to PEP-8
        test_documentation: test all documentation in file

    Attributes:
        _path_list (list): contain [<path>] to test
    """
    _path_list = []

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        self._path_list.clear()
        pass

    def test_conformance(self):
        """test conformance to PEP-8"""
        for _path in self._path_list:
            style = pycodestyle.StyleGuide(quiet=True)
            result = style.check_files([_path])
            self.assertEqual(
                result.total_errors,
                0,
                f"Found code style errors (pycodestyle) in file \"{_path}\""
            )

    def test_documentation(self):
        """test all documentation in file"""
        # read file in _path
        for _path in self._path_list:
            textfile = open(_path, 'r')
            filetext = textfile.read()
            textfile.close()

            # find classes in the file
            matches = re.findall("class .+\(.+\):", filetext)
            if matches:

                # browse each matches classes
                for matche in matches:
                    class_name = re.search("class (.+)\(.+\):", str(matche))
                    if class_name:
                        _class = class_name.group(1)

                        # imports modules of the class
                        module = SourceFileLoader(_class, _path).load_module()

                        # check for module documentation
                        self.assertIsNotNone(
                            module.__doc__,
                            f"Missing: documentation of module \"{_path}\""
                        )

                        # check for class documentation
                        for key, value in module.__dict__.items():
                            if inspect.isclass(value):
                                self.assertIsNotNone(
                                    value.__doc__,
                                    f"Missing: documentation of class \"{value.__name__}\" in \"{_path}\""
                                )
                                # check for function documentation
                                for key, value in getattr(module, _class).__dict__.items():
                                    if inspect.isfunction(value):
                                        self.assertIsNotNone(
                                            value.__doc__,
                                            f"Missing: documentation of function \"{value.__name__}\" in \"{_path}\""
                                        )
                    else:
                        print(f"class has an unvalid name: {matche} in {_path}")
            # else:
            #     print(f"no class found in {matches} in {_path}")
