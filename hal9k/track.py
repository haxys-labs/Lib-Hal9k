"""HackerLab 9000 Track Library."""

import virtualbox


class Track:
    """The Track Class."""

    def __init__(self, track_name, vbox):
        """Initialize the Track class."""
        self.__vbox = vbox
        self.__session = virtualbox.Session()
        self.__machine = self.__vbox.find_machine(track_name)

    def __enter__(self):
        """Work with context managers."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Work with context managers."""

    def play(self):
        """Start the VM in headless mode."""
        progress = self.__machine.launch_vm_process(
            self.__session, "headless", ""
        )
        progress.wait_for_completion()
