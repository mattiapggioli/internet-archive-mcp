from mcp.server.fastmcp import FastMCP

mcp = FastMCP("internet-archive-mcp")


@mcp.tool()
def ping() -> str:
    """Return pong."""
    return "pong"
