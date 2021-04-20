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
