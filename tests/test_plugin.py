from unittest.mock import patch

import pytest
from danger_python.danger import Danger, Violation
from testfixtures.popen import MockPopen

from danger_flake8 import DangerFlake8


@pytest.mark.parametrize("modified_files", [["danger_flake8/plugin.py"]])
def test_lint_modified_files(danger: Danger):
    with open("tests/fixtures/flake8_output") as fixture:
        with patch("subprocess.Popen", new_callable=MockPopen) as popen:
            popen.set_command("flake8", stdout=fixture.read().encode("utf-8"))
            plugin = DangerFlake8()
            plugin.lint()

    assert danger.results.warnings == [
        Violation(
            message="F811 redefinition of unused 'DangerPlugin' from line 1",
            file_name="danger_flake8/plugin.py",
            line=2,
        ),
        Violation(
            message="E303 too many blank lines (3)",
            file_name="danger_flake8/plugin.py",
            line=6,
        ),
        Violation(
            message="W391 blank line at end of file",
            file_name="danger_flake8/plugin.py",
            line=11,
        ),
    ]


def test_lint_warnings_not_in_touched_files(danger: Danger):
    with open("tests/fixtures/flake8_output") as fixture:
        with patch("subprocess.Popen", new_callable=MockPopen) as popen:
            popen.set_command("flake8", stdout=fixture.read().encode("utf-8"))
            plugin = DangerFlake8()
            plugin.lint()

    assert danger.results.warnings == []


@pytest.mark.parametrize("created_files", [["tests/test_violation.py"]])
@pytest.mark.parametrize("modified_files", [["danger_flake8/violation.py"]])
def test_lint_touched_files(danger: Danger):
    with open("tests/fixtures/flake8_output") as fixture:
        with patch("subprocess.Popen", new_callable=MockPopen) as popen:
            popen.set_command("flake8", stdout=fixture.read().encode("utf-8"))
            plugin = DangerFlake8()
            plugin.lint()

    assert danger.results.warnings == [
        Violation(
            message="W391 blank line at end of file",
            file_name="danger_flake8/violation.py",
            line=21,
        ),
        Violation(
            message="F401 'profile' imported but unused",
            file_name="tests/test_violation.py",
            line=5,
        ),
    ]
