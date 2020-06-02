"""HackerLab 9000 Meta Library."""

import virtualbox

from hal9k import Track


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
        if track_name in self.get_machines():
            return Track(track_name)
        raise IndexError

    def get_machines(self):
        """Return the names of all available VMs."""
        return [vm.name for vm in self.__vbox.machines]
