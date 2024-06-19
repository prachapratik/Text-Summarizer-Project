from pathlib import Path
from textSummarizer.logging import logger


CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

logger.info(f"Using CONFIG_FILE_PATH: {CONFIG_FILE_PATH}")
logger.info(f"Using PARAMS_FILE_PATH: {PARAMS_FILE_PATH}")