from typing import Optional


def tag(name: str, /, *content: str, class_: Optional[str] = None, **attrs: str) -> str:
    return repr((name, content, class_, attrs))
