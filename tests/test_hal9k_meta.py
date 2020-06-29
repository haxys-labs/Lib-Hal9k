"""Test the hal9k Meta class."""

from random import choice
from string import ascii_letters
from unittest import TestCase, mock

from hal9k import Meta


class Hal9kMetaTest(TestCase):
    """Tests for the hal9k.Meta class."""

    @staticmethod
    def random_name():
        """Produce a random string of five characters."""
        return "".join(choice(ascii_letters) for _ in range(5))

    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    def test_meta_get_tracks(self, mock_VirtualBox):
        """Test the Meta.get_tracks() function."""
        # Simulate the VirtualBox class.
        def random_name():
            """Proxy function."""
            return self.random_name()

        class Track:
            """Mock Track."""

            def __init__(self, name):
                """Initialize the mock Track."""
                self.name = name

        class Vbox:
            """Mock Vbox."""

            def __init__(self):
                """Initialize the mock Vbox."""
                self.machines = [Track(random_name) for index in range(5)]

        # Set up the test environment.
        vbox = Vbox()
        track_names = [track.name for track in vbox.machines]
        mock_VirtualBox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check the return value of the `get_tracks` function.
            self.assertEqual(meta.get_tracks(), track_names)

    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    @mock.patch("hal9k.meta.Meta.get_tracks")
    @mock.patch("hal9k.meta.Track")
    def test_meta_fetch(self, mock_Track, mock_get_tracks, mock_VirtualBox):
        """Test the Meta.fetch() function."""

        class Track:
            """Mock Track."""

            def __init__(self, name):
                """Initialize the mock Track."""
                self.name = name

            def __eq__(self, other):
                """Compare the mock Track with another object."""
                if isinstance(other, Track):
                    return self.name == other.name
                return False

        # Set up the test environment.
        track_title = self.random_name()
        bad_title = self.random_name()
        track = Track(track_title)
        mock_Track.return_value = track
        mock_get_tracks.return_value = [track_title]
        vbox = mock.MagicMock()
        mock_VirtualBox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check that the function returns a Track.
            self.assertEqual(meta.fetch(track_title), track)
            mock_Track.assert_called_with(track_title, vbox)
            # Check that the function returns IndexError with a bad track.
            with self.assertRaises(IndexError):
                meta.fetch(bad_title)
