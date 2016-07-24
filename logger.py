"""
How to use:
- put @logger before a function created
Example:

!====Another .py====!
from logger import logger

@logger
def foo(a,b,c):
    return a,b,c

foo("aadvark", "bear", "claw")
!===================!
"""

import time

def logger(fxn):
    def testing(*arg):
        t = time.time()
        print "\n!=====Testing function: " + fxn.func_name + "=====!"
        print fxn.func_name + str(arg)
        print "Returns: ",
        print fxn(*arg)
        print 'Execution time: ' + str(time.time() - t) + ' seconds'
        print "!" + ("=" * 23) + ("=" * (len(fxn.func_name) + 5)) + "!\n"
    return testing
