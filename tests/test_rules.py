import unittest
from item import Item
from cart import Cart
from catalog import Catalog
from rule import BOGOCoffeeRule, AppleBulkRule, ChaiAndMilk, HappyHorse
import copy

class RuleTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_coffee(self):
        rule = BOGOCoffeeRule()
        items = [
            copy.deepcopy(Catalog['CF1']),
            copy.deepcopy(Catalog['CF1']),
            copy.deepcopy(Catalog['CF1']),
            copy.deepcopy(Catalog['CF1'])
        ]
        map(rule.handleitem, items)
        self.assertEqual(0, len(items[0].discounts))
        self.assertEqual(1, len(items[1].discounts))
        self.assertEqual(0, len(items[2].discounts))
        self.assertEqual(1, len(items[3].discounts))
        unused = str(rule)
        self.assertTrue(len(unused) > 0)

    def test_applerule_less(self):
        rule = AppleBulkRule()
        items = [
            copy.deepcopy(Catalog['AP1']),
            copy.deepcopy(Catalog['AP1']),
        ]
        map(rule.handleitem, items)
        self.assertEqual(0, len(items[0].discounts))
        self.assertEqual(0, len(items[1].discounts))

    def test_applerule(self):
        rule = AppleBulkRule()
        items = [
            copy.deepcopy(Catalog['AP1']),
            copy.deepcopy(Catalog['AP1']),
            copy.deepcopy(Catalog['AP1']),
            copy.deepcopy(Catalog['AP1'])
        ]
        map(rule.handleitem, items)
        self.assertEqual(1, len(items[0].discounts))
        self.assertEqual(1, len(items[1].discounts))
        self.assertEqual(1, len(items[2].discounts))
        self.assertEqual(1, len(items[3].discounts))

    def test_chairule_forward(self):
        rule = ChaiAndMilk()
        items = [
            copy.deepcopy(Catalog['CH1']),
            copy.deepcopy(Catalog['MK1']),
        ]
        map(rule.handleitem, items)
        self.assertEqual(0, len(items[0].discounts))
        self.assertEqual(1, len(items[1].discounts))

    def test_chairule_backward(self):
        rule = ChaiAndMilk()
        items = [
            copy.deepcopy(Catalog['MK1']),
            copy.deepcopy(Catalog['CH1']),
        ]
        map(rule.handleitem, items)
        self.assertEqual(1, len(items[0].discounts))
        self.assertEqual(0, len(items[1].discounts))

    def test_horse(self):
        rule = HappyHorse()
        items = [
            copy.deepcopy(Catalog['AP1']),
            copy.deepcopy(Catalog['OM1']),
            copy.deepcopy(Catalog['AP1']),
        ]
        map(rule.handleitem, items)
        self.assertEqual(1, len(items[0].discounts))
        self.assertEqual(0, len(items[1].discounts))
        self.assertEqual(0, len(items[2].discounts))

