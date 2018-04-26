from price import Price

class Item:
    '''
    A somewhat inflexible item to be found in a store.
    '''
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = Price(price)
        # this is a list of Items that could affect the total price
        self.discounts = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        '''
        Return the partial receipt string with discount lines if present
        :return:
        '''
        lines = []
        '''
                35 chars wide
                left, 12
                middle stop @ 12
                right, 10
                part 1: main item
        CH1                            3.11
        '''

        parts = []
        parts.append('{:<12}'.format(self.code))
        parts.append('{:<12}'.format(''))
        parts.append('{:>11}'.format(str(self.price)))
        lines.append(''.join(parts))

        '''
        part 2: one or more discounts
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

        for d in self.discounts:
            parts = []
            parts.append('{:<12}'.format(''))
            parts.append('{:<12}'.format(d.code))
            parts.append('{:>11}'.format(str(d.price)))
            lines.append(''.join(parts))

        return '\n'.join(lines)

    def __add__(self, other):
        '''
        Support simple mathmatical addition
        :param other:
        :return: a new Item with the combined Price
        '''
        p = Price()
        p.cents = self.price.cents + other.price.cents
        return Item('','', p)
