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
import typer
import subprocess
from src.archivist import __app_name__, __version__, DEBUG

app = typer.Typer()


class Config:
    def __init__(self, version: Optional[bool], github_url: Optional[str],
                 output_path: Optional[str], branch: Optional[str],
                 verbose: Optional[bool], quiet: Optional[bool],
                 token: Optional[str], config_file: Optional[str],
                 update: Optional[bool], embeddings_path: Optional[str]):
        self.version = version
        self.github_url = github_url
        self.output_path = output_path
        self.branch = branch
        self.verbose = verbose
        self.quiet = quiet
        self.token = token
        self.config_file = config_file
        self.update = update
        self.embeddings_path = embeddings_path


@app.command()
def main(
        version: Annotated[Optional[bool], typer.Option(
            False,
            "--version",
            "-v",
            help="Print the version number and exit.",
        )] = None,
        github_url: Annotated[Optional[str], typer.Option(
            None,
            "--github-url",
            "-g",
            help="The GitHub URL to download the code from."
        )] = None,
        output_path: Annotated[Optional[str], typer.Option(
            None,
            "--output-path",
            "-o",
            help="The path where the GitHub repo will be cloned."
        )] = None,
        branch: Annotated[Optional[str], typer.Option(
            None,
            "--branch",
            "-b",
            help="Specify a particular branch to clone."
        )] = None,
        verbose: Annotated[Optional[bool], typer.Option(
            False,
            "--verbose",
            "-V",
            help="Enable verbose output."
        )] = None,
        quiet: Annotated[Optional[bool], typer.Option(
            False,
            "--quiet",
            "-q",
            help="Suppress all output except errors."
        )] = None,
        token: Annotated[Optional[str], typer.Option(
            None,
            "--token",
            "-k",
            help="Provide a GitHub authentication token."
        )] = None,
        config: Annotated[Optional[str], typer.Option(
            "config.yaml",
            "--config",
            "-c",
            help="Path to a configuration file."
        )] = None,
        update: Annotated[Optional[bool], typer.Option(
            None,
            "--update",
            "-u",
            help="Update the Archivist tool to the latest version."
        )] = None,
        embeddings_path: Annotated[Optional[str], typer.Option(
            None,
            "--embeddings-path",
            "-e",
            help="The output path for vector embeddings."
        )] = None,
) -> None:
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
    if version:
        typer.echo(f"{__app_name__} version {__version__}")
        sys.exit(0)

    if update:
        if DEBUG:
            subprocess.run(["pip", "install", "-e", "."])
        else:
            subprocess.run(["pip", "install", "--upgrade", "archivist"])
        typer.echo("Updated to the latest version.")
        sys.exit(0)

