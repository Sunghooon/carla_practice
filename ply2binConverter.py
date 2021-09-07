import numpy as np
import struct
from open3d import *

plyFilePath = '../resource/ply/00043509.ply'
binFilePath = '../resource/bin/00043509.bin'
tempPath = '../resource/bin/000000.bin'

list_pcd = []
intensity = 0.2
with open(plyFilePath, "r") as f:

    for line in f:
        if "end_header" in line:
            print(line)
            break

    for line in f:
        val = f.readline()
        val = val.split()
        x, y, z = val
        list_pcd.append([x, y, z, intensity])

with open(binFilePath, "wb") as f:
    idx = 0
    for i in range(len(list_pcd)):
        temp = list_pcd[i]
        temp = np.array(temp)
        x = float(temp[0])
        y = float(temp[1])
        z = float(temp[2])
        r = float(temp[3])
        #b_data = bytes(temp)
        #print(temp)
        b_data = struct.pack("ffff", x, y, z, r)
        #print(b_data)
        #print(type(b_data))
        f.write(b_data)
        
        
    

size_float = 4
with open(binFilePath, "rb") as f:
    byte = f.read(size_float * 4)

    while byte:
        x, y, z, intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z])
        byte = f.read(size_float * 4)
    
    #print(list_pcd)
