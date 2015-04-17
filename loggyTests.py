#!/usr/bin/python

import unittest,json
from loggy import pickMessageByIndex

class LoggyTests(unittest.TestCase):

    def testPickMessageByIndex(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = pickMessageByIndex(data, "Linux", "Lin1")
        self.assertEqual(output, "Linux syslog test message one")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
