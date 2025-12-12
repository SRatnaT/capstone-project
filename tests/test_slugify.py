import pytest

from slugify import slugify


@pytest.mark.parametrize(
    "input_text, ascii_only , expected",
    [
        ("My Cool Project", False, "my-cool-project"),
        ("  Leading and trailing  ", False, "leading-and-trailing"),
        ("Multiple   spaces", False, "multiple-spaces"),
        ("Hello, World!", False, "hello-world"),
        ("Café con leche", False, "café-con-leche"),
        ("Café con leche", True, "cafe-con-leche"),
        ("", False, ""),
        ("123 Go", False, "123-go"),
        ("MixedCASE Title", False, "mixedcase-title"),
    ],
)
def test_basic_slug(input_text, ascii_only, expected):
    assert slugify(input_text, ascii_only) == expected


def test_underscores_removed():

    assert (
        slugify("some_text_with_underscores", ascii_only=True)
        == "some-text-with-underscores"
    )
