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
from copy import deepcopy
from urllib.parse import urlparse
import os

from src.archivist.__main__ import Config
from src.archivist.errors.errors import UNSUPPORTED_CONFIG, NO_CONFIG, UNSUPPORTED_URL, NO_EMPTY_PATH, \
    UNSUPPORTED_PATH, NON_EXISTENT_PATH, UNSUPPORTED_CONFIG_PATH


def handle_config(config: Config) -> Config:
    """
    Main entry point for handling all CLI options.

    Args:
        config (Config): The configuration object.

    Returns:
        Config: The updated configuration object.
    """
    if not config:
        raise ValueError(NO_CONFIG)

    if not isinstance(config, Config):
        raise ValueError(UNSUPPORTED_CONFIG)

    if (not config.github_url
            and not config.output_path
            and not config.branch
            and not config.verbose
            and not config.quiet
            and not config.token
            and not config.config_file
            and not config.update
            and not config.embeddings_path):
        raise ValueError(UNSUPPORTED_CONFIG)

    config_copy = deepcopy(config)
    handle_github_url(config_copy)
    handle_output_path(config_copy)
    handle_branch(config_copy)
    handle_verbose(config_copy)
    handle_quiet(config_copy)
    handle_token(config_copy)
    handle_config_file(config_copy)
    handle_update(config_copy)
    handle_embeddings_path(config_copy)
    return config_copy


def handle_github_url(config: Config) -> None:
    """
    Handle the --github-url option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    github_url = config.github_url

    if not github_url:
        raise ValueError(UNSUPPORTED_URL)

    try:
        parsed_url = urlparse(github_url)
    except Exception as e:
        raise ValueError(UNSUPPORTED_URL)

    if parsed_url.netloc != "github.com":
        raise ValueError(UNSUPPORTED_URL)


def handle_output_path(config: Config) -> None:
    """
    Handle the --output-path option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    output_path = config.output_path

    if output_path is None or output_path.strip() == "":
        raise ValueError(NO_EMPTY_PATH)

    if not all(c.isalnum() or c in '-_./\\' for c in output_path):
        raise ValueError(UNSUPPORTED_PATH)


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
    config_file = config.config_file

    if config_file is None:
        return

    if not all(c.isalnum() or c in '-_./\\' for c in config_file):
        raise ValueError(UNSUPPORTED_CONFIG_PATH)

    if not os.path.exists(config_file):
        raise ValueError(NON_EXISTENT_PATH)


def handle_update(config: Config) -> None:
    """
    Handle the --update option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    if config.update and not isinstance(config.update, bool):
        raise ValueError(UNSUPPORTED_CONFIG)


def handle_embeddings_path(config: Config) -> None:
    """
    Handle the --embeddings-path option.

    Args:
        config (Config): The configuration object.

    Returns:
        None
    """
    embeddings_path = config.embeddings_path

    if embeddings_path is None:
        raise ValueError(NON_EXISTENT_PATH)

    if not all(c.isalnum() or c in '-_./\\' for c in embeddings_path):
        raise ValueError(UNSUPPORTED_PATH)
