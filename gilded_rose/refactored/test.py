import pytest

from gilded_rose.refactored.gilded_rose import GildedRose, Item
from tests.settings import xfail_new_features


@pytest.mark.xfail(xfail_new_features, reason="new feature: conjured items degrade twice as fast")
def test_conjured_item_degrades_twice_as_fast():
    item = Item("Conjured Item", 5, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 8

@pytest.mark.xfail(xfail_new_features, reason="new feature: conjured items degrade twice as fast")
def test_conjured_item_degrades_twice_as_fast_after_sell_in():
    item = Item("Conjured Item", 0, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 6

@pytest.mark.xfail(xfail_new_features, reason="new feature: conjured items degrade twice as fast")
def test_conjured_item_quality_does_not_become_negative():
    item = Item("Conjured Item", 5, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 0

@pytest.mark.xfail(xfail_new_features, reason="new feature: conjured items degrade twice as fast")
def test_conjured_item_quality_does_not_become_negative_after_sell_in():
    item = Item("Conjured Item", 0, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0
