from internet_archive_mcp.config import (
    DEFAULT_FIELDS,
    DEFAULT_MAX_RESULTS,
    DETAILS_URL,
    THUMBNAIL_URL,
)


def test_default_max_results_is_positive_int():
    assert isinstance(DEFAULT_MAX_RESULTS, int)
    assert DEFAULT_MAX_RESULTS > 0


def test_default_fields_contains_identifier():
    assert "identifier" in DEFAULT_FIELDS


def test_thumbnail_url_has_placeholder():
    assert "{identifier}" in THUMBNAIL_URL


def test_details_url_has_placeholder():
    assert "{identifier}" in DETAILS_URL
