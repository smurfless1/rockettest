import unittest
from item import Item

class ItemTest(unittest.TestCase):
    def item_badprice(self):
        ii = Item('a', 'b', 'c')
        self.assertIsNone(ii)

    def test_item_created(self):
        ii = Item('a', 'b', '11.50')

    def test_itemstr(self):
        ii = Item('a', 'b', '11.50')
        #                '------------++++++++++++-----------'
        self.assertEqual('a                            $11.50', str(ii))

    def test_itemstr_negative(self):
        ii = Item('a', 'b', '-11.50')
        #                '------------++++++++++++-----------'
        self.assertEqual('a                           -$11.50', str(ii))

    def test_itemstr_with_discounts(self):
        ii = Item('a', 'b', '11.50')
        ii.discounts.append(Item('d','e','-4.00'))
        #                '------------++++++++++++-----------'
        self.assertEqual('a                            $11.50\n            d                -$4.00', str(ii))

