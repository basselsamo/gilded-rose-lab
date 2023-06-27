from .item_decorator import ItemDecorator

class ConjuredDecorator(ItemDecorator):
    def update_quality(self):
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality -= 2
        else:
            self.item.quality -= 4
        self.item.quality = max(self.item.quality, 0)
        self.item.quality = min(self.item.quality, 50)