import json
from typing import Any, cast
from unittest.mock import patch

import pytest
from mcp.types import TextContent

from internet_archive_mcp.server import mcp

FAKE_ITEMS = [
    {
        "identifier": "tool_img",
        "title": "Tool Image",
        "creator": "Tester",
        "date": "2024-06-01",
        "description": "For testing",
    },
]


@pytest.mark.anyio
async def test_search_images_tool_is_registered():
    tools = await mcp.list_tools()
    tool_names = [t.name for t in tools]
    assert "search_images_tool" in tool_names


@pytest.mark.anyio
@patch(
    "internet_archive_mcp.tools.search_images.search_images",
)
async def test_search_images_tool_returns_json(mock_search):
    mock_search.return_value = [
        {
            "identifier": "tool_img",
            "title": "Tool Image",
            "creator": "Tester",
            "date": "2024-06-01",
            "description": "For testing",
            "thumbnail_url": ("https://archive.org/services/img/tool_img"),
            "details_url": ("https://archive.org/details/tool_img"),
        },
    ]

    result = await mcp.call_tool(
        "search_images_tool",
        {"query": "test"},
    )
    content_list = cast(tuple[list[Any], Any], result)[0]
    text = cast(TextContent, content_list[0]).text
    data = json.loads(text)
    assert isinstance(data, list)
    assert data[0]["identifier"] == "tool_img"


@pytest.mark.anyio
@patch(
    "internet_archive_mcp.tools.search_images.search_images",
)
async def test_search_images_tool_passes_max_results(
    mock_search,
):
    mock_search.return_value = []
    await mcp.call_tool(
        "search_images_tool",
        {"query": "cats", "max_results": 5},
    )
    mock_search.assert_called_once_with("cats", max_results=5, collection=None)


@pytest.mark.anyio
@patch(
    "internet_archive_mcp.tools.search_images.search_images",
)
async def test_search_images_tool_passes_collection(
    mock_search,
):
    mock_search.return_value = []
    await mcp.call_tool(
        "search_images_tool",
        {"query": "moon", "collection": "nasa"},
    )
    mock_search.assert_called_once_with(
        "moon", max_results=10, collection="nasa"
    )
