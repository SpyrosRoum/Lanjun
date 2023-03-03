import logging
import logging.config
from pathlib import Path

from lanjun.common import settings


def setup_logger() -> None:
    logging.config.fileConfig(
        Path(__file__).parent / "../../logging.conf", disable_existing_loggers=False
    )

    logging.getLogger().setLevel(settings.LOGGING_LEVEL)
