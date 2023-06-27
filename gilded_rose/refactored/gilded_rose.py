# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes":
                if item.quality > 0:
                    if item.name != "Sulfuras":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes":
                        if item.quality > 0:
                            if item.name != "Sulfuras":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class AgedBrieItemStrategy(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasItemStrategy(Item):
    def update_quality(self, item):
        pass


class BackstagePassItemStrategy(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            if item.sell_in < 0:
                item.quality = 0
            elif item.sell_in < 5:
                item.quality += 3
            elif item.sell_in < 10:
                item.quality += 2
            else:
                item.quality += 1

class ConjuredItemStrategy(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


    def get_item_strategy(self, item):
        if item.name == "Aged Brie":
            return AgedBrieItemStrategy()
        elif item.name == "Sulfuras":
            return SulfurasItemStrategy()
        elif item.name == "Backstage passes":
            return BackstagePassItemStrategy()
        elif item.name == "Conjured":
            return ConjuredItemStrategy()
        else:
            return Item();











