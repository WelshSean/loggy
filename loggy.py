#!/usr/bin/python

import json,sys
from pprint import pprint

def pickMessageByIndex(data, OS, Indices):
    ans = list()
    if type(Indices) is not list:
        Indices = [ Indices ]
    for Index in Indices:
        ans.append(data[OS][Index])
    return ans

def pickRandomByOS(data, OS, test = False):   ### No test yet
    from random import randint
    ri = randint(0, getEntriesPerOS(data, OS) - 1)  ### Remember array indices start from 0
    k = data[OS].keys()
    return data[OS][k[ri]]

def pickRandom(data, test = False):   ### No test yet
    from random import randint
    ri = randint(0, getNumberOS(data) - 1)
    k = data.keys()
    OS = k[ri]
    return pickRandomByOS(data, OS)

def getEntriesPerOS(data,OS):
    return len(data[OS])

def getNumberOS(data):
    return len(data.keys())


def main():
    with open('loggy.data') as data_file:    
        data = json.load(data_file)

## Example of data format
## print data["Linux"]["Lin1"]


    if  sys.argv[1] == "pickOne":
        print pickMessage(data, sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "pickOSRan":
        print pickRandomByOS(data, sys.argv[2])
    elif sys.argv[1] == "pickRan":
        print pickRandom(data)


if __name__ == '__main__':
    main()


