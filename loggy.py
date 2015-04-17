#!/usr/bin/python

import json,sys
from pprint import pprint

def pickMessageByIndex(data, OS, Index):
    return data[OS][Index]

def pickRandomByOS(data, OS, test = False):
    from random import randint
    ri = randint(0, getEntriesPerOS(data, OS) -1)  ### Remember array indices start from 0
    k = data[OS].keys()
    print "k", k
    print "ri", ri
    print "OS", OS
    return data[OS][k[ri]]

def getEntriesPerOS(data,OS):
    return len(data[OS])


def main():
    with open('loggy.data') as data_file:    
        data = json.load(data_file)

## Example of data format
## print data["Linux"]["Lin1"]


    if  sys.argv[1] == "pickOne":
        print pickMessage(data, sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "pickRan":
        print pickRandomByOS(data, sys.argv[2])


if __name__ == '__main__':
    main()


