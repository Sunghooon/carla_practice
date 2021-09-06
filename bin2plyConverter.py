# thanks to https://gist.github.com/HTLife/e8f1c4ff1737710e34258ef965b48344

import numpy as np
import struct
from open3d import *

size_float = 4
list_pcd = []
binFilePath = '../resource/bin/000000.bin'
plyFilePath = '../resource/ply/temp.ply'

with open(binFilePath, "rb") as f:
    byte = f.read(size_float * 4)
    idx = 0
    while byte:
        x, y, z, intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z])
        byte = f.read(size_float * 4)
        idx = idx + 1
    
with open(plyFilePath, "w") as f:
    f.write('ply\n')
    f.write('format ascii 1.0\n')
    f.write('element vertex %d\n' %idx)
    f.write('property float32 x\n')
    f.write('property float32 y\n')
    f.write('property float32 z\n')
    f.write('end_header\n')

    for i in range(len(list_pcd)):
        f.write('%4f %4f %4f\n' %(list_pcd[i][0], list_pcd[i][1], list_pcd[i][2]))


