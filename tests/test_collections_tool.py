import json
from unittest.mock import patch

import pytest

from internet_archive_mcp.server import mcp


@pytest.mark.anyio
async def test_list_curated_collections_tool_is_registered():
    tools = await mcp.list_tools()
    names = [t.name for t in tools]
    assert "list_curated_collections_tool" in names


@pytest.mark.anyio
async def test_list_curated_collections_tool_returns_json():
    content, _ = await mcp.call_tool(
        "list_curated_collections_tool",
        {},
    )
    data = json.loads(content[0].text)
    assert isinstance(data, list)
    ids = [c["identifier"] for c in data]
    assert "nasa" in ids


@pytest.mark.anyio
async def test_search_collections_tool_is_registered():
    tools = await mcp.list_tools()
    names = [t.name for t in tools]
    assert "search_collections_tool" in names


@pytest.mark.anyio
@patch(
    "internet_archive_mcp.tools.collections.search_collections",
)
async def test_search_collections_tool_returns_json(
    mock_search,
):
    mock_search.return_value = [
        {
            "identifier": "test_col",
            "title": "Test Collection",
            "description": "For testing",
            "details_url": ("https://archive.org/details/test_col"),
        },
    ]
    content, _ = await mcp.call_tool(
        "search_collections_tool",
        {"query": "test"},
    )
    data = json.loads(content[0].text)
    assert isinstance(data, list)
    assert data[0]["identifier"] == "test_col"


@pytest.mark.anyio
@patch(
    "internet_archive_mcp.tools.collections.search_collections",
)
async def test_search_collections_tool_passes_max_results(
    mock_search,
):
    mock_search.return_value = []
    await mcp.call_tool(
        "search_collections_tool",
        {"query": "art", "max_results": 3},
    )
    mock_search.assert_called_once_with("art", max_results=3)
