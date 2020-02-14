from danger_python.danger import Violation

from danger_flake8.violation import violations


def test_empty_output():
    output = ""

    violations_list = violations(output, {"danger_flake8/violation.py"})

    assert violations_list == []


def test_violations_in_touched_files():
    output = (
        "./danger_flake8/plugin.py:7:1: F401 'profile' imported but unused\n"
        "./danger_flake8/plugin.py:18:1: W391 blank line at end of file\n"
        "./tests/test_violation.py:5:1: F401 'profile' imported but unused\n"
        "./tests/test_violation.py:7:1: E302 expected 2 blank lines, found 1\n"
        "./tests/test_violation.py:42:1: W391 blank line at end of file\n"
        "./danger_flake8/violation.py:21:1: W391 blank line at end of file\n"
    )

    touched_files = {"danger_flake8/plugin.py", "danger_flake8/violation.py"}

    violations_list = violations(output, touched_files)

    assert violations_list == [
        Violation(
            message="F401 'profile' imported but unused",
            file_name="danger_flake8/plugin.py",
            line=7,
        ),
        Violation(
            message="W391 blank line at end of file",
            file_name="danger_flake8/plugin.py",
            line=18,
        ),
        Violation(
            message="W391 blank line at end of file",
            file_name="danger_flake8/violation.py",
            line=21,
        ),
    ]


def test_violations_not_in_touched_files():
    output = (
        "./danger_flake8/plugin.py:7:1: F401 'profile' imported but unused\n"
        "./danger_flake8/plugin.py:18:1: W391 blank line at end of file\n"
        "./tests/test_violation.py:5:1: F401 'profile' imported but unused\n"
        "./tests/test_violation.py:7:1: E302 expected 2 blank lines, found 1\n"
        "./tests/test_violation.py:42:1: W391 blank line at end of file\n"
        "./danger_flake8/violation.py:21:1: W391 blank line at end of file\n"
    )

    violations_list = violations(output, set())

    assert violations_list == []


