"""HackerLab 9000 Track Library."""

import virtualbox
from virtualbox.library import LockType, VBoxErrorInvalidObjectState


class TrackException(Exception):
    """Custom exception for the track class."""


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
        try:
            progress = self.__machine.launch_vm_process(
                self.__session, "headless", ""
            )
            progress.wait_for_completion()
        except VBoxErrorInvalidObjectState:
            raise TrackException(
                "Could not play track. (Track currently playing.)"
            )

    def rewind(self):
        """Revert the VM to the PRODUCTION snapshot."""
        try:
            self.__machine.lock_machine(self.__session, LockType(2))
            snapshot = self.__machine.find_snapshot("PRODUCTION")
            progress = self.__session.machine.restore_snapshot(snapshot)
            progress.wait_for_completion()
            self.__session.unlock_machine()
        except VBoxErrorInvalidObjectState:
            raise TrackException(
                "Could not rewind track. (Track currently playing.)"
            )

    def status(self):
        """Check the VM status."""
        machine_state_return_value = [
            # -1: Error, 0: Stopped, 1: Running, 2: Rewinding, 3: Busy
            -1,  # 0: Null (never used by API)
            0,  # 1: Powered Off
            0,  # 2: Saved
            -1,  # 3: Teleported
            0,  # 4: Aborted
            1,  # 5: Running
            -1,  # 6: Paused
            -1,  # 7: Stuck
            -1,  # 8: Teleporting
            3,  # 9: Live Snapshotting
            3,  # 10: Starting
            3,  # 11: Stopping
            3,  # 12: Saving
            3,  # 13: Restoring
            -1,  # 14: Teleporting Paused VM
            -1,  # 15: Teleporting In
            1,  # 16: Deleting Snapshot Online
            -1,  # 17: Deleting Snapshot Paused
            -1,  # 18: Online Snapshotting
            2,  # 19: Restoring Snapshot
            0,  # 20: Deleting Snapshot
            -1,  # 21: Setting Up
            0,  # 22: Offline Snapshotting
        ]
        return machine_state_return_value[int(self.__machine.state)]

    def stop(self):
        """Stop the VM."""
        try:
            progress = self.__session.console.power_down()
            progress.wait_for_completion()
        except Exception as exception:
            try:
                if (
                    exception.errno == -2147418113
                    or exception.errno == 2147549183
                ):
                    raise TrackException(
                        "Could not stop track. (Track already stopped.)"
                    )
                print(f"Unknown Error Number: {exception.errno}")
                raise TrackException(
                    "Could not stop track. (Unknown error number.)"
                )
            except AttributeError:
                raise TrackException("Could not stop track. (Unknown error.)")
