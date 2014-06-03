'''
Created on 19 kwi 2014

@author: tpalys
'''

import sys
from src.compiler.Compiler import Compiler

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "file.in"
        file = open(filename, "r")
        compiler = Compiler()
        text = file.read()
        scene = compiler.compile(text)

        print str(scene)
#TODO

    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)