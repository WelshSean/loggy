#!/usr/bin/python

import json,sys
from pprint import pprint

def pickMessageByIndex(data, OS, Index):
    return data[OS][Index]

def main():
    with open('loggy.data') as data_file:    
        data = json.load(data_file)

## Example of data format
## print data["Linux"]["Lin1"]


    if  sys.argv[1] == "pickOne":
        pickMessage(data, sys.argv[2], sys.argv[3])



if __name__ == '__main__':
    main()


