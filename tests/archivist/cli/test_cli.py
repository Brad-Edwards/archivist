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
from src.archivist.cli.cli import handle_config, handle_github_url, handle_output_path, \
    handle_branch, handle_verbose, handle_quiet, handle_token, handle_config_file, handle_update, \
    handle_embeddings_path
from src.archivist.__main__ import Config
from src.archivist.errors.errors import UNSUPPORTED_CONFIG, NO_CONFIG, UNSUPPORTED_URL, NO_EMPTY_PATH, \
    UNSUPPORTED_PATH, UNSUPPORTED_CONFIG_PATH


class TestHandleConfig(unittest.TestCase):

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
                                                    mock_handle_output_path, mock_handle_github_url):
        initial_config = Config(version=True, github_url="https://github.com/test", output_path="test",
                                branch="master", verbose=True, quiet=True, token="test", config_file="test",
                                update=False, embeddings_path="test")
        final_config = handle_config(initial_config)
        self.assertIsInstance(final_config, Config)
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
        with self.assertRaisesRegex(ValueError, NO_CONFIG):
            handle_config(None)

    def test_handle_config_with_invalid_config_object(self):
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_CONFIG):
            handle_config("test")

    def test_handle_config_with_empty_config_object(self):
        initial_config = Config(version=None, github_url=None, output_path=None, branch=None, verbose=None,
                                quiet=None, token=None, config_file=None, update=None, embeddings_path=None)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_CONFIG):
            handle_config(initial_config)


class TestHandleGithubUrl(unittest.TestCase):

    def test_valid_github_url(self):
        config = Config(github_url="https://github.com/username/repo.git",
                        output_path="test", branch="master", verbose=True, quiet=True, token="test",
                        config_file="test", update=False, embeddings_path="test", version=False)
        try:
            handle_github_url(config)
        except ValueError:
            self.fail("handle_github_url() raised ValueError unexpectedly!")

    def test_invalid_github_url(self):
        config = Config(github_url="https://gitlab.com/username/repo.git",
                        output_path="test", branch="master", verbose=True, quiet=True, token="test",
                        config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_URL):
            handle_github_url(config)

    def test_empty_url(self):
        config = Config(github_url="",
                        output_path="test", branch="master", verbose=True, quiet=True, token="test",
                        config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_URL):
            handle_github_url(config)

    def test_malformed_url(self):
        config = Config(github_url="malformed_url",
                        output_path="test", branch="master", verbose=True, quiet=True, token="test",
                        config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_URL):
            handle_github_url(config)

    def test_none_url(self):
        config = Config(github_url=None,
                        output_path="test", branch="master", verbose=True, quiet=True, token="test",
                        config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_URL):
            handle_github_url(config)


class TestHandleOutputPath(unittest.TestCase):

    def test_valid_output_path(self):
        config = Config(output_path="./output", github_url="test", branch="master", verbose=True, quiet=True,
                        token="test", config_file="test", update=False, embeddings_path="test", version=False)
        try:
            handle_output_path(config)
        except ValueError:
            self.fail("handle_output_path() raised ValueError unexpectedly!")

    def test_none_output_path(self):
        config = Config(output_path=None, github_url="test", branch="master", verbose=True, quiet=True,
                        token="test", config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, NO_EMPTY_PATH):
            handle_output_path(config)

    def test_empty_output_path(self):
        config = Config(output_path="", github_url="test", branch="master", verbose=True, quiet=True,
                        token="test", config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, NO_EMPTY_PATH):
            handle_output_path(config)

    def test_invalid_characters_in_output_path(self):
        config = Config(output_path="output<>|:", github_url="test", branch="master", verbose=True, quiet=True,
                        token="test", config_file="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_PATH):
            handle_output_path(config)


class TestHandleBranch(unittest.TestCase):

    def test_handle_branch(self):
        pass


class TestHandleVerbose(unittest.TestCase):

    def test_handle_verbose(self):
        pass


class TestHandleQuiet(unittest.TestCase):

        def test_handle_quiet(self):
            pass


class TestHandleToken(unittest.TestCase):

    def test_handle_token(self):
        pass


class TestHandleConfigFile(unittest.TestCase):

    def test_valid_config_file(self):
        with mock.patch('os.path.exists', return_value=True):
            config = Config(config_file="./config.yaml", github_url="test", output_path="test", branch="master",
                            verbose=True, quiet=True, token="test", update=False, embeddings_path="test", version=False)
            try:
                handle_config_file(config)
            except ValueError:
                self.fail("handle_config_file() raised ValueError unexpectedly!")

    def test_none_config_file(self):
        config = Config(config_file=None, github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", update=False, embeddings_path="test", version=False)
        self.assertIsNone(handle_config_file(config))

    @mock.patch("src.archivist.cli.cli.os.path.exists")
    def test_empty_config_file(self, mock_path_exists):
        config = Config(config_file="", github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", update=False, embeddings_path="test", version=False)
        self.assertIsNone(handle_config_file(config))

    def test_invalid_characters_in_config_file(self):
        config = Config(config_file="config<>|:", github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", update=False, embeddings_path="test", version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_CONFIG_PATH):
            handle_config_file(config)


class TestHandleUpdate(unittest.TestCase):

    def test_update_is_true(self):
        config = Config(update=True, github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", embeddings_path="test",
                        version=False)
        try:
            handle_update(config)
        except ValueError:
            self.fail("handle_update() raised ValueError unexpectedly when update is True!")

    def test_update_is_false(self):
        config = Config(update=False, github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", embeddings_path="test",
                        version=False)
        try:
            handle_update(config)
        except ValueError:
            self.fail("handle_update() raised ValueError unexpectedly when update is False!")

    def test_update_is_none(self):
        config = Config(update=None, github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", embeddings_path="test",
                        version=False)
        try:
            handle_update(config)
        except ValueError:
            self.fail("handle_update() raised ValueError unexpectedly when update is None!")

    def test_update_is_unsupported_value(self):
        config = Config(update="unsupported", github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", embeddings_path="test",
                        version=False)
        with self.assertRaisesRegex(ValueError, UNSUPPORTED_CONFIG):
            handle_update(config)


class TestHandleEmbeddingsPath(unittest.TestCase):

    def test_valid_embeddings_path_exists(self):
        with mock.patch('os.path.exists', return_value=True):
            config = Config(embeddings_path="./embeddings", github_url="test", output_path="test", branch="master",
                            verbose=True, quiet=True, token="test", config_file="test", update=False, version=False)
            try:
                handle_embeddings_path(config)
            except ValueError:
                self.fail("handle_embeddings_path() raised ValueError unexpectedly!")

    def test_valid_embeddings_path_not_exists(self):
        with mock.patch('os.path.exists', return_value=False):
            config = Config(embeddings_path="./embeddings", github_url="test", output_path="test", branch="master",
                            verbose=True, quiet=True, token="test", config_file="test", update=False, version=False)
            try:
                handle_embeddings_path(config)
            except ValueError:
                self.fail("handle_embeddings_path() raised ValueError unexpectedly!")

    def test_no_embeddings_path(self):
        config = Config(embeddings_path=None, github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", update=False, version=False)
        with self.assertRaises(ValueError):
            handle_embeddings_path(config)

    def test_invalid_embeddings_path(self):
        config = Config(embeddings_path="::invalid::", github_url="test", output_path="test", branch="master",
                        verbose=True, quiet=True, token="test", config_file="test", update=False, version=False)
        with self.assertRaises(ValueError):
            handle_embeddings_path(config)


if __name__ == "__main__":
    unittest.main()

