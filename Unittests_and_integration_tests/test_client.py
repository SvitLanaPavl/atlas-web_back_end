#!/usr/bin/env python3
'''Test client Doc'''
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from utils import (
    get_json,
    access_nested_map,
    memoize,
)
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''Test has license'''
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test'''
    @parameterized_class(
        {'org_payload': org_payload, 'repos_payload': repos_payload, 'expected_repos': expected_repos, 'apache2_repos': apache2_repos}
    )

    @classmethod
    def setUpClass(cls):
        '''Setup method'''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start() 

    @classmethod
    def tearDownClass(self):
        '''TearDown'''
    cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
