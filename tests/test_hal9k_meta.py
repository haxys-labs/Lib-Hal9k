"""Test the hal9k Meta class."""

from random import choice
from string import ascii_letters
from unittest import TestCase, mock

import virtualbox

from hal9k import Meta


class Hal9kMetaTest(TestCase):
    """Tests for the hal9k.Meta class."""

    @staticmethod
    def random_name():
        """Produce a random string of five characters."""
        return "".join(choice(ascii_letters) for _ in range(5))

    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    def test_meta_get_tracks(self, mock_virtualbox):
        """Test the Meta.get_tracks() function."""
        # Set up test environment.
        vms = [mock.MagicMock() for index in range(5)]
        prod_vms = list()
        track_names = list()
        indices = list(range(5))
        for _ in range(choice(range(2, 5))):
            # Select from two to four systems to be in "production."
            prod_vms.append(indices.pop(choice(range(len(indices)))))
        for (index, _) in enumerate(vms):
            vms[index].name = self.random_name()
            if index in prod_vms:
                # This one's live.
                vms[index].find_snapshot.return_value = mock.MagicMock()
                track_names.append(vms[index].name)
            else:
                # This one's not.
                vms[
                    index
                ].find_snapshot.side_effect = (
                    virtualbox.library.VBoxErrorObjectNotFound
                )
        vbox = mock.MagicMock()
        vbox.machines = vms
        mock_virtualbox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check the return value of the `get_tracks` function.
            self.assertEqual(meta.get_tracks(), track_names)

    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    @mock.patch("hal9k.meta.Meta.get_tracks")
    @mock.patch("hal9k.meta.Track")
    def test_meta_fetch(self, mock_track, mock_get_tracks, mock_virtualbox):
        """Test the Meta.fetch() function."""
        # Set up the test environment.
        track_title = self.random_name()
        bad_title = self.random_name()
        track = mock.MagicMock()
        track.name = track_title
        mock_track.return_value = track
        mock_get_tracks.return_value = [track_title]
        vbox = mock.MagicMock()
        mock_virtualbox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check that the function returns a Track.
            self.assertEqual(meta.fetch(track_title), track)
            mock_track.assert_called_with(track_title, vbox)
            # Check that the function returns IndexError with a bad track.
            with self.assertRaises(IndexError):
                meta.fetch(bad_title)
