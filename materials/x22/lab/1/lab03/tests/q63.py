test = {   'name': 'q63',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> sorted(farmers_markets_locations.labels) == ['MarketName', 'State', 'city', 'x', 'y']\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> farmers_markets_locations.num_rows == 8546\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> farmers_markets_locations.sort(0).take(range(3))\n'
                                               'MarketName                                       | city      | State    | x        | y\n'
                                               ' Caledonia Farmers Market Association - Danville | Danville  | Vermont  | -72.1403 | 44.411\n'
                                               " Stearns Homestead Farmers' Market               | Parma     | Ohio     | -81.7286 | 41.3751\n"
                                               '100 Mile Market                                  | Kalamazoo | Michigan | -85.5749 | 42.296',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
