import os

from .base import *  # noqa: F401, F403


CACHES = {
    "default": {
        # Use dummy cache (ie, no caching):
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Don't use S3 for tests
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "..", "tests", "_media")  # noqa: F405
MEDIA_URL = "/media/"


# Make it easier/quicker to test pagination:
REST_FRAMEWORK["PAGE_SIZE"] = 5  # noqa: F405
