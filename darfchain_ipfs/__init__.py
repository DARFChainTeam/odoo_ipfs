import models

import pip
try:
    import json
except ImportError:
    print('\n There was no such module named -ujson- installed')
    print('xxxxxxxxxxxxxxxx installing ujson xxxxxxxxxxxxxx')
    pip.main(['install', 'ujson'])
try:
    import base58
except ImportError:
    print('There was no such module name -base58- installed')
    pip.main(['install', 'base58'])
try:
    import web3
except ImportError:
    print('There was no such module name -base58- installed')
    pip.main(['install', 'web3'])
try:
    import xmltodict
except ImportError:
    print('Install xmltodict')
    pip.main(['install', 'xmltodict'])
