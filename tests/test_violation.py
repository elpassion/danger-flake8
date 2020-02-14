from danger_python.danger import Violation

from danger_flake8.violation import violations


def test_not_empty_output():
    output = (
        "./danger_flake8/plugin.py:2:1: F811 redefinition of unused 'DangerPlugin' from line 1\n"
        "./danger_flake8/plugin.py:6:1: E303 too many blank lines (3)\n"
        "./danger_flake8/plugin.py:11:1: W391 blank line at end of file\n"
    )

    violations_list = violations(output)

    assert violations_list == [
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


def test_empty_output():
    output = ""

    violations_list = violations(output)

    assert violations_list == []


