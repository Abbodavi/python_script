# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:41:40 2020

@author: david
"""

import sys, getopt, os
import numpy as np

def get_file(argv):
    try:
        opts, args = getopt.getopt(argv, 't:s:o:', ['train=','test=','output='])
        for opt, arg in opts:
            if opt in ("-t","--train"):
                train=arg
            elif opt in ("-s", "--secondary"):
                test=arg
            elif opt in ("-o", "--output"):
                output_file=arg
    except getopt.GetoptError:
        print("Invalid argument")
        sys.exit(2)
    return train, test, output_file



if __name__=="__main__":
    train, test, result = get_file(sys.argv[1:])
    