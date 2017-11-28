'''
This code will write mcnp input files for shields of different materials while varying lengths

User desired parameters can be altered near the bottom of the code.
'''

import numpy as np
import subprocess
import os


#numbering
#  0 Void
#  1 Air      2 Borated Polyethylene
#  3 Aluminum 4 Lead
#  5 Tungsten 6 Cadmium
#  n neutron  p photon

density = [0.0, 1.000, 11.34, 19.3,]
label = ['VOID', 'Borated Polyethylene', 'Lead', 'Tungsten']
abrev = ['VOID', 'bp', 'pb', 'w']


def createInputs(name):
    length = 30
    H  = 'c  *********************************************************\n'
    H += 'c                           BLOCK 1\n'
    H += 'c  *********************************************************\n'
    H += '11 0 11 -12     -21            $ NEBP Cavity\n'
    H += '12 1 -1.0       11 -12  21 -22            $ Borated Poly Collimator\n'
    H += '13 4 -2.699     11 -12  22 -23            $ NEBP Aluminum Case\n'
    H += 'c \n'
    H += '200 {} -{} 120 -121 122 -123 12 -131 \n'.format(name[0], density[int(name[0])])
    H += '201 {} -{} 120 -121 122 -123 131 -132 \n'.format(name[1], density[int(name[1])])
    H += '202 {} -{} 120 -121 122 -123 132 -133 \n'.format(name[2], density[int(name[2])])
    H += '203 {} -{} 120 -121 122 -123 133 -134 \n'.format(name[3], density[int(name[3])])
    H += '204 {} -{} 120 -121 122 -123 134 -135 \n'.format(name[4], density[int(name[4])])
    H += '205 {} -{} 120 -121 122 -123 135 -136 \n'.format(name[5], density[int(name[5])])
    H += '206 {} -{} 120 -121 122 -123 136 -137 \n'.format(name[6], density[int(name[6])])
    H += '207 {} -{} 120 -121 122 -123 137 -138 \n'.format(name[7], density[int(name[7])])
    H += '208 {} -{} 120 -121 122 -123 138 -139 \n'.format(name[8], density[int(name[8])])
    H += '209 {} -{} 120 -121 122 -123 139 -140 \n'.format(name[9], density[int(name[9])])
    H += 'c \n'
    H += '31 0  41 -32     -21        $ Detector Cell\n'
    H += 'c Define Problem space cell\n'
    H += '90 0 -32 #11 #12 #13 (-12:-120:121:-122:123:140) #31\n'
    H += '99 0            32                        $ Graveyard (RIP IN PEACE)\n'
    H += '\n'
    H += 'c  *********************************************************\n'
    H += 'c                           BLOCK 2\n'
    H += 'c  *********************************************************\n'
    H += 'c  _____Problem Planes\n'
    H += '11  PX  -36.015          $ Collimator Front Plane\n'
    H += '12  PX   0               $ Collimator Back Plane\n'
    H += 'c  _____Cylinders\n'
    H += '21  CX   1.27            $ Cavity Cylinder\n'
    H += '22  CX   7.62            $ Borated Poly Cylinder\n'
    H += '23  CX   8.255           $ Aluminum Case Cylinder\n'
    H += 'c  _____Rectangular Parallelepiped\n'
    H += '120 PZ -10\n'
    H += '121 PZ 10\n'
    H += '122 PY -10\n'
    H += '123 PY 10\n'
    for i in range(10):
        H += '{} PX {} \n'.format(131 + i, (length * 0.1) * (i + 1) + .0001) 
    H += '32  RPP    -40 101             -11   11      -11  11    $ Problem Space\n'
    H += 'c  _____Detector Planes\n'
    H += '41 PX {}\n'.format(length + .0002)
    H += '\n'
    H += 'c  *********************************************************\n'
    H += 'c                           BLOCK 3\n'
    H += 'c  *********************************************************\n'
    H += open('nsource.txt', 'r').read()
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                   PROBLEM SPECIFICATIONS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'NPS 100000\n'
    H += 'PRINT 110\n'
    H += 'MODE n p\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                        IMPORTANCES\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'IMP:n 1 14r 0\n'
    H += 'IMP:p 1 14r 0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                      MATERIAL CARDS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 1:      BORATED POLYETHYLENE\n'
    H += 'c  ---------------------------(density 1.000 g/cm^3)--------\n'
    H += 'M1     1001     -0.125355\n'
    H += '       5010.70c -0.100000\n'
    H += '       6000     -0.774645\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 2:      LEAD  \n'
    H += 'c  ---------------------------(density 11.34 g/cm^3)--------\n'
    H += 'M2   82207.70c   -1.0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 3:      TUNGSTEN   \n'
    H += 'c  ---------------------------(density 19.3 g/cm^3)---------\n'
    H += 'M3   074184   -1.0\n'
    H += 'M4    13027.70c -1.0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                       TALLY CARDS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'F11:n 41\n'
    H += 'FS11  21\n'
    H += 'E11   0.0 0.5 20\n'
    H += 'F21:p 41\n'
    H += 'FS21  21\n'
    H += 'E21   0.0 0.1 20\n'
    H += '\n'
    with open('{}n.i'.format(name), 'w') as F:
            F.write(H)
    
    H  = 'c  *********************************************************\n'
    H += 'c                           BLOCK 1\n'
    H += 'c  *********************************************************\n'
    H += '11 0  11 -12     -21            $ NEBP Cavity\n'
    H += '12 1 -1.0       11 -12  21 -22            $ Borated Poly Collimator\n'
    H += '13 4 -2.699     11 -12  22 -23            $ NEBP Aluminum Case\n'
    H += 'c \n'
    H += '200 {} -{} 120 -121 122 -123 12 -131 \n'.format(name[0], density[int(name[0])])
    H += '201 {} -{} 120 -121 122 -123 131 -132 \n'.format(name[1], density[int(name[1])])
    H += '202 {} -{} 120 -121 122 -123 132 -133 \n'.format(name[2], density[int(name[2])])
    H += '203 {} -{} 120 -121 122 -123 133 -134 \n'.format(name[3], density[int(name[3])])
    H += '204 {} -{} 120 -121 122 -123 134 -135 \n'.format(name[4], density[int(name[4])])
    H += '205 {} -{} 120 -121 122 -123 135 -136 \n'.format(name[5], density[int(name[5])])
    H += '206 {} -{} 120 -121 122 -123 136 -137 \n'.format(name[6], density[int(name[6])])
    H += '207 {} -{} 120 -121 122 -123 137 -138 \n'.format(name[7], density[int(name[7])])
    H += '208 {} -{} 120 -121 122 -123 138 -139 \n'.format(name[8], density[int(name[8])])
    H += '209 {} -{} 120 -121 122 -123 139 -140 \n'.format(name[9], density[int(name[9])])
    H += 'c \n'
    H += '31 0  41 -32     -21        $ Detector Cell\n'
    H += 'c Define Problem space cell\n'
    H += '90 0 -32 #11 #12 #13 (-12:-120:121:-122:123:140) #31\n'
    H += '99 0            32                        $ Graveyard (RIP IN PEACE)\n'
    H += '\n'
    H += 'c  *********************************************************\n'
    H += 'c                           BLOCK 2\n'
    H += 'c  *********************************************************\n'
    H += 'c  _____Problem Planes\n'
    H += '11  PX  -36.015          $ Collimator Front Plane\n'
    H += '12  PX   0               $ Collimator Back Plane\n'
    H += 'c  _____Cylinders\n'
    H += '21  CX   1.27            $ Cavity Cylinder\n'
    H += '22  CX   7.62            $ Borated Poly Cylinder\n'
    H += '23  CX   8.255           $ Aluminum Case Cylinder\n'
    H += 'c  _____Rectangular Parallelepiped\n'
    H += '120 PZ -10\n'
    H += '121 PZ 10\n'
    H += '122 PY -10\n'
    H += '123 PY 10\n'
    for i in range(10):
        H += '{} PX {} \n'.format(131 + i, (length * 0.1) * (i + 1) + .0001) 
    H += '32  RPP    -40 101             -11   11      -11  11    $ Problem Space\n'
    H += 'c  _____Detector Planes\n'
    H += '41 PX {}\n'.format(length + .0002)
    H += '\n'
    H += 'c  *********************************************************\n'
    H += 'c                           BLOCK 3\n'
    H += 'c  *********************************************************\n'
    H += open('psource.txt', 'r').read()
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                   PROBLEM SPECIFICATIONS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'NPS 100000\n'
    H += 'PRINT 110\n'
    H += 'MODE p\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                        IMPORTANCES\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'IMP:p 1 14r 0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                      MATERIAL CARDS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 1:      BORATED POLYETHYLENE\n'
    H += 'c  ---------------------------(density 1.000 g/cm^3)--------\n'
    H += 'M1     1001     -0.125355\n'
    H += '       5010.70c -0.100000\n'
    H += '       6000     -0.774645\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 2:      LEAD  \n'
    H += 'c  ---------------------------(density 11.34 g/cm^3)--------\n'
    H += 'M2   82207.70c   -1.0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c  MATERIAL 3:      TUNGSTEN   \n'
    H += 'c  ---------------------------(density 19.3 g/cm^3)---------\n'
    H += 'M3   074184   -1.0\n'
    H += 'M4    13027.70c -1.0\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'c                       TALLY CARDS\n'
    H += 'c  ---------------------------------------------------------\n'
    H += 'F21:p 41\n'
    H += 'FS21  21\n'
    H += 'E21   0.0 0.1 20\n'
    H += '\n'
    with open('{}p.i'.format(name), 'w') as F:
            F.write(H)
            
    
    H = open('template.qsub', 'r').read()
    H += 'mcnp6 i={}n.i ru={}n.ru o={}n.o\n'.format(name, name, name)
    with open('{}n.qsub'.format(name), 'w') as F:
            F.write(H)
    
    H = open('template.qsub', 'r').read()
    H += 'mcnp6 i={}p.i ru={}p.ru o={}p.o\n'.format(name, name, name)
    with open('{}p.qsub'.format(name), 'w') as F:
            F.write(H)





protected_files = ['filter_functions.py', 'filter_functions.pyc', 'filter_writer.py', 'nsource.txt', 'psource.txt', 'template.qsub', 'filter_data.txt']
def remove():
    files = os.listdir('/home/mjcb/filter')
    for name in files:
        if name not in protected_files:
            try:
                os.remove(name)
            except OSError:
                pass
    

def readGamma(name):
    try:
        f = open('{}p.o'.format(name)).readlines()
        for i, line in enumerate(f):
            if '1tally       21' in line:
                nFastG = float(f[i+17].split()[1])
                totalGamma = float(f[i+18].split()[1])
        return nFastG, totalGamma
    except OSError:
        return 0.000

def readNeutron(name):
    try:
        f = open('{}n.o'.format(name)).readlines()
        for i, line in enumerate(f):
            if '1tally       11' in line:
                nFastN = float(f[i+17].split()[1])
                totalNeutrons = float(f[i+18].split()[1])
            if '1tally       21' in line:
                nFastG = float(f[i+17].split()[1])
                totalGamma = float(f[i+18].split()[1])
        return nFastN, totalNeutrons, nFastG, totalGamma
    except OSError:
        return 0.000
    
