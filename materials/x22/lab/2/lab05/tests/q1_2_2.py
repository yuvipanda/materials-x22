test = {   'name': 'q1_2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> phoenix.num_rows == 46021\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(phoenix.labels) == 6\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> phoenix.labels == ('Date', 'tmax', 'tmin', 'prcp', 'Year', 'Month')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> phoenix.group("Year").column(1).item(0) == 366\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> phoenix.group("Year").column(1).item(110) == 365\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> list(phoenix.group('Month').row(1)) == ['02 (Feb)', 3559]\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
