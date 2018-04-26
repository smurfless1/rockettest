from price import Price
from item import Item
from catalog import Catalog
import copy

class Cart:
    def __init__(self):
        self.total = Price()
        self.dirty = False

        # code: item map
        self.catalog = Catalog
        # Items the user has added to the cart
        # REALLY don't poke this directly folks
        self._items = []
        # set of rules to apply
        self._rules = []

    def set_from(self, cartstring):
        '''
        Add multiple keys from the catalog to the items list. Will throw if you pass it a
        key that is not in the catalog.
        :param cartstring: The comma separated list of keys to add, as in the test scenarios.
        :return: nothing
        '''
        parts = cartstring.split(' ')
        for key in parts:
            subpart = key.strip(',')
            self.additemfromkey(subpart.strip())

    def additem(self, item):
        '''
        Add a user-constructed Item object
        :param item: The Item to add
        :return: nothing, but will throw ValueError if the object passed is not an Item
        '''
        if not isinstance(item, Item):
            raise ValueError
        self.dirty = True
        self._items.append(item)

    def additemfromkey(self, key):
        '''
        Add an item to the order from a key in the catalog:
        cart.additemfromkey('MK1')
        :param key: key from the Catalog
        :return: nothing, but will throw ValueError if the key is not in the catalog
        '''
        _key = key.strip()
        if len(_key) < 1:
            return
        if _key not in Catalog.keys():
            raise ValueError
        self.dirty = True
        self._items.append(copy.deepcopy(self.catalog[_key]))

    def total(self):
        '''
        :return: the total price of this order as a Price object
        '''
        self.evaluate()
        return self.total()

    def evaluate(self):
        '''
        Calculate the total and prepare for printing or totalling
        Do no work if nothing has changed since the last eval
        :return:
        '''

        # todo there's another optimization to just keep this up to date always, but this is already huge
        if not self.dirty:
            return
        self.dirty = False

        for rule in self._rules:
            rule.reset()

        for item in self._items:
            # clear previous discounts from previous evaluations
            item.discounts = []
            for rule in self._rules:
                rule.handleitem(item)

        # compile the final total
        self.total.cents = 0
        for item in self._items:
            self.total.cents += item.price.cents
            for subitem in item.discounts:
                self.total.cents += subitem.price.cents

    def __str__(self):
        '''
        Calculate and return the full "receipt" formatted string.
        :return: Multiline string containing the calculated receipt.
        '''
        self.evaluate()
        '''
        Notes for me:
        
        35 chars wide
        left, 12
        middle stop @ 12
        right, 11
        
        Example:
Item                          Price
----                          -----
CH1                            3.11
AP1                            6.00
            APPL              -1.50
AP1                            6.00
            APPL              -1.50
AP1                            6.00
            APPl              -1.50
MK1                            4.75
            CHMK              -4.75
-----------------------------------
                              16.61
        '''

        header = '''Item                          Price
----                          -----'''
        footer = '''-----------------------------------'''

        lines = []
        for item in self._items:
            lines.append(str(item))
        middle = '\n'.join(lines)
        fullstring = '{0}\n{1}\n{2}\n{3:>35}'.format(header, middle, footer, str(self.total))

        return fullstring

