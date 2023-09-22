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

test_cli.py
"""
import unittest
from unittest import mock
from src.archivist.cli.cli import handle_config, handle_version, handle_github_url, handle_output_path, \
    handle_branch, handle_verbose, handle_quiet, handle_token, handle_config_file, handle_update, \
    handle_embeddings_path
from src.archivist.__main__ import Config
from src.archivist.errors.errors import ERRORS, INVALID_CONFIG, NO_CONFIG


class TestHandleConfig(unittest.TestCase):

    @mock.patch("src.archivist.cli.cli.handle_version")
    @mock.patch("src.archivist.cli.cli.handle_github_url")
    @mock.patch("src.archivist.cli.cli.handle_output_path")
    @mock.patch("src.archivist.cli.cli.handle_branch")
    @mock.patch("src.archivist.cli.cli.handle_verbose")
    @mock.patch("src.archivist.cli.cli.handle_quiet")
    @mock.patch("src.archivist.cli.cli.handle_token")
    @mock.patch("src.archivist.cli.cli.handle_config_file")
    @mock.patch("src.archivist.cli.cli.handle_update")
    @mock.patch("src.archivist.cli.cli.handle_embeddings_path")
    def test_handle_config_with_valid_config_object(self, mock_handle_embeddings_path, mock_handle_update,
                                                    mock_handle_config_file, mock_handle_token, mock_handle_quiet,
                                                    mock_handle_verbose, mock_handle_branch,
                                                    mock_handle_output_path, mock_handle_github_url,
                                                    mock_handle_version):
        initial_config = Config(version=True, github_url="https://github.com/test", output_path="test",
                                branch="master", verbose=True, quiet=True, token="test", config_file="test",
                                update=False, embeddings_path="test")
        final_config = handle_config(initial_config)
        self.assertIsInstance(final_config, Config)
        mock_handle_version.assert_called_once()
        mock_handle_github_url.assert_called_once()
        mock_handle_output_path.assert_called_once()
        mock_handle_branch.assert_called_once()
        mock_handle_verbose.assert_called_once()
        mock_handle_quiet.assert_called_once()
        mock_handle_token.assert_called_once()
        mock_handle_config_file.assert_called_once()
        mock_handle_update.assert_called_once()
        mock_handle_embeddings_path.assert_called_once()

    def test_handle_config_with_no_config_object(self):
        with self.assertRaisesRegex(ValueError, ERRORS[NO_CONFIG]):
            handle_config(None)

    def test_handle_config_with_invalid_config_object(self):
        with self.assertRaisesRegex(ValueError, ERRORS[INVALID_CONFIG]):
            handle_config("test")

    def test_handle_config_with_empty_config_object(self):
        initial_config = Config(version=None, github_url=None, output_path=None, branch=None, verbose=None,
                                quiet=None, token=None, config_file=None, update=None, embeddings_path=None)
        with self.assertRaisesRegex(ValueError, ERRORS[INVALID_CONFIG]):
            handle_config(initial_config)


if __name__ == "__main__":
    unittest.main()

