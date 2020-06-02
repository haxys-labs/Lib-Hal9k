"""HackerLab 9000 Meta Library."""

import virtualbox

from hal9k.track import Track


class Meta:
    """The Meta Class.

    This class provides methods for interacting with VirtualBox.
    """

    def __init__(self):
        """Initialize the Meta class."""
        self.__vbox = virtualbox.VirtualBox()

    def __enter__(self):
        """Work with Context Managers."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Work with Context Managers."""
        del self.__vbox

    # Public Functions
    def fetch(self, track_name):
        """Return a Track controller for the specified track."""
        if track_name in self.get_tracks():
            return Track(track_name, self.__vbox)
        raise IndexError

    def get_tracks(self):
        """Return the names of all available VMs."""
        return [vm.name for vm in self.__vbox.machines]
