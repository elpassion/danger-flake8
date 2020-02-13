import subprocess
from typing import List, Dict, Any
from unittest.mock import patch

from danger_python.danger import Danger

from danger_flake8 import DangerFlake8


def test_lint_run_flake8_subprocess(danger: Danger):
    def fake_run(commands: List[str], **kwargs: Dict[str, Any]) -> subprocess.CompletedProcess:
        if (
                commands == ["flake8"]
                and kwargs["capture_output"] == True
                and kwargs["text"] == True
        ):
            return subprocess.CompletedProcess(["flake8"], 0, stdout="output".encode("utf-8"))
        raise ValueError(f"Could not stub commands: {commands}")

    with patch("subprocess.run") as mock_subprocess:
        mock_subprocess.side_effect = fake_run
        plugin = DangerFlake8()
        plugin.lint()

    assert danger.results.markdowns == ["output"]
