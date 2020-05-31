"""Test the hal9k Meta class."""

from unittest import TestCase, mock
from string import ascii_letters
from random import choice

from hal9k import Meta

class Hal9kMetaTest(TestCase):
    @mock.patch("hal9k.meta.virtualbox.VirtualBox")
    def test_meta_list_machines(self, mock_VirtualBox):
        # Simulate the VirtualBox class.
        class Box:
            def __init__(self, name):
                self.name = name
        class Vbox:
            def __init__(self):
                self.machines = [Box(f"box-{index}") for index in range(5)]
        # Set up the test environment.
        vbox = Vbox()
        box_names = [box.name for box in vbox.machines]
        mock_VirtualBox.return_value = vbox
        # Spawn the `Meta` class.
        with Meta() as meta:
            # Check the return value of the `get_machines` function.
            self.assertEqual(meta.get_machines(), box_names)
