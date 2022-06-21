test = {   'name': 'q32',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(imdb) == tables.Table\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> imdb.num_rows == 250\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> imdb.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(2,5))\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
