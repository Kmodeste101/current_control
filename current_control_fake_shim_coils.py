#!/usr/bin/python3

import numpy as np
import time
import matplotlib.pyplot as plt

#using global variables: x,y,z for each sensor position.
sensor_xyz = np.float64((
    (-0.25, -0.25, -0.25),
    (-0.25, -0.25, 0),
    (-0.25, -0.25, 0.25),
    (-0.25, 0, -0.25),
    (-0.25, 0, 0),
    (-0.25, 0, 0.25),
    (-0.25, 0.25, -0.25),
    (-0.25, 0.25, 0),
    (-0.25, 0.25, 0.25),
    (0, -0.25, -0.25),
    (0, -0.25, 0),
    (0, -0.25, 0.25),
    (0, 0, -0.25),
    (0, 0, 0),
    (0, 0, 0.25),
    (0, 0.25, -0.25),
    (0, 0.25, 0),
    (0, 0.25, 0.25),
    (0.25, -0.25, -0.25),
    (0.25, -0.25, 0),
    (0.25, -0.25, 0.25),
    (0.25, 0, -0.25),
    (0.25, 0, 0),
    (0.25, 0, 0.25),
    (0.25, 0.25, -0.25),
    (0.25, 0.25, 0),
    (0.25, 0.25, 0.25)))
print('sensors',sensor_xyz)

'''
import os
import sys
import zipfile

archive = sys.argv[1] # assuming launched with `python my_script.py archive.zip`

try:
    with zipfile.ZipFile(archive) as z:    
        for filename in z.namelist():
            if not os.path.isdir(filename):
                print(f'\nFile "{filename}":')
                # read the file
                for line in z.open(filename):
                    print(line.decode('utf-8'))
            else:
                print(f'\nDirectory "{filename}"')
except zipfile.BadZipFile:
    print(f'Bad zip file: "{archive}"')
except IsADirectoryError:
    print(f'Directory, not file: "{archive}"')
except FileNotFoundError:
    print(f'File not found: "{archive}"')
'''
'''
import csv
from io import TextIOWrapper
from zipfile import ZipFile

with ZipFile('OPERA_shim.zip') as zf:
    with zf.open('coilnum00.txt', 'r') as infile:
        reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
        for row in reader:
            # process the CSV here
            print(row)
'''
import os
import zipfile

with zipfile.ZipFile('OPERA_shim.zip') as z:
    for filename in z.namelist():
        if not os.path.isdir(filename):
            # read the file
            with z.open(filename) as f:
                for line in f:
                    if line.strip():  # Skip empty lines
                        print (line)
