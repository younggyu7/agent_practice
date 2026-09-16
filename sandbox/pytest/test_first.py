def clean_title(raw):
    return raw.strip()


def test_erase_blank_frontback():
    assert clean_title("    hello pytest   ") == "hello pytest"


def test_notErase_notBlank():
    assert clean_title("hello test") == "hello test"


def emptyTitle_emptyString():
    assert clean_title("   ") == ""
