"""HackerLab 9000 Meta Library."""

import virtualbox


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
    def get_machines(self):
        """Return the names of all available VMs."""
        return [vm.name for vm in self.__vbox.machines]
