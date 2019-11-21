# -*- coding: utf-8 -*-
__author__ = "FTest"

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data,indent=4)

print(json_str)