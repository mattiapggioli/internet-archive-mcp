import itertools
from typing import TypedDict

import internetarchive

from internet_archive_mcp.config import (
    DEFAULT_FIELDS,
    DEFAULT_MAX_RESULTS,
    DETAILS_URL,
    THUMBNAIL_URL,
)


class ImageResult(TypedDict):
    identifier: str
    title: str
    creator: str
    date: str
    description: str
    thumbnail_url: str
    details_url: str


def search_images(
    query: str,
    max_results: int = DEFAULT_MAX_RESULTS,
) -> list[ImageResult]:
    """Search the Internet Archive for images matching *query*."""
    results = internetarchive.search_items(
        f"{query} AND mediatype:image",
        fields=DEFAULT_FIELDS,
    )
    return [
        ImageResult(
            identifier=item.get("identifier", ""),
            title=item.get("title", ""),
            creator=item.get("creator", ""),
            date=item.get("date", ""),
            description=item.get("description", ""),
            thumbnail_url=THUMBNAIL_URL.format(
                identifier=item.get("identifier", ""),
            ),
            details_url=DETAILS_URL.format(
                identifier=item.get("identifier", ""),
            ),
        )
        for item in itertools.islice(results, max_results)
    ]
