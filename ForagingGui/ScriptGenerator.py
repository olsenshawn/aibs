# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:34:46 2013

@author: derricw
"""

import os
import datetime

NOW = datetime.datetime.now()
HEADER = """
# *** This script has been auto-generated by """ + __file__ +  """ ***
# *** 	on """ + str(NOW) + "   ***"
IMPORTS = """
from aibs.Terrain import Terrain
from aibs.Foraging import Foraging
from psychopy import visual, core, event, logging, misc, monitors
import numpy as np

"""


class Script(object):
    def __init__(self):
        #Generate imports
        self.script = ""
        self.script += HEADER
        self.script += IMPORTS

    def add(self, *args):
    	for a in args:
            if a is not None:
    	        self.script+=a + '\n'

    def save(self, path):
    	with open(path, 'w+') as f:
    		f.write(self.script)




if __name__ == '__main__':
	s = Script()
	s.add('import scipy as sp')
	print s.script