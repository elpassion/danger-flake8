import subprocess

from danger_python.plugins import DangerPlugin


class DangerFlake8(DangerPlugin):
    def lint(self):
        result = subprocess.run(["flake8"], capture_output=True, text=True)
        output = result.stdout
        self.markdown(output)
