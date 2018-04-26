from item import Item
from price import Price
from catalog import Catalog

class Rule:
    def handleitem(self, item):
        pass
    def reset(self):
        pass

class BOGOCoffeeRule(Rule):
    def __init__(self):
        self.reset()

    def handleitem(self, item):
        if item.code == 'CF1':
            if (self.free):
                item.discounts.append(Item('BOGO', 'Free coffee', '-' + str(Catalog['CF1'].price)))
            self.free = not self.free

    def reset(self):
        self.free = False

class AppleBulkRule(Rule):
    def __init__(self):
        self.prevapples = []
        self.applecount = 0

    def makediscount(self):
        return Item('AAPL', 'Bulk apple discount', '-1.50')

    def handleitem(self, item):
        if item.code == 'AP1':
            self.applecount += 1
            if self.applecount > 2:
                for pitem in self.prevapples:
                    pitem.discounts.append(self.makediscount())
                self.prevapples = []
                item.discounts.append(self.makediscount())
            else:
                self.prevapples.append(item)

    def reset(self):
        self.applecount = 0
        self.prevapples = []

class ChaiAndMilk(Rule):
    def __init__(self):
        self.reset()

    def handleitem(self, item):
        if item.code == 'CH1':
            self.chai = True
        if item.code == 'MK1':
            self.milk = True
            self.milkitem = item
        if self.milk and self.chai and not self.applied:
            self.applied = True
            pp = '-' + str(Catalog['MK1'].price)
            self.milkitem.discounts.append(Item('CHMK', '', pp))

    def reset(self):
        self.milk = False
        self.milkitem = None
        self.chai = False
        self.applied = False

class HappyHorse(Rule):
    def __init__(self):
        self.reset()

    def handleitem(self, item):
        if item.code == 'OM1':
            self.oatmeal = True

        if item.code == 'AP1':
            self.apples = True
            if self.applesitem is None:
                self.applesitem = item

        if self.oatmeal and self.apples and not self.applied:
            self.applied = True
            pp = Price()
            pp.cents = Catalog['AP1'].price.cents
            pp.cents /= 2
            pp.cents *= -1
            self.applesitem.discounts.append(Item('APOM','',str(pp)))

    def reset(self):
        self.oatmeal = False
        self.apples = False
        self.applied = False
        self.applesitem = None
