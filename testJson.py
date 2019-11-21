# -*- coding: utf-8 -*-
__author__ = "FTest"
# import json
# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }#
# json_str = json.dumps(data,indent=4)
# print(json_str)
list_test = [{'day':1,'no':101},
             {'day':2,'no':301},
             {'day':3,'no':3},
             {'day':1,'no': 401},
             {'day':3,'no': 201}]

list_new = list(list_test)
list_new2 = list_test

print(list_new2)
print(list_new)

for match in list_test:
    if match['no'] <= 300:
        match['type'] = 'FB'
    else:
        match['type'] = 'BK'

list_new[1]['day'] = 7
list_new.pop()

print(list_test)
print(list_new)

