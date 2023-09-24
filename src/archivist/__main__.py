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

__main__.py

Typical usage example:
    
    python __main__.py
"""
import sys

from typing import Optional
from typing_extensions import Annotated
import argparse
import subprocess
from src.archivist import __app_name__, __version__, DEBUG
from src.archivist.crawler.crawler import Crawler

parser = argparse.ArgumentParser(prog='Archivist', description="Archivist is a tool for understanding codebases.")
parser.add_argument("--version", "-v", action="store_true",
                    help="Print the version number and exit.", default=False)
parser.add_argument("--update", "-u", action="store_true",
                    help="Update the Archivist tool to the latest version.", default=False)
parser.add_argument("--github_url", "-g", type=str,
                    help="The GitHub URL to download the code from.")
parser.add_argument("--output_path", "-o", type=str,
                    help="The path where the GitHub repo will be cloned.")
parser.add_argument("--branch", "-b", type=str,
                    help="Specify a particular branch to clone.")
parser.add_argument("--verbose", "-V", action="store_true",
                    help="Enable verbose output.", default=False)
parser.add_argument("--quiet", "-q", action="store_true",
                    help="Suppress all output except errors.", default=False)
parser.add_argument("--token", "-t", type=str,
                    help="Provide a GitHub authentication token.")
parser.add_argument("--config", "-c", type=str,
                    help="Path to a configuration file.")
parser.add_argument("--embeddings_path", "-e", type=str,
                    help="The output path for vector embeddings.")


class Config:
    """
    Config class for Archivist.
    """
    def __init__(self, github_url: Optional[str],
                 output_path: Optional[str], branch: Optional[str],
                 verbose: Optional[bool], quiet: Optional[bool],
                 token: Optional[str], config_file: Optional[str],
                 embeddings_path: Optional[str]):
        self.github_url = github_url
        self.output_path = output_path
        self.branch = branch
        self.verbose = verbose
        self.quiet = quiet
        self.token = token
        self.config_file = config_file
        self.embeddings_path = embeddings_path


def main() -> None:
    """
    Archivist is a tool for understanding codebases.

    Args:
        version: Print the version number and exit.
        github_url: The GitHub URL to download the code from.
        output_path: The path where the GitHub repo will be cloned.
        branch: Specify a particular branch to clone.
        verbose: Enable verbose output.
        quiet: Suppress all output except errors.
        token: Provide a GitHub authentication token.
        config: Path to a configuration file.
        update: Update the Archivist tool to the latest version.
        embeddings_path: The output path for vector embeddings.

    Returns:
        None
    """
    args = parser.parse_args()
    if args.version:
        print(f"{__app_name__} version {__version__}")
        sys.exit(0)

    if args.update:
        if DEBUG:
            print("DEBUG: Updating Archivist to the latest version.")
            subprocess.run(["pip", "install", "-e", "."])
            sys.exit(0)
        else:
            subprocess.run(["pip", "install", "--upgrade", "archivist"])
            print("Updated to the latest version.")
            sys.exit(0)

    config = Config(github_url=args.github_url, output_path=args.output_path, branch=args.branch,
                    verbose=args.verbose, quiet=args.quiet, token=args.token, config_file=args.config,
                    embeddings_path=args.embeddings_path)

    crawler = Crawler(config.github_url, config.output_path)
    crawler.execute()
