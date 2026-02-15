import json

from mcp.server.fastmcp import FastMCP

from internet_archive_mcp.config import DEFAULT_MAX_RESULTS
from internet_archive_mcp.ia_client import search_images


def register_search_images(mcp: FastMCP) -> None:
    """Register the search_images tool on the MCP server.

    Args:
        mcp: The FastMCP server instance.
    """

    @mcp.tool()
    def search_images_tool(
        query: str,
        max_results: int = DEFAULT_MAX_RESULTS,
    ) -> str:
        """Search the Internet Archive for images.

        Args:
            query: Keywords to search for in the archive.
            max_results: Maximum number of results to return.

        Returns:
            A JSON string containing a list of image results with metadata and URLs.
        """
        results = search_images(query, max_results=max_results)
        return json.dumps(results)
