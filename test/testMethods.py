#!/usr/bin/python2.7

import os
import os.path
import unittest
import sys, traceback

sys.path.insert(0, '../app')

from ui import UI

ui = UI()

class BaseTest(unittest.TestCase):
    def test(self):
        katoolin.constants
