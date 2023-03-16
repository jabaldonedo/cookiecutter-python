"""Configuration for the pytest test suite."""

from click.testing import CliRunner
from pytest import fixture


@fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces.

    :return: The CliRunner object.
    """
    return CliRunner()
