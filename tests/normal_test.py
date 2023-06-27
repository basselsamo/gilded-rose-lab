from _pytest.nodes import Item

from tests.settings import *

# create tests for normal items here...

def test_something():
    item = Item("name item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

# aged_brie_test.py
def test_aged_brie_item():
    item = Item("Aged Brie", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 21

# sulfuras_test.py
def test_sulfuras_item():
    item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 0
    assert item.quality == 80

# backstage_passes_test.py
def test_backstage_passes_item():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 11
    assert item.quality == 21

    # conjured_items_test.py
def test_conjured_item():
    item = Item("Conjured Item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 18
