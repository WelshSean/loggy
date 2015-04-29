#!/usr/bin/python

import json,sys, time
from pprint import pprint

#OS:index:PID:hostname
def sequenceRun(data, seqFile, outFile):
    lines = [line.strip() for line in open(seqFile)]
    for line in lines:
        if line.startswith('#'):
            continue
        args = line.split(':')
        writeLogMessage(data, args[1], OS=args[0], hostName=args[3], logFile=outFile, pid=args[2]  )       

def writeLogMessage(data, index, OS="Linux", hostName="testhost", logFile="/var/tmp/teslog", pid="9999"):
    info = pickMessageByIndex(data, OS, index)
    procString=info["proc"]+"["+pid+"]"
    writeSyslog(info["message"], hostName, logFile, procString)

def writeSyslog(message, host, filename, procString):
    try:
        fh = open(filename, "a")
    except:
        print "Cant Open File"
    else:
        try:
            fh.write(time.strftime("%b %d  %H:%M:%S") + " " + host + " " + procString +" " + message +"\n")
        finally: fh.close()

def pickMessageByIndex(data, OS, Index):
    return data[OS][Index]

def pickRandomByOS(data, OS, test = False):   ### No test yet
    from random import randint
    ri = randint(0, getEntriesPerOS(data, OS) - 1)  ### Remember array indices start from 0
    k = data[OS].keys()
    return pickMessageByIndex(data, OS, k[ri]) 

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
    elif sys.argv[1] == "wlm":
        writeLogMessage(data, sys.argv[2])
    elif sys.argv[1] == "seq":
        sequenceRun(data, "test.lsq", outFile="/tmp/sean")


if __name__ == '__main__':
    main()


