from typing import List

from danger_python.danger import Violation


def violations(text_violations: str) -> List[Violation]:
    return list(map(violation, text_violations.split("\n")))


def violation(text_violation: str) -> Violation:
    message = text_violation.split(":")[3][1:]
    file_name = text_violation.split(":")[0][2:]
    line = text_violation.split(":")[1]
    return Violation(message=message, file_name=file_name, line=line)