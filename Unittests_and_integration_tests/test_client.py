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

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Test org'''
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))

    @patch.object(GithubOrgClient, 'org',
                  return_value={'repo_url': 'https://github.com/test/repo'})
    def test_public_repos_url(self, mock_org):
        '''Test public repo method'''
        client = GithubOrgClient('test')
        result = client._public_repos_url
        self.assertEqual(result, 'https://github.com/test/repo')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''Test Public Repos'''

        payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = payload
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          return_value='https://github.com/test/repos'
                          ) as mocked:
            client = GithubOrgClient('test')
            result = client.public_repos()
            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mocked.assert_called_once
            mock_get_json.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, repo, license_key, expected):
        '''Test has license'''
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


if __name__ == '__main__':
    unittest.main()
