# internet-archive-mcp

An MCP server that exposes Internet Archive search and retrieval as tools for LLM agents. Any MCP-compatible client (Claude Desktop, Claude Code, etc.) can use it to search for images and browse collections on the Internet Archive.

## Tools

### `search_images_tool`

Search the Internet Archive for images.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | `str` | required | Keywords to search for |
| `max_results` | `int` | `10` | Maximum number of results |
| `collection` | `str \| None` | `None` | Collection identifier to restrict results to |

Returns JSON with `identifier`, `title`, `creator`, `date`, `description`, `thumbnail_url`, and `details_url` for each result.

### `list_curated_collections_tool`

Returns a curated list of Internet Archive collections that are particularly rich in high-quality images. No parameters.

Included collections: NASA, Flickr Commons, Metropolitan Museum of Art, Biodiversity Heritage Library, Smithsonian Institution, Brooklyn Museum, Library of Congress, Wellcome Collection, Internet Archive Books.

### `search_collections_tool`

Search for Internet Archive collections by keyword.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | `str` | required | Keywords to search for |
| `max_results` | `int` | `10` | Maximum number of results |

Returns JSON with `identifier`, `title`, `description`, and `details_url` for each collection.

## Setup

Requires Python >= 3.14 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Usage

### Claude Desktop

Add to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "internet-archive": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/internet-archive-mcp", "internet-archive-mcp"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add internet-archive -- uv run --directory /path/to/internet-archive-mcp internet-archive-mcp
```

### Direct (stdio)

```bash
uv run internet-archive-mcp
```

## Development

```bash
uv run pytest                # Run tests
uv run ruff check .          # Lint
uv run ruff format .         # Format
```
