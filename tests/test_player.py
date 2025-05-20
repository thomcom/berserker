import pytest
from advmodel.Player import Player

def test_use_mp_decreases_mp():
    player = Player("Test")
    player.create("Wizard")
    initial_mp = player.get_mp()
    player.use_mp(5)
    assert player.get_mp() == initial_mp - 5
