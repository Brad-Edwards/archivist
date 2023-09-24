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
from unittest.mock import patch
from src.archivist.__main__ import main


class TestMain(unittest.TestCase):

    @patch('src.archivist.__main__.sys.exit')
    @patch('src.archivist.__main__.typer.echo')
    def test_version_option(self, mock_echo, mock_exit):
        main(version=True)
        mock_echo.assert_called_once_with("archivist version 0.0.1")
        mock_exit.assert_called_once_with(0)

    @patch('src.archivist.__main__.sys.exit')
    @patch('src.archivist.__main__.subprocess.run')
    @patch('src.archivist.__main__.typer.echo')
    def test_update_option(self, mock_echo, mock_run, mock_exit):
        mock_echo.reset_mock()
        main(update=True)
        mock_run.assert_called_once_with(["pip", "install", "--upgrade", "archivist"])
        mock_echo.assert_called_once_with("Updated to the latest version.")


if __name__ == '__main__':
    unittest.main()
