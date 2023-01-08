from __future__ import with_statement
import os
from os.path import isfile
import numpy as np


MAX_SIZE = 512
SHAPE_SIDE = 7
dict = {  '-' : -1,  '#' : 1 }


def read(dir):
    shapes_files = []
    for filename in os.listdir(dir):
        path = os.path.join(dir, filename)
        if isfile(path):
            shapes_files.append(path)
                
    shapes = []
    for path in shapes_files:
            shape = read_shape(path)
            shapes.append(np.array(shape))
    return shapes


def read_shape(path):
    with open(path) as f:
        contents = f.read(MAX_SIZE)
        contents = str.replace(contents, "\n", "")
        contents = str.replace(contents, "\r", "")

        shape = []
        for c in contents:
            shape.append(dict[c])
        if len(shape) != pow(SHAPE_SIDE,2):
            print("Shape size must be", SHAPE_SIDE, "x", SHAPE_SIDE)
        return shape
