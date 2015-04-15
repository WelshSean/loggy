#!/usr/bin/python

import unittest,json
from loggy import pickMessage

class FooTests(unittest.TestCase):

    def testPickOne(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = pickMessage(data, "Linux", "Lin1")
        self.assertEqual(output, "Linux syslog test message one")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
