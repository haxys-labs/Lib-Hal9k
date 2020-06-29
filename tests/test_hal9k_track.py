"""Test the hal9k Track class."""

from unittest import TestCase, mock

from hal9k import Track


class Hal9kTrackTest(TestCase):
    """Tests for the hal9k.Track class."""
    def setUp(self):
        """Set up for the Track tests."""
        self.progress = mock.MagicMock()
        self.machine = mock.MagicMock()
        self.machine.launch_vm_process.return_value = self.progress
        self.vbox = mock.MagicMock()
        self.vbox.find_machine.return_value = self.machine
        self.session = mock.MagicMock()

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
