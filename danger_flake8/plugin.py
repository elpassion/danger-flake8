import subprocess

from danger_python.plugins import DangerPlugin

from danger_flake8.violation import violations


class DangerFlake8(DangerPlugin):
    def lint(self):
        result = subprocess.run(["flake8"], capture_output=True, text=True)
        violations_list = violations(result.stdout)

        for violation in violations_list:
            self.warn(violation.message, violation.file_name, violation.line)
