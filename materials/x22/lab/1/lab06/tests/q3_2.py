test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # Check your column labels and spelling\n>>> recent.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Careful, the population of Australia in 2010 was 22,162,863\n>>> recent.where('geo', 'aus').column(2).item(0) == 22162863\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The number of people estimated to be living in extreme poverty\n'
                                               ">>> # in Australia should be 301,415. That's 22,162,863 * 0.0136\n"
                                               '>>> # rounded to the nearest integer.\n'
                                               ">>> float(recent.where('geo', 'aus').column(3).item(0)) == 301415.0\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> sum(recent.column(3)) == 990911651.0\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
