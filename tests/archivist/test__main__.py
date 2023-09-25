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

test__main__.py
"""
import unittest
from unittest.mock import patch, Mock
from src.archivist.__main__ import main


class TestArchivist(unittest.TestCase):

    @patch('src.archivist.__main__.Crawler')
    @patch('src.archivist.__main__.DEBUG', new_callable=Mock)
    @patch('src.archivist.__main__.argparse.ArgumentParser.parse_args')
    @patch('src.archivist.__main__.subprocess.run')
    @patch('src.archivist.__main__.sys.exit')
    def test_update_flag(self, mock_exit, mock_run, mock_parse_args, mock_debug, mocked_crawler):
        mock_debug.return_value = False
        mock_args = Mock()
        mock_args.update = True
        mock_args.version = False
        mock_parse_args.return_value = mock_args

        # Setup the mock Crawler instance
        mock_crawler_instance = Mock()
        mock_crawler_instance.repo_url = 'https://mocked.repo.url'
        mocked_crawler.return_value = mock_crawler_instance

        main()

        mock_run.assert_called_once()
        mock_exit.assert_called_once_with(0)

    @patch('src.archivist.__main__.Crawler')
    @patch('src.archivist.__main__.DEBUG', new_callable=Mock)
    @patch('argparse.ArgumentParser.parse_args')
    @patch('subprocess.run')
    @patch('sys.exit')
    def test_version_flag(self, mock_exit, mock_run, mock_parse_args, mock_debug, mocked_crawler):
        mock_debug.return_value = False
        mock_args = Mock()
        mock_args.github_url = "some_url"
        mock_args.output_path = "some_path"
        mock_args.version = False
        mock_args.update = False
        mock_parse_args.return_value = mock_args

        # Setup the mock Crawler instance
        mock_crawler_instance = Mock()
        mocked_crawler.return_value = mock_crawler_instance

        # Optionally, set return values or side effects for methods in mock_crawler_instance
        # For example, mock_crawler_instance.execute.return_value = "some_value"

        main()
        self.assertEqual(mock_args.github_url, "some_url")
        self.assertEqual(mock_args.output_path, "some_path")


if __name__ == '__main__':
    unittest.main()
