from mcp.server.fastmcp import FastMCP

from internet_archive_mcp.tools import register_tools

mcp = FastMCP("internet-archive-mcp")

register_tools(mcp)
