
# make sure we're using the right kind of string comparison between python2 and python3
try:
   basestring
except NameError:
   basestring=str

class Price:
    ''' Convert everything to just cents, and provide pretty printers, because float can surprise you'''
    def __init__(self, value=None):
        self.cents = 0
        if value is not None:
            try:
                self.setfrom(value)
            except ValueError:
                print("Uhno.")

    def setfrom(self, what):
        try:
            # convert str -> float -> cents and store that
            if not isinstance(what, basestring):
                return
            what = what.replace('$','')

            neg = False
            if '-' in what:
                neg = True
            what = what.replace('-','')

            if '.' in what:
                parts = what.split('.')
                if (len(parts) != 2):
                    raise ValueError('Too many decimal points')
                self.cents = 100 * int(parts[0])
                self.cents += int(parts[1][:2])
            else:
                self.cents = 100 * int(what)

            if neg:
                self.cents *= -1
        except:
            raise ValueError('Could not parse the source price')

    def __repr__(self):
        return str(self)

    def __str__(self):
        neg = ''
        if self.cents < 0:
            neg = '-'

        return '%s$%d.%02d' % (neg, abs(self.cents) / 100, abs(self.cents) % 100)

    def __lt__(self, other):
        return self.cents < other.cents

    def __gt__(self, other):
        return self.cents > other.cents

    def __le__(self, other):
        return self.cents <= other.cents

    def __ge__(self, other):
        return self.cents >= other.cents

    def __eq__(self, other):
        return self.cents == other.cents

    def __add__(self, other):
        self.cents += other.cents
        return self

    def __sub__(self, other):
        self.cents -= other.cents
        return self


if __name__ == '__main__':
    a = Price()
    print(str(a))
    b = Price(None)
    print(str(b))
    c = Price('5.00')
    print(str(c))
    d = Price('5.01')
    print(str(d))
    e = Price('5.01.300')
    print(str(e))
    try:
        e.setfrom('5.0.0.1')
    except ValueError:
        pass
    try:
        f = Price(5.01)
    except ValueError:
        pass
    e.cents = 501
    print(str(e))

    # +- == math should work
    a += d
    print(str(a))
    print(a == d)
    a -= c
    print(str(c))

    a = Price('$5.02')
    print(str(a))
