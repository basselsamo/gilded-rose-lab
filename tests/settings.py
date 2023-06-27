import pytest

# this file contains all imports
# and xfail flags for all tests.
# this is the only file you need to import in your tests.

# use this to switch between the original and your refactored version.

#from gilded_rose.gilded_rose import GildedRose, Item

from gilded_rose.refactored.gilded_rose import GildedRose, Item

# XFAIL FLAGS
# use this to be able to refactor without the need to pertaining found
# bugs.

# initial xfail setting:
# xfail everything
xfail_bug_in_original = True  
xfail_bug_fix = True
xfail_new_features = True


# xfail setting during refactoring and bug fixing
# xfail everything!

# xfail_bug_in_original = True
# xfail_bug_fix = True
# xfail_new_features = True

# xfail setting after fixing bugs
# xfail_bug_fix should really fail now!

# xfail_bug_in_original = True
# xfail_bug_fix = False
# xfail_new_features = True


# after implementing the new feature:

# xfail_new_features = False

@pytest.mark.xfail(xfail_bug_in_original, reason="Bug in original implementation")
def test_bug_in_original():
    item = Item("Normal Item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

@pytest.mark.xfail(xfail_bug_fix, reason="Bug fix test")
def test_bug_fix():
    item = Item("Normal Item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19

@pytest.mark.xfail(xfail_new_features, reason="New feature test")
def test_new_feature():
    item = Item("Conjured Item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 18
