from typing import List, Optional, Set, Iterator

from danger_python.danger import Violation


def violations(text_violations: str, touched_files: Set[str]) -> List[Violation]:
    if not text_violations:
        return []
    violations_list: Iterator[Violation] = filter(None, map(violation, text_violations.split("\n")))
    return list(filter(lambda x: x.file_name in touched_files, violations_list))


def violation(text_violation: str) -> Optional[Violation]:
    if not text_violation:
        return None
    message = text_violation.split(":")[3][1:]
    file_name = text_violation.split(":")[0][2:]
    line = text_violation.split(":")[1]
    return Violation(message=message, file_name=file_name, line=line)


