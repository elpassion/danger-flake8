from danger_python.plugins import DangerPlugin


class DangerFlake8(DangerPlugin):
    def lint(self):
        self.fail("fail")
