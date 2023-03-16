"""Common functions and classes for the package."""

from logging import CRITICAL
from logging import DEBUG
from logging import Formatter
from logging import StreamHandler
from logging import getLogger
from socket import gethostname


__all__ = ["set_logging"]
logger = getLogger(__name__)


def set_logging() -> None:
    """Set a logger handler for the package and configure the formatter and level.

    the user must call this function right at the start of the execution of the main program. After this, he can log
    any message throughout the program by instantiating the logger.

    ..  code-block:: python

        # on your main program
        from {{cookiecutter.package_name}} import set_logging

        set_logging()

        # on any other module
        from logging import getLogger

        logger = getLogger(__name__)
        logger.debug("this is a debug message")

    """
    root = getLogger()
    root.setLevel(CRITICAL)

    logger_ = getLogger("{{cookiecutter.package_name}}")

    ch = StreamHandler()
    ch.setLevel(DEBUG)

    formatter = Formatter(f"%(asctime)s - {gethostname()} - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    logger_.addHandler(ch)
    logger_.setLevel(DEBUG)

    logger_.debug("logging configured.")
