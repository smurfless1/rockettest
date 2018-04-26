import unittest
from item import Item
from cart import Cart
from catalog import Catalog
from rule import HappyHorse

class TestCart(unittest.TestCase):
    def test_create(self):
        pass

    def test_add_raw_item(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.additem(1)
        cart.additem(Item('A', 'B', '11.50'))
        self.assertEqual(1, len(cart._items))

    def test_add_key_item(self):
        cart = Cart()
        cart.additemfromkey('MK1')
        self.assertEqual(1, len(cart._items))

    def test_cart_str(self):
        cart = Cart()
        self.assertEqual('''Item                          Price
----                          -----

-----------------------------------
                              $0.00''', str(cart))

    def test_cart_with_item_str(self):
        cart = Cart()
        cart.additemfromkey('MK1')
        self.assertEqual(1, len(cart._items))
        self.assertEqual('''Item                          Price
----                          -----
MK1                           $4.75
-----------------------------------
                              $4.75''', str(cart))

    def test_cart_with_discount_str(self):
        cart = Cart()
        cart._rules.append(HappyHorse())
        cart.additemfromkey('OM1')
        cart.additemfromkey('AP1')
        self.assertEqual('''Item                          Price
----                          -----
OM1                           $3.69
AP1                           $6.00
            APOM             -$3.00
-----------------------------------
                              $6.69''', str(cart))

    def test_cart_from_multistring(self):
        cart = Cart()
        cart._rules.append(HappyHorse())
        cart.set_from('OM1, AP1')
        self.assertEqual('''Item                          Price
----                          -----
OM1                           $3.69
AP1                           $6.00
            APOM             -$3.00
-----------------------------------
                              $6.69''', str(cart))

    def test_cart_from_multistring2(self):
        cart = Cart()
        cart._rules.append(HappyHorse())
        cart.set_from('AP1 ')
        self.assertEqual('''Item                          Price
----                          -----
AP1                           $6.00
-----------------------------------
                              $6.00''', str(cart))

