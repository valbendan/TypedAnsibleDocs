from packaging.version import parse

__all__ = ["my_version_cmp"]


def my_version_cmp(v1: str, v2: str) -> int:
    t1 = parse(v1)
    t2 = parse(v2)
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1
    return 0
