#!/usr/bin/env python
import sys

def argerr(x, *message):
    if len(sys.argv) == x:
       return(False)
    else:
        if len(message) > 0:
            print(message)
        return(True)
