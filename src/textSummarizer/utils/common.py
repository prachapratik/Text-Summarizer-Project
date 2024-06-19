import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import Box, BoxError
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml):
    logger.info(f"Attempting to read YAML file: {path_to_yaml}")
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug(f"Raw content read from YAML file: {content} (type: {type(content)})")
            if content is None:
                logger.warning(f"YAML file {path_to_yaml} is empty, using default empty dictionary")
                content = {}  # Provide default empty dictionary if file is empty
            elif isinstance(content, str):
                logger.error(f"YAML file {path_to_yaml} contains invalid content: {content}")
                raise ValueError(f"YAML file {path_to_yaml} contains invalid content")

            logger.info(f"YAML file: {path_to_yaml} loaded successfully with content: {content}")
            return Box(content)
    except FileNotFoundError:
        logger.error(f"YAML file {path_to_yaml} not found")
        raise ValueError(f"YAML file {path_to_yaml} not found")
    except BoxError as e:  # Use BoxError instead of BoxValueError
        logger.error(f"Cannot extrapolate Box from string in file: {path_to_yaml}. Error: {e}")
        raise ValueError("Cannot extrapolate Box from string")
    except yaml.YAMLError as exc:
        logger.error(f"Error parsing YAML file {path_to_yaml}: {exc}")
        raise ValueError(f"Error parsing YAML file: {exc}")
    except Exception as e:
        logger.error(f"An error occurred while reading the YAML file {path_to_yaml}: {e}")
        raise ValueError(f"An error occurred while reading the YAML file: {e}")


    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    