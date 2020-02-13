from danger_python.danger import Danger, Violation

from danger_flake8.plugin import DangerFlake8


def test_plugin_lint(danger: Danger):
    plugin = DangerFlake8()
    plugin.lint()

    assert danger.results.markdowns == []
    assert danger.results.fails == [Violation(message="fail")]
