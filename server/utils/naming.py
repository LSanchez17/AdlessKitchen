def to_camel(string: str) -> str:
    """
    Convert a snake_case string to camelCase.
    Example: "first_name" -> "firstName"
    """
    parts = string.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])