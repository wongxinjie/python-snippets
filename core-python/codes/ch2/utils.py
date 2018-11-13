def ensure_bytes(text, encoding="utf-8"):
    if isinstance(text, bytes):
        return text
    return str(text).encode(encoding)


def ensure_unicode(text, encoding="utf-8"):
    if isinstance(text, bytes):
        return text.decode("utf-8")
    return str(text)
