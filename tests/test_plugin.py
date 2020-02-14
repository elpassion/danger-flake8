from unittest.mock import patch

from danger_python.danger import Danger, Violation
from testfixtures.popen import MockPopen

from danger_flake8 import DangerFlake8


def test_lint_run_flake8_subprocess(danger: Danger):
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
