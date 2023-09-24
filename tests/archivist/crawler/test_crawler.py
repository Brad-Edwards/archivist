"""
Copyright © 2023 Brad Edwards

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

test_crawler.py
"""
import unittest
from unittest.mock import patch, Mock
from src.archivist.crawler.crawler import Crawler


class TestValidateRepoUrl(unittest.TestCase):

    @patch('src.archivist.crawler.validators.url')
    def test_valid_repo_url(self, mock_check_url):
        mock_check_url.return_value = True
        crawler = Crawler("https://github.com/sample/repo.git", "/output/path")
        self.assertTrue(crawler.validate_repo_url())

    @patch('src.archivist.crawler.crawler.some_external_dependency_to_check_url')
    def test_invalid_repo_url(self, mock_check_url):
        mock_check_url.return_value = False
        crawler = Crawler("invalid_url", "/output/path")
        self.assertFalse(crawler.validate_repo_url())

    def test_empty_repo_url(self):
        with self.assertRaises(ValueError):
            Crawler("", "/output/path")


class TestPrepareOutputPath(unittest.TestCase):

    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_existing_output_path(self, mock_makedirs, mock_exists):
        mock_exists.return_value = True
        crawler = Crawler("https://github.com/sample/repo.git", "/existing/path")
        self.assertTrue(crawler.prepare_output_path())
        mock_makedirs.assert_not_called()

    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_create_new_output_path(self, mock_makedirs, mock_exists):
        mock_exists.return_value = False
        crawler = Crawler("https://github.com/sample/repo.git", "/new/path")
        self.assertTrue(crawler.prepare_output_path())
        mock_makedirs.assert_called_once_with("/new/path")

    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_create_new_output_path_fails(self, mock_makedirs, mock_exists):
        mock_exists.return_value = False
        mock_makedirs.side_effect = PermissionError("Permission denied")
        crawler = Crawler("https://github.com/sample/repo.git", "/new/path")
        with self.assertRaises(PermissionError):
            crawler.prepare_output_path()


class TestCloneRepo(unittest.TestCase):

    @patch('subprocess.run')
    def test_clone_repo_success(self, mock_run):
        mock_run.return_value = Mock(returncode=0)
        crawler = Crawler("https://github.com/sample/repo.git", "/output/path")
        self.assertEqual(crawler.clone_repo(), "/output/path")

    @patch('subprocess.run')
    def test_clone_repo_failure(self, mock_run):
        mock_run.return_value = Mock(returncode=1)
        crawler = Crawler("https://github.com/sample/repo.git", "/output/path")
        with self.assertRaises(Exception):
            crawler.clone_repo()


class TestExecute(unittest.TestCase):

    @patch.object(Crawler, 'validate_repo_url')
    @patch.object(Crawler, 'prepare_output_path')
    @patch.object(Crawler, 'clone_repo')
    def test_execute_success(self, mock_clone, mock_prepare, mock_validate):
        mock_validate.return_value = True
        mock_prepare.return_value = True
        mock_clone.return_value = "/output/path"
        crawler = Crawler("https://github.com/sample/repo.git", "/output/path")
        self.assertEqual(crawler.execute(), "/output/path")

    @patch.object(Crawler, 'validate_repo_url')
    def test_execute_invalid_url(self, mock_validate):
        mock_validate.return_value = False
        crawler = Crawler("invalid_url", "/output/path")
        with self.assertRaises(Exception):
            crawler.execute()


if __name__ == '__main__':
    unittest.main()
