test = {   'name': 'q41',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(above_eight) == tables.Table\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> above_eight.num_rows == 20\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure your columns are in the right order!\n'
                                               ">>> # First column should be 'Title', second column should be 'Rating'\n"
                                               '>>> print(above_eight.sort(0).take([17]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
