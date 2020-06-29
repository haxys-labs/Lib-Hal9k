"""Test the hal9k Track class."""

from unittest import TestCase, mock

from hal9k import Track


class Hal9kTrackTest(TestCase):
    """Tests for the hal9k.Track class."""

    def setUp(self):
        """Set up for the Track tests."""
        self.console = mock.MagicMock()
        self.machine = mock.MagicMock()
        self.progress = mock.MagicMock()
        self.session = mock.MagicMock()
        self.vbox = mock.MagicMock()
        self.reset()

    def reset(self):
        """Reset the mocks."""
        self.progress.reset_mock()
        self.machine.reset_mock()
        self.machine.state = 1  # Stopped
        self.machine.launch_vm_process.return_value = self.progress
        self.vbox.reset_mock()
        self.vbox.find_machine.return_value = self.machine
        self.session.reset_mock()
        self.session.console = self.console

    @mock.patch("hal9k.track.virtualbox.Session")
    def test_track_init(self, mock_Session):
        """Test Track initialization."""
        # Set up test environment.
        mock_Session.return_value = self.session
        # Spawn the `Track` class.
        with Track("demo track", self.vbox) as track:
            # Check that the track was properly instantiated.
            mock_Session.assert_called()
            self.vbox.find_machine.assert_called_with("demo track")
        self.reset()

    @mock.patch("hal9k.track.virtualbox.Session")
    def test_track_status(self, mock_Session):
        """Test the Track.status() function."""
        # Set up test environment.
        mock_Session.return_value = self.session

        class typeCastMe:
            """A class that demands typecasting."""

            def __init__(self, value):
                """Initialize the class."""
                self.value = value

            def __int__(self):
                """Return the integer format of the class."""
                return self.value

        # Set up a series of tests.
        tests = [
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
        # Spawn the `Track` class.
        with Track("demo track", self.vbox) as track:
            for (index, value) in enumerate(tests):
                # Check return values for various machine states.
                # Each machine state is an object that should be typecast
                # into an integer.
                self.machine.state = typeCastMe(index)
                self.assertEqual(track.status(), value)
        self.reset()

    @mock.patch("hal9k.track.virtualbox.Session")
    def test_track_play(self, mock_Session):
        """Test the Track.play() function."""
        # Set up test environment.
        mock_Session.return_value = self.session
        # Spawn the `Track` class.
        with Track("demo track", self.vbox) as track:
            # Play the track.
            track.play()
            # Check what happened.
            self.machine.launch_vm_process.assert_called_with(
                self.session, "headless", ""
            )
            self.progress.wait_for_completion.assert_called()
        self.reset()

    @mock.patch("hal9k.track.virtualbox.Session")
    def test_track_stop(self, mock_Session):
        """Test the Track.stop() function."""
        # Set up test environment.
        mock_Session.return_value = self.session
        # Spawn the `Track` class.
        with Track("demo track", self.vbox) as track:
            # Stop the track.
            track.stop()
            # Check what happened.
            self.session.console.power_down.assert_called()
        self.reset()
