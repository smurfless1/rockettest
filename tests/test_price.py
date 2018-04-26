import unittest
from price import Price

class PriceTests(unittest.TestCase):
    def test_noargs(self):
        a = Price()
        self.assertEqual(a.cents, 0)
        a = Price(None)
        self.assertEqual(a.cents, 0)

    def test_str(self):
        a = Price()
        self.assertEqual(str(a), '$0.00')
        a = Price('5.01')
        self.assertEqual(str(a), '$5.01')

    def test_simplemath(self):
        # +- == math should work
        a = Price()
        c = Price('5.00')
        d = Price('5.01')

        self.assertEquals(0, a.cents)
        a += d
        self.assertEquals(501, a.cents)
        self.assertEquals(a, d)
        a -= c
        self.assertEquals(1, a.cents)

    def test_toomanydots(self):
        e = Price()
        with self.assertRaises(ValueError):
            e.setfrom('5.0.0.1')

    def test_clipsdollarsign(self):
        a = Price()
        a.setfrom('$5.01')
        self.assertEquals(501, a.cents)

    def test_negativeprice(self):
        a = Price('-$5.01')
        self.assertEquals(-501, a.cents)
