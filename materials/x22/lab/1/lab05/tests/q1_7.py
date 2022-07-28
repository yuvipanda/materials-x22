test = {   'name': 'q1_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> # Make sure you are using the date range 1970-2020\n>>> post_1969_fertility_and_child_mortality.num_rows\n51', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Check your column labels and spelling\n'
                                               ">>> all([label in post_1969_fertility_and_child_mortality.labels for label in ['Children per woman', 'Child deaths per 1000 born']])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(1).item(0), 223.13)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(1).item(-1), 27.7)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(0).item(-1), 2.0)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(0).item(0), 6.95)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(1).mean(), 121.15352941176468)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> facm = post_1969_fertility_and_child_mortality.select('Children per woman', 'Child deaths per 1000 born')\n"
                                               '>>> np.allclose(facm.column(0).mean(), 4.166274509803921)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
