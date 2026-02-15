from mcp.server.fastmcp import FastMCP

from internet_archive_mcp.tools import register_tools

mcp = FastMCP("internet-archive-mcp")


@mcp.tool()
def ping() -> str:
    """Return pong.

    Returns:
        The string 'pong'.
    """
    return "pong"


register_tools(mcp)
