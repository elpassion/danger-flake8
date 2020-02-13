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

    assert danger.results.markdowns == [
        Violation(
            message=(
                "./danger_flake8/plugin.py:2:1: F811 redefinition of unused 'DangerPlugin' from line 1\n"
                "./danger_flake8/plugin.py:6:1: E303 too many blank lines (3)\n"
                "./danger_flake8/plugin.py:11:1: W391 blank line at end of file"
            )
        )
    ]
