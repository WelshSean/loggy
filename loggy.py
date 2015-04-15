#!/usr/bin/python

import json
from pprint import pprint

with open('loggy.data') as data_file:    
    data = json.load(data_file)

print data["Linux"]
