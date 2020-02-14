from typing import List, Optional

from danger_python.danger import Violation


def violations(text_violations: str) -> List[Violation]:
    if not text_violations.split():
        return []
    results = list(map(violation, text_violations.split("\n")))
    return list(filter(None, results))


def violation(text_violation: str) -> Optional[Violation]:
    if not text_violation.split():
        return
    message = text_violation.split(":")[3][1:]
    file_name = text_violation.split(":")[0][2:]
    line = text_violation.split(":")[1]
    return Violation(message=message, file_name=file_name, line=line)
