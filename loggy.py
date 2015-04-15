#!/usr/bin/python

import json,sys
from pprint import pprint

def pickMessage(data, OS, Index):
    print data[OS][Index]

with open('loggy.data') as data_file:    
    data = json.load(data_file)

## Example of data format
## print data["Linux"]["Lin1"]


if  sys.argv[1] == "Random":
    pickMessage(data, sys.argv[2], sys.argv[3])


