#!/usr/bin/env python3
"""TestAccessNestedMap Module
"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """ TestAccessNestedMap Class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nest, path, result):
        """test_access_nested_map method
        """
        self.assertEqual(access_nested_map(nest, path), result)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nest, path):
        """test_access_nested_map_exception method
        """
        with self.assertRaises(KeyError) as keyerror:
            access_nested_map(nest, path)
        self.assertEqual(keyerror.exception.args[0], path[-1])
