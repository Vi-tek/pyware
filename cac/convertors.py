def convert_to_string(phrase: bytes) -> str:
    try:
        return str(phrase, "utf-8")
    except TypeError:
        return ""


def convert_to_bytes(phrase: str) -> bytes:
    try:
        return bytes(phrase, "utf-8")
    except TypeError:
        return b''
