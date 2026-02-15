from unittest.mock import patch

from internet_archive_mcp.ia_client import search_images

FAKE_ITEMS = [
    {
        "identifier": "img001",
        "title": "Sunset",
        "creator": "Alice",
        "date": "2024-01-01",
        "description": "A sunset photo",
    },
    {
        "identifier": "img002",
        "title": "Mountain",
        "creator": "Bob",
        "date": "2024-02-01",
        "description": "A mountain photo",
    },
]


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_returns_list(mock_search):
    mock_search.return_value = iter(FAKE_ITEMS)
    results = search_images("nature")
    assert len(results) == 2
    assert results[0]["identifier"] == "img001"
    assert results[1]["identifier"] == "img002"


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_builds_urls(mock_search):
    mock_search.return_value = iter(FAKE_ITEMS[:1])
    results = search_images("sunset")
    assert results[0]["thumbnail_url"] == (
        "https://archive.org/services/img/img001"
    )
    assert results[0]["details_url"] == ("https://archive.org/details/img001")


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_passes_query_with_mediatype(mock_search):
    mock_search.return_value = iter([])
    search_images("cats")
    call_args = mock_search.call_args
    assert "cats AND mediatype:image" == call_args[0][0]


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_respects_max_results(mock_search):
    many_items = [
        {"identifier": f"img{i}", "title": f"Title {i}"} for i in range(20)
    ]
    mock_search.return_value = iter(many_items)
    results = search_images("lots", max_results=3)
    assert len(results) == 3


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_handles_missing_fields(mock_search):
    mock_search.return_value = iter([{"identifier": "sparse"}])
    results = search_images("sparse")
    assert results[0]["title"] == ""
    assert results[0]["creator"] == ""


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_with_collection(mock_search):
    mock_search.return_value = iter([])
    search_images("stars", collection="nasa")
    query = mock_search.call_args[0][0]
    assert query == "stars AND mediatype:image AND collection:nasa"


@patch("internet_archive_mcp.ia_client.internetarchive.search_items")
def test_search_images_without_collection(mock_search):
    mock_search.return_value = iter([])
    search_images("stars")
    query = mock_search.call_args[0][0]
    assert "collection:" not in query
