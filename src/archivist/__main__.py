"""
Copyright 2023 Brad Edwards

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
from typing import Optional, List
import typer
import subprocess
from src.archivist import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.command()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Print the version number and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
        github_url: Optional[str] = typer.Option(
            None,
            "--github-url",
            "-g",
            help="The GitHub URL to download the code from."
        ),
        output_path: Optional[str] = typer.Option(
            None,
            "--output-path",
            "-o",
            help="The path where the GitHub repo will be cloned."
        ),
        branch: Optional[str] = typer.Option(
            None,
            "--branch",
            "-b",
            help="Specify a particular branch to clone."
        ),
        verbose: Optional[bool] = typer.Option(
            None,
            "--verbose",
            "-V",
            help="Enable verbose output."
        ),
        quiet: Optional[bool] = typer.Option(
            None,
            "--quiet",
            "-q",
            help="Suppress all output except errors."
        ),
        token: Optional[str] = typer.Option(
            None,
            "--token",
            "-k",
            help="Provide a GitHub authentication token."
        ),
        config: Optional[str] = typer.Option(
            "config.yaml",
            "--config",
            "-c",
            help="Path to a configuration file."
        ),
        update: Optional[bool] = typer.Option(
            None,
            "--update",
            "-u",
            help="Update the Archivist tool to the latest version."
        ),
        embeddings_path: Optional[str] = typer.Option(
            None,
            "--embeddings-path",
            "-e",
            help="The output path for vector embeddings."
        )
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
    typer.echo(f"{__app_name__} version {__version__}")
