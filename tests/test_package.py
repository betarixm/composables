from importlib.metadata import distribution
from importlib.resources import files
from pathlib import Path

import composables


def test_package_license_matches_repository() -> None:
    repository_directory = Path(__file__).parents[1]
    repository_license = (repository_directory / "LICENSE").read_text(encoding="utf-8")
    package_license = (
        repository_directory / "packages" / "composables" / "LICENSE"
    ).read_text(encoding="utf-8")

    assert distribution("composables").metadata["License-Expression"] == "MIT"
    assert package_license == repository_license, (
        "The package must include the complete repository license"
    )


def test_package_includes_typing_marker() -> None:
    assert files(composables).joinpath("py.typed").is_file(), (
        "The installed package must include its PEP 561 typing marker"
    )


def test_console_entry_points_are_callable() -> None:
    for entry_point in distribution("composables").entry_points:
        if entry_point.group in {"console_scripts", "gui_scripts"}:
            assert callable(entry_point.load()), (
                f"Entry point {entry_point.name} must resolve to a callable"
            )
