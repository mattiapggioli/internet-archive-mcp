import json

from mcp.server.fastmcp import FastMCP

from internet_archive_mcp.config import DEFAULT_MAX_RESULTS
from internet_archive_mcp.ia_client import (
    get_curated_collections,
    search_collections,
)


def register_collections(mcp: FastMCP) -> None:
    """Register collection tools on the MCP server.

    Args:
        mcp: The FastMCP server instance.
    """

    @mcp.tool()
    def list_curated_collections_tool() -> str:
        """List a curated set of Internet Archive collections.

        These collections are particularly rich in
        high-quality images. Use this as a starting point
        to discover good sources for visual material.

        Returns:
            A JSON string with curated collection metadata.
        """
        return json.dumps(get_curated_collections())

    @mcp.tool()
    def search_collections_tool(
        query: str,
        max_results: int = DEFAULT_MAX_RESULTS,
    ) -> str:
        """Search Internet Archive for collections.

        Search for collections matching a keyword. Use this
        to find niche or specialized image sources beyond
        the curated list.

        Args:
            query: Keywords to search for.
            max_results: Maximum number of results.

        Returns:
            A JSON string with matching collections.
        """
        results = search_collections(query, max_results=max_results)
        return json.dumps(results)
