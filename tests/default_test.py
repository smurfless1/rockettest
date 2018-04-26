import unittest
from cart import Cart
import rule

class MarketTest1(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart._rules.append(rule.BOGOCoffeeRule())
        self.cart._rules.append(rule.AppleBulkRule())
        self.cart._rules.append(rule.ChaiAndMilk())
        self.cart._rules.append(rule.HappyHorse())

    def test_minimal(self):
        basketstr = 'CH1, AP1'
        expected = '$9.11'
        self.cart.set_from(basketstr)
        self.assertEqual(911, self.cart.total.cents)

    def test_one(self):
        basketstr = 'CH1, AP1, AP1, AP1, MK1'
        expected = '$16.61'
        self.cart.set_from(basketstr)
        self.assertEqual(1661, self.cart.total.cents)

    def test_two(self):
        basketstr = 'CH1, AP1, CF1, MK1'
        expected = '$20.34'
        self.cart.set_from(basketstr)
        self.assertEqual(2034, self.cart.total.cents)

    def test_three(self):
        basketstr = 'MK1, AP1'
        expected = '$10.75'
        self.cart.set_from(basketstr)
        self.assertEqual(1075, self.cart.total.cents)

    def test_two_coffees(self):
        basketstr = 'CF1, CF1'
        expected = '$11.23'
        self.cart.set_from(basketstr)
        self.assertEqual(1123, self.cart.total.cents)

    def test_five(self):
        basketstr = 'AP1, AP1, CH1, AP1'
        expected = '$16.61'
        self.cart.set_from(basketstr)
        self.assertEqual(1661, self.cart.total.cents)

