test = {   'name': 'q52',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Use .select("Row Labels", "1970", "2009") to select the columns.\n>>> top_1970_with_2009.labels == ("Row Labels", "1970", "2009")\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Use .sort("1970", descending=True) to sort in descreasing order.\n'
                                               '>>> print(top_1970_with_2009.take(0))\n'
                                               'Row Labels    | 1970 | 2009\n'
                                               'United States | 11   | 13.7\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
