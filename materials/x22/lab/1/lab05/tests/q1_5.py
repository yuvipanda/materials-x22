test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # Check your column labels and spelling\n>>> fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the start year to determine the data range.\n'
                                               ">>> all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2021))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the start year to determine the data range.\n'
                                               ">>> all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2021))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(fertility_over_time('bgd', 2012))\n"
                                               'Year | Children per woman\n'
                                               '2012 | 2.21\n'
                                               '2013 | 2.18\n'
                                               '2014 | 2.16\n'
                                               '2015 | 2.13\n'
                                               '2016 | 2.1\n'
                                               '2017 | 2.08\n'
                                               '2018 | 2.05\n'
                                               '2019 | 2.02\n'
                                               '2020 | 2\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(fertility_over_time('usa', 2015))\nYear | Children per woman\n2015 | 1.93\n2016 | 1.92\n2017 | 1.91\n2018 | 1.9\n2019 | 1.9\n2020 | 1.89\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print(fertility_over_time('hti', 2015))\nYear | Children per woman\n2015 | 2.97\n2016 | 2.92\n2017 | 2.87\n2018 | 2.82\n2019 | 2.77\n2020 | 2.73\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
