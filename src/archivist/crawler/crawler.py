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

crawler.py
"""


class Crawler:
    """
    Crawler class responsible for cloning Git repositories.
    """

    def __init__(self, repo_url: str, output_path: str):
        """
        Initialize the Crawler object.

        Args:
            repo_url (str): The URL of the Git repository to clone.
            output_path (str): The directory where the repository will be cloned.

        Raises:
            ValueError: If `repo_url` is invalid.
        """
        pass

    def validate_repo_url(self) -> bool:
        """
        Validates the given Git repository URL.

        Returns:
            bool: True if the URL is valid, False otherwise.

        Raises:
            ConnectionError: If unable to connect to the repository.
        """
        pass

    def prepare_output_path(self) -> bool:
        """
        Prepares the output directory path. Creates it if it doesn't exist.

        Returns:
            bool: True if the path is valid or successfully created, False otherwise.

        Raises:
            PermissionError: If the program lacks write permission to create the directory.
        """
        pass

    def clone_repo(self) -> str:
        """
        Clones the Git repository to the specified output path.

        Returns:
            str: The path to the root of the cloned repository.

        Raises:
            GitCommandError: If the git clone operation fails.
        """
        pass

    def execute(self) -> str:
        """
        Orchestrates the whole cloning operation.

        Returns:
            str: The path to the root of the cloned repository.

        Raises:
            Exception: If any step in the operation fails.
        """
        pass
