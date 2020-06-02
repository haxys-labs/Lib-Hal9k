"""Test the hal9k Meta class."""

from unittest import TestCase, mock
from string import ascii_letters
from random import choice

from hal9k import Meta

class Hal9kMetaTest(TestCase):
    @staticmethod
    def random_name():
        return ''.join(choice(ascii_letters) for _ in range(5))


    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    def test_meta_get_machines(self, mock_VirtualBox):
        # Simulate the VirtualBox class.
        def random_name():
            return self.random_name()
        class Track:
            def __init__(self, name):
                self.name = name
        class Vbox:
            def __init__(self):
                self.machines = [Track(random_name) for index in range(5)]
        # Set up the test environment.
        vbox = Vbox()
        track_names = [track.name for track in vbox.machines]
        mock_VirtualBox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check the return value of the `get_machines` function.
            self.assertEqual(meta.get_machines(), track_names)

    @mock.patch("hal9k.meta.Meta.get_machines")
    @mock.patch("hal9k.meta.Track")
    def test_meta_fetch(self, mock_Track, mock_get_machines):
        # Simulate the Track class.
        class Track:
            def __init__(self, name):
                self.name = name
            def __eq__(self, other):
                if isinstance(other, Track):
                    return self.name == other.name
                return False
        # Set up the test environment.
        track_title = self.random_name()
        bad_title = self.random_name()
        track = Track(track_title)
        mock_Track.return_value = track
        mock_get_machines.return_value = [track_title]
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check that the function returns a Track.
            self.assertEqual(meta.fetch(track_title), track)
            # Check that the function returns IndexError with a bad track.
            with self.assertRaises(IndexError):
                meta.fetch(bad_title)
