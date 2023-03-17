def as_bool(value: str | None) -> bool:
    return value and value.strip().lower() in ['true', '1', 'yes', 'y']


def as_int(value: str | None) -> int:
    return int(value) if value else 0
