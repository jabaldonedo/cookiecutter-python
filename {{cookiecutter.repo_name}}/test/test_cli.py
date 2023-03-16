"""Test cases for the cli module."""

from click.testing import CliRunner

from {{cookiecutter.package_name}} import main


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero.

    :param runner: The CliRunner object.
    """
    result = runner.invoke(main)

    assert result.exit_code == 0
