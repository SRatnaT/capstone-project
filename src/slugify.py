import re
import unicodedata


def _to_ascii(s: str) -> str:

    normalized = unicodedata.normalize("NFKD", s)
    ascii_bytes = normalized.encode("ascii", "ignore")
    return ascii_bytes.decode("ascii")


def slugify(text: str, ascii_only: bool = False) -> str:

    if not text:
        return ""

    # 1. lowercase and strip whitespace
    s = text.strip().lower()

    # 2. optionally convert to ASCII
    if ascii_only:
        s = _to_ascii(s)
        # only allow ascii letters and digits
        s = re.sub(r"[^0-9a-z]+", "-", s)
    else:
        # allow Unicode letters and numbers
        s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE)

    # 3. remove leading and trailing hyphens
    s = s.strip("-")

    return s
