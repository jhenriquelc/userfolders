"""MacOS implementation of userfolders.

Your application should not use this directly; "import userfolders" will
automatically select the correct implementation for the current platform.
"""

from os.path import expanduser


# MacOS uses standard folders in standard locations found in reference link #1.
# The localization of the names is done by Finder changing the dysplay
# name as stated in reference link #2.
#
# The userfolders module was originally designed from a Windows-centric
# perspective. Some Windows paths do not have a direct equivalent on Mac
# such as (Roaming and Local AppData). In these cases, userfolders attempts
# to return the nearest functional equivalent, but it is up to the library's
# consumer to ensure their application is using the appropriate path for
# what it seeks to do. 
#
# If you know of other applicable standards, or better equivalents than
# the ones used here, please feel free to submit a patch.
#
# References:
# [1] https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html
# [2] https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemAdvancedPT/LocalizingtheNameofaDirectory/LocalizingtheNameofaDirectory.html


def get_appdata() -> str:
    """Return the current user's roaming Application Data folder."""
    return expanduser("~/Library/Application Support")


def get_desktop() -> str:
    """Return the current user's Desktop folder."""
    return expanduser("~/Desktop")


def get_downloads() -> str:
    """Return the current user's Downloads folder."""
    return expanduser("~/Downloads")


def get_local_appdata() -> str:
    """Return the current user's local Application Data folder."""
    return expanduser("~/Library/Application Support")


def get_my_documents() -> str:
    """Return the current user's My Documents folder."""
    return expanduser("~/Documents")


def get_my_music() -> str:
    """Return the current user's My Music folder."""
    return expanduser("~/Music")


def get_my_pictures() -> str:
    """Return the current user's My Pictures folder."""
    return expanduser("~/Pictures")


def get_my_videos() -> str:
    """Return the current user's My Videos folder."""
    return expanduser("~/Movies")


def get_profile() -> str:
    """Return the current user's profile folder."""
    return expanduser("~")
