import itertools
from typing import TypedDict

import internetarchive

from internet_archive_mcp.config import (
    COLLECTION_FIELDS,
    CURATED_COLLECTIONS,
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


class CollectionResult(TypedDict):
    identifier: str
    title: str
    description: str
    details_url: str


def get_curated_collections() -> list[dict[str, str]]:
    """Return the curated collections list from config."""
    return CURATED_COLLECTIONS


def search_collections(
    query: str,
    max_results: int = DEFAULT_MAX_RESULTS,
) -> list[CollectionResult]:
    """Search the Internet Archive for collections.

    Args:
        query: The search query string.
        max_results: Maximum number of results to return.

    Returns:
        A list of CollectionResult dictionaries.
    """
    results = internetarchive.search_items(
        f"{query} AND mediatype:collection",
        fields=COLLECTION_FIELDS,
    )
    return [
        CollectionResult(
            identifier=item.get("identifier", ""),
            title=item.get("title", ""),
            description=item.get("description", ""),
            details_url=DETAILS_URL.format(
                identifier=item.get("identifier", ""),
            ),
        )
        for item in itertools.islice(results, max_results)
    ]


def search_images(
    query: str,
    max_results: int = DEFAULT_MAX_RESULTS,
    collection: str | None = None,
) -> list[ImageResult]:
    """Search the Internet Archive for images matching a query.

    Args:
        query: The search query string.
        max_results: Maximum number of results to return.
        collection: Optional collection identifier to filter by.

    Returns:
        A list of ImageResult dictionaries containing metadata and URLs.
    """
    q = f"{query} AND mediatype:image"
    if collection:
        q += f" AND collection:{collection}"
    results = internetarchive.search_items(
        q,
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
