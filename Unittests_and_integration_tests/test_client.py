#!/usr/bin/env python3
'''Test client Doc'''
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import (
    get_json,
    access_nested_map,
    memoize,
)



class TestGithubOrgClient(unittest.TestCase):
    '''Test GitHub Org Client'''

    @patch('client.get_json')
    @parameterized.expand([
        ("google", {"repos_url": "https://github.com/google/repositories"}),
        ("abc", {"repos_url": "https://github.com/abc/repositories"})
    ])
    def test_org(self, org_name, mock_get_json_result):
        '''Test org'''
        mock_get_json_result.return_value = mock_get_json_result
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json_result.assert_called_once(GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, mock_get_json_result.return_value)

