def as_bool(value: str | None) -> bool:
    return True if value and value.strip().lower() in ['true', '1', 'yes', 'y'] else False


def as_int(value: str | None) -> int:
    return int(value) if value else 0
