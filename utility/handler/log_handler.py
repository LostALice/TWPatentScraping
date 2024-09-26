# Code by AkinoAlice@TyrantRey

from pprint import pformat
from typing import Any
import logging


class Logger(object):

    def __init__(
        self,
        filename: str,
        fmt: str = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
    ) -> None:
        logging.FileHandler(filename=filename, mode="a", encoding="utf-8")
        self.logger = logging.getLogger(__name__)
        self.handler = logging.StreamHandler()

        formatter = logging.Formatter(fmt)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)

    def debug(self, message: Any, format_json: bool = False) -> None:
        if format_json:
            self.logger.debug(pformat(message, indent=4))
        else:
            self.logger.debug(message)

    def info(self, message: Any, format_json: bool = False) -> None:
        if format_json:
            self.logger.info(pformat(message, indent=4))
        else:
            self.logger.info(message)

    def warning(self, message: Any, format_json: bool = False) -> None:
        if format_json:
            self.logger.warning(pformat(message, indent=4))
        else:
            self.logger.warning(message)

    def error(self, message: Any, format_json: bool = False) -> None:
        if format_json:
            self.logger.error(pformat(message, indent=4))
        else:
            self.logger.error(message)

    def critical(self, message: Any, format_json: bool = False) -> None:
        if format_json:
            self.logger.critical(pformat(message, indent=4))
        else:
            self.logger.critical(message)

    def log(self, level: str, message: Any) -> None:
        if level.capitalize == "DEBUG":
            self.logger.debug(message)

        if level.capitalize == "INFO":
            self.logger.info(message)

        if level.capitalize == "WARNING":
            self.logger.warning(message)

        if level.capitalize == "ERROR":
            self.logger.error(message)

        if level.capitalize == "CRITICAL":
            self.logger.critical(message)

    def log_json(self, level: str, message: Any) -> None:
        if level.capitalize == "DEBUG":
            self.logger.debug(pformat(message, indent=4))

        if level.capitalize == "INFO":
            self.logger.info(pformat(message, indent=4))

        if level.capitalize == "WARNING":
            self.logger.warning(pformat(message, indent=4))

        if level.capitalize == "ERROR":
            self.logger.error(pformat(message, indent=4))

        if level.capitalize == "CRITICAL":
            self.logger.critical(pformat(message, indent=4))
