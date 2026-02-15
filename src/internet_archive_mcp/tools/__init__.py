from mcp.server.fastmcp import FastMCP

from internet_archive_mcp.tools.search_images import (
    register_search_images,
)


def register_tools(mcp: FastMCP) -> None:
    """Wire up all tool modules."""
    register_search_images(mcp)
