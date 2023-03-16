"""{{ cookiecutter.project_name }} Command Line Interface module."""

from click import group


__all__ = ["main"]


@group()
def main() -> None:
    """{{ cookiecutter.project_name }} Command Line Interface."""
    pass
