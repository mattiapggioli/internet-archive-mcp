import pytest

from internet_archive_mcp.server import mcp


@pytest.mark.anyio
async def test_ping_tool_is_registered():
    tools = await mcp.list_tools()
    tool_names = [tool.name for tool in tools]
    assert "ping" in tool_names
