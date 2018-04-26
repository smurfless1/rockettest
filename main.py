from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion

import sys

from cart import Cart
from catalog import Catalog
from rule import AppleBulkRule, HappyHorse, ChaiAndMilk, BOGOCoffeeRule

class CodeValidator(Validator):
    def validate(self, document):
        text = document.text

        if text:
            for word in text.split(' '):
                if len(word) < 1:
                    continue
                cleaned = word.strip(',')
                if not cleaned in Catalog.keys():
                    raise ValidationError(message='No, really, please only pick from the product codes.')

class CodeSuggestion(AutoSuggest):
    def get_suggestion(self, cli, buffer, document):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        for code in Catalog.keys():
            if word_before_cursor in code:
                subcode = code[:-len(word_before_cursor)]
                return Suggestion(subcode)

html_completer = WordCompleter(Catalog.keys())

print(u"===============================================================================")
print(u"General notes: Tab completion works, and type exit to return cleanly.")
print(u"You can use commas between codes if you like, but at least a space is required.")
print(u"The code 'clear' will empty your cart.")
print(u"Including the code 'exit' will stop after the next cart list.")
print(u"===============================================================================")

ptext = u'Basket: '

# todo 'clear' command?
cart = Cart()
cart._rules.append(AppleBulkRule())
cart._rules.append(BOGOCoffeeRule())
cart._rules.append(ChaiAndMilk())
cart._rules.append(HappyHorse())

exit = False
try:
    while not exit:
        codes = prompt(ptext, validator=CodeValidator(), completer=html_completer, auto_suggest=CodeSuggestion())
        if 'exit' in codes:
            exit = True
            codes = codes.replace('exit', '')
        elif 'clear' in codes:
            cart = Cart()
            cart._rules.append(AppleBulkRule())
            cart._rules.append(BOGOCoffeeRule())
            cart._rules.append(ChaiAndMilk())
            cart._rules.append(HappyHorse())
            continue
        cart.set_from(codes)
        print str(cart)
        print('')
        print('')
except KeyboardInterrupt:
    pass
