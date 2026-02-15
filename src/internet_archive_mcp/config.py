DEFAULT_MAX_RESULTS = 10

DEFAULT_FIELDS = [
    "identifier",
    "title",
    "creator",
    "date",
    "description",
]

THUMBNAIL_URL = "https://archive.org/services/img/{identifier}"
DETAILS_URL = "https://archive.org/details/{identifier}"

COLLECTION_FIELDS = [
    "identifier",
    "title",
    "description",
]

CURATED_COLLECTIONS = [
    {
        "identifier": "nasa",
        "title": "NASA",
        "description": (
            "Space photography, Earth observation, mission imagery"
        ),
    },
    {
        "identifier": "flickrcommons",
        "title": "Flickr Commons",
        "description": (
            "Historical photography from libraries and museums worldwide"
        ),
    },
    {
        "identifier": "metropolitanmuseumofart",
        "title": "Metropolitan Museum of Art",
        "description": (
            "Artworks and artifacts from the Met's open access collection"
        ),
    },
    {
        "identifier": "biodiversitylibrary",
        "title": "Biodiversity Heritage Library",
        "description": (
            "Scientific illustrations of plants, animals, natural history"
        ),
    },
    {
        "identifier": "smithsonian",
        "title": "Smithsonian Institution",
        "description": ("Mixed media from Smithsonian Institution archives"),
    },
    {
        "identifier": "brooklynmuseum",
        "title": "Brooklyn Museum",
        "description": ("Art and cultural objects from the Brooklyn Museum"),
    },
    {
        "identifier": "library_of_congress",
        "title": "Library of Congress",
        "description": ("Historical prints, photographs, maps, posters"),
    }
]
