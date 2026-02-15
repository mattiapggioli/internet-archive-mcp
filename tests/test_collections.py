from unittest.mock import patch

from internet_archive_mcp.ia_client import (
    get_curated_collections,
    search_collections,
)


def test_get_curated_collections_returns_list():
    result = get_curated_collections()
    assert isinstance(result, list)
    assert len(result) > 0


def test_curated_collections_have_required_keys():
    for col in get_curated_collections():
        assert "identifier" in col
        assert "title" in col
        assert "description" in col


def test_curated_collections_contains_nasa():
    ids = [c["identifier"] for c in get_curated_collections()]
    assert "nasa" in ids


@patch(
    "internet_archive_mcp.ia_client.internetarchive.search_items",
)
def test_search_collections_returns_list(mock_search):
    mock_search.return_value = iter(
        [
            {
                "identifier": "col1",
                "title": "Collection One",
                "description": "First collection",
            },
        ]
    )
    results = search_collections("photos")
    assert len(results) == 1
    assert results[0]["identifier"] == "col1"


@patch(
    "internet_archive_mcp.ia_client.internetarchive.search_items",
)
def test_search_collections_builds_details_url(mock_search):
    mock_search.return_value = iter([{"identifier": "col1"}])
    results = search_collections("photos")
    assert results[0]["details_url"] == ("https://archive.org/details/col1")


@patch(
    "internet_archive_mcp.ia_client.internetarchive.search_items",
)
def test_search_collections_passes_mediatype_query(
    mock_search,
):
    mock_search.return_value = iter([])
    search_collections("birds")
    query = mock_search.call_args[0][0]
    assert query == "birds AND mediatype:collection"


@patch(
    "internet_archive_mcp.ia_client.internetarchive.search_items",
)
def test_search_collections_respects_max_results(
    mock_search,
):
    items = [{"identifier": f"c{i}"} for i in range(20)]
    mock_search.return_value = iter(items)
    results = search_collections("many", max_results=3)
    assert len(results) == 3


@patch(
    "internet_archive_mcp.ia_client.internetarchive.search_items",
)
def test_search_collections_handles_missing_fields(
    mock_search,
):
    mock_search.return_value = iter([{"identifier": "sparse"}])
    results = search_collections("sparse")
    assert results[0]["title"] == ""
    assert results[0]["description"] == ""
