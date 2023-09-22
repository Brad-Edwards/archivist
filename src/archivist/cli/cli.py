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

cli.py

Module for the command line interface. Parses command line arguments and
passes them to the main function.
"""
from src.archivist.__main__ import Config
from src.archivist.errors.errors import ERRORS, INVALID_CONFIG, NO_CONFIG

def handle_config(config: Config) -> Config:
    """
    Main entry point for handling all CLI options.

    Args:
        config (Config): The configuration object.

    Returns:
        Config: The updated configuration object.
    """
    if not config:
        raise ValueError(ERRORS[NO_CONFIG])

    if not isinstance(config, Config):
        raise ValueError(ERRORS[INVALID_CONFIG])

    if (not config.version
            and not config.github_url
            and not config.output_path
            and not config.branch
            and not config.verbose
            and not config.quiet
            and not config.token
            and not config.config_file
            and not config.update
            and not config.embeddings_path):
        raise ValueError(ERRORS[INVALID_CONFIG])

    handle_version(config)
    handle_github_url(config)
    handle_output_path(config)
    handle_branch(config)
    handle_verbose(config)
    handle_quiet(config)
    handle_token(config)
    handle_config_file(config)
    handle_update(config)
    handle_embeddings_path(config)
    return config



def handle_version(config: Config) -> None:
    """
    Handle the --version option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_github_url(config: Config) -> None:
    """Handle the --github-url option."""
    pass


def handle_output_path(config: Config) -> None:
    """
    Handle the --output-path option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_branch(config: Config) -> None:
    """
    Handle the --branch option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_verbose(config: Config) -> None:
    """
    Handle the --verbose option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_quiet(config: Config) -> None:
    """
    Handle the --quiet option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_token(config: Config) -> None:
    """
    Handle the --token option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_config_file(config: Config) -> None:
    """
    Handle the --config-file option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_update(config: Config) -> None:
    """
    Handle the --update option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass


def handle_embeddings_path(config: Config) -> None:
    """
    Handle the --embeddings-path option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    pass