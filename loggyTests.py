#!/usr/bin/python

import unittest,json, os
from loggy import pickMessageByIndex, getEntriesPerOS, getNumberOS, writeSyslog, writeLogMessage

class LoggyTests(unittest.TestCase):

    def testPickMessageByIndex(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        expectedResponse = ["Linux syslog test message one"]
        output = pickMessageByIndex(data, "Linux", "Lin1")
        self.assertEqual(output, expectedResponse)

    def testPickMultipleMessagesByIndex(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        indices = ["Lin1", "Lin2", "Lin1"]
        expectedResponse = ["Linux syslog test message one", "Linux syslog test message two", "Linux syslog test message one"]
        output = pickMessageByIndex(data, "Linux", indices)
        self.assertEqual(output, expectedResponse)

    def testGetEntriesPerOS(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = getEntriesPerOS(data, "Linux")
        self.assertEqual(output, 2)


    def testGetNumberOS(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = getNumberOS(data)
        self.assertEqual(output, 3)

    def testWriteSyslog(self):
        fName = "/tmp/testfile"
        expectedContents = "ZZZZZ"
        if os.path.isfile(fName):
           os.remove(fName)
        writeSyslog(expectedContents, "Blaina", fName)
        fH = open(fName)
        output = fH.readline()
        self.assertTrue(expectedContents in output)       
	
    def testWriteSyslogproc(self):
        fName = "/tmp/testfile"
        expectedContents = "ZZZZZ"
        expectedProc = "sshd[345]"
        if os.path.isfile(fName):
           os.remove(fName)
        writeSyslog(expectedContents, "Blaina", fName, procString=expectedProc)
        fH = open(fName)
        output = fH.readline()
        self.assertTrue(expectedContents in output and expectedProc in output)       

    def testWriteLogMessage(self):
        expectedContents = "Linux syslog test message one"
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        fName = "/tmp/testfile"
        if os.path.isfile(fName):
           os.remove(fName)
        writeLogMessage(data, "Lin1", "Linux", logFile=fName)
        fH = open(fName)
        output = fH.readline()
        self.assertTrue(expectedContents in output)       
           


def main():
    unittest.main()

if __name__ == '__main__':
    main()
