#!/usr/bin/python
# encoding: utf-8

'''
In all examples of addresses I've found, the number is just before or after
the street name, so this application search for a match to the number at the
beginning or end of the string.
'''

import re


def trim_spaces(addressList):
    return [x.strip().strip(',') for x in addressList]


def separate_address(address):

    # Searching for the number at the beginning of the string
    number = re.search(r'^([Nn]\D?\D?\s?)?(\D?\d\d*\s?\D?\s)', address)
    if number:
        separated = [re.sub(number.group(), "", address), number.group(2)]
        # I've chosen to take group(2) to keep only the number, without any
        # abreviation like "No" or "N."
    else:
        # Searching for the number at the end of the string
        number = re.search(r'(\s[Nn]\D?\D?\s?)?(\w?\d\d*\s?\w?)$', address)
        separated = [re.sub(number.group(), "", address), number.group(2)]
    return trim_spaces(separated)


def main():

    given_examples = [
        u'Winterallee 3',
        u'Musterstrasse 45',
        u'Blaufeldweg 123B',
        u'Am Bächle 23',
        u'Auf der Vogelwiese 23 b',
        u'4, rue de la revolution',
        u'200 Broadway Av',
        u'Calle Aduana, 29',
        u'Calle 39 No 1540']

    other_examples = [
        u'Rua dos Lagos 125',
        u'250 2nd Av',
        u'Av Consolação, 314',
        u'Via Gustavo Baz No. 166',
        u'27 Rue Pasteur',
        u'55 Chin Shan South Road Sec. 2',
        u'221B Baker Street',
        u'A19 Calle Amapola',
        u'3rd Street, 21']

    print '\nTesting the given examples:\n'
    for x in given_examples:
        print ("%s -> { \"%s\", \"%s\" }" %
               (x, separate_address(x)[0], separate_address(x)[1]))

    print '\nTesting more examples:\n'
    for x in other_examples:
        print ("%s -> { \"%s\", \"%s\" }" %
               (x, separate_address(x)[0], separate_address(x)[1]))


if __name__ == '__main__':
    main()
