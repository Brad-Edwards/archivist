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
from src.archivist.__main__ import main, Config

class TestArchivist(unittest.TestCase):

    @patch('src.archivist.__main__.ArgumentParser.parse_args')  # Mocking argparse's parse_args method
    @patch('src.archivist.__main__.subprocess.run')  # Mocking subprocess.run method
    @patch('src.archivist.__main__.sys.exit')  # Mocking sys.exit
    def test_version_flag(self, mock_exit, mock_run, mock_parse_args):
        mock_args = Mock()
        mock_args.version = True
        mock_parse_args.return_value = mock_args

        main()

        mock_exit.assert_called_once_with(0)

    @patch('src.archivist.__main__.DEBUG', new_callable=Mock)
    @patch('src.archivist.__main__.argparse.ArgumentParser.parse_args')
    @patch('src.archivist.__main__.subprocess.run')
    @patch('src.archivist.__main__.sys.exit')
    def test_update_flag(self, mock_exit, mock_run, mock_parse_args, mock_debug):
        mock_debug.return_value = False
        mock_args = Mock()
        mock_args.update = True
        mock_args.version = False
        mock_parse_args.return_value = mock_args

        main()

        mock_run.assert_called_once()
        mock_exit.assert_called_once_with(0)

    @patch('src.archivist.__main__.DEBUG', new_callable=Mock)
    @patch('argparse.ArgumentParser.parse_args')
    @patch('subprocess.run')
    @patch('sys.exit')
    def test_version_flag(self, mock_exit, mock_run, mock_parse_args, mock_debug):
        mock_debug.return_value = False
        mock_args = Mock()
        mock_args.github_url = "some_url"
        mock_args.output_path = "some_path"
        mock_args.version = False
        mock_args.update = False
        mock_parse_args.return_value = mock_args

        main()

        config = Config(github_url=mock_args.github_url, output_path=mock_args.output_path,
                        branch=mock_args.branch, verbose=mock_args.verbose, quiet=mock_args.quiet,
                        token=mock_args.token, config_file=mock_args.config,
                        embeddings_path=mock_args.embeddings_path)
        self.assertEqual(config.github_url, "some_url")
        self.assertEqual(config.output_path, "some_path")


if __name__ == '__main__':
    unittest.main()
