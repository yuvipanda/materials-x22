test = {   'name': 'q211',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Hint 1: To understand how this question works, first set\n'
                                               ">>> #   you = 'fi'\n"
                                               '>>> # and add the line\n'
                                               ">>> #   print('beeper'.replace('p', you))\n"
                                               '>>> # and you should see the word "beefier" appear as the first output.\n'
                                               '>>> #\n'
                                               '>>> # Hint 2: Just by changing you, you can create a word with two\n'
                                               '>>> # double letters in a row: beekeeper\n'
                                               '>>> type(you) == str\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # You can make the word beekeeper by assigning\n>>> #   you = 'keep'\n>>> 'beeper'.replace('p', you)[::-1]\n'repeekeeb'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The word you\'re trying to make is "bookkeeper"!\n'
                                               '>>> #\n'
                                               '>>> # To change "beekeeper" to "bookkeeper", change the "bee" to "book".\n'
                                               ">>> #   this = 'book'\n"
                                               ">>> 'beeper'.replace('p', you).replace('bee', this)[::-1]\n"
                                               "'repeekkoob'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
