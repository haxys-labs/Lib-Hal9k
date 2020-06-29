"""Test the hal9k Track class."""

from unittest import TestCase, mock

from hal9k import Track


class Hal9kTrackTest(TestCase):
    """Tests for the hal9k.Track class."""

    @mock.patch("hal9k.track.virtualbox.Session")
    def test_track_play(self, mock_Session):
        """Test the Track.play() function."""
        # Set up test environment.
        progress = mock.MagicMock()
        machine = mock.MagicMock()
        machine.launch_vm_process.return_value = progress
        vbox = mock.MagicMock()
        vbox.find_machine.return_value = machine
        session = mock.MagicMock()
        mock_Session.return_value = session
        # Spawn the `Track` class.
        with Track("demo track", vbox) as track:
            # Play the track.
            track.play()
            # Check what happened.
            mock_Session.assert_called()
            vbox.find_machine.assert_called_with("demo track")
            machine.launch_vm_process.assert_called_with(
                session, "headless", ""
            )
            progress.wait_for_completion.assert_called()
