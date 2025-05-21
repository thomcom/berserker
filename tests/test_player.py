import pytest
from advmodel.Player import Player

def test_use_mp_decreases_mp():
    player = Player("Test")
    player.create("Wizard")
    initial_mp = player.get_mp()
    player.use_mp(5)
    assert player.get_mp() == initial_mp - 5

from advmodel.Monster import Monster

def test_reward_adds_loot_to_inventory():
    player = Player("LootTester")
    player.create("Fighter")
    monster = Monster()
    monster.loot = {"item": "rat pelt"}
    monster.reward(player)
    assert "rat pelt" in player.get_inventory()

def test_reward_adds_gold_to_player():
    player = Player("GoldTester")
    player.create("Fighter")
    monster = Monster()
    monster.loot = {"gold": {"minimum": 10, "random": 0}}
    monster.reward(player)
    assert player.get_gold() == 10
