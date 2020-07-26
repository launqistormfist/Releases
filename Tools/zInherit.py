import binascii
import re
import struct
import math
import os
import copy
import operator

def find_sublist(sub, bigger):
    if not bigger:
        return -1
    if not sub:
        return 0
    first, rest = sub[0], sub[1:]
    pos = 0
    try:
        while True:
            pos = bigger.index(first, pos) + 1
            if not rest or bigger[pos:pos+len(rest)] == rest:
                return pos
    except ValueError:
        return -1


HeilosGUID = [
[85, 156, 192, 172, 116, 33, 26, 66, 161, 251, 184, 251, 13, 78, 174, 168],
[124, 92, 249, 29, 52, 46, 15, 76, 187, 186, 72, 81, 128, 184, 2, 14],
[219, 94, 161, 177, 199, 212, 165, 74, 131, 145, 221, 227, 202, 63, 18, 105],
[109, 203, 34, 249, 28, 168, 144, 76, 174, 152, 99, 191, 75, 251, 40, 92],
[149, 218, 185, 54, 11, 167, 128, 70, 168, 180, 45, 237, 236, 113, 206, 199],
[155, 122, 163, 205, 43, 200, 97, 69, 150, 236, 25, 126, 83, 229, 92, 200],
[24, 131, 61, 53, 50, 247, 200, 76, 157, 58, 240, 84, 22, 102, 82, 174],
[195, 241, 250, 220, 30, 143, 162, 68, 164, 172, 124, 12, 119, 16, 255, 110],
[59, 26, 236, 131, 29, 189, 23, 73, 140, 183, 183, 30, 205, 2, 71, 119],
[80, 115, 172, 32, 244, 216, 221, 72, 136, 250, 66, 94, 82, 24, 214, 94],
[194, 190, 49, 217, 213, 107, 201, 78, 164, 252, 105, 209, 218, 139, 82, 217],
[93, 32, 31, 45, 64, 202, 180, 70, 140, 133, 221, 141, 133, 217, 139, 214],
[97, 100, 191, 188, 187, 201, 155, 79, 190, 195, 117, 54, 133, 30, 33, 35],
[32, 117, 78, 83, 21, 228, 63, 64, 162, 146, 201, 202, 7, 211, 8, 50],
[179, 168, 197, 133, 122, 117, 194, 70, 144, 228, 92, 15, 129, 249, 37, 83],
[192, 233, 64, 163, 100, 106, 88, 75, 158, 141, 90, 102, 62, 108, 38, 63],
[156, 1, 23, 156, 241, 100, 43, 79, 172, 112, 104, 179, 169, 207, 93, 35]
]

MaxGUID = [
[141, 115, 134, 36, 113, 125, 67, 68, 130, 158, 11, 38, 5, 88, 205, 202],
[167, 53, 95, 27, 242, 141, 75, 69, 133, 124, 138, 13, 13, 96, 134, 82],
[34, 167, 12, 97, 120, 255, 137, 70, 172, 150, 103, 135, 227, 96, 96, 27],
[199, 238, 254, 130, 36, 161, 217, 75, 161, 97, 193, 179, 22, 1, 253, 27],
[249, 212, 54, 6, 62, 19, 186, 76, 133, 240, 173, 177, 77, 149, 5, 206],
[118, 145, 28, 8, 157, 195, 91, 64, 188, 63, 254, 248, 28, 211, 92, 151],
[223, 102, 242, 58, 141, 69, 234, 64, 139, 109, 9, 89, 124, 178, 3, 183],
[178, 28, 18, 120, 112, 16, 130, 79, 175, 189, 112, 182, 164, 99, 180, 52],
[201, 4, 1, 157, 72, 245, 79, 68, 189, 89, 128, 234, 88, 139, 96, 248],
[88, 254, 52, 200, 241, 45, 193, 71, 131, 190, 221, 219, 126, 254, 144, 171],
[89, 39, 154, 117, 77, 119, 39, 77, 169, 15, 91, 66, 25, 88, 56, 132],
[72, 228, 211, 168, 233, 70, 58, 79, 189, 140, 225, 117, 48, 54, 108, 98],
[1, 189, 181, 21, 54, 137, 30, 68, 143, 217, 167, 115, 190, 2, 8, 185],
[244, 75, 245, 17, 184, 223, 41, 69, 188, 175, 141, 202, 53, 105, 149, 56],
[222, 227, 135, 228, 143, 131, 143, 79, 143, 44, 109, 62, 132, 53, 132, 199],
[138, 212, 92, 142, 38, 163, 252, 73, 151, 151, 70, 15, 22, 245, 24, 140],
[140, 49, 18, 17, 157, 193, 169, 76, 175, 54, 171, 27, 94, 167, 226, 21]
]

for subdir, dirs, files in os.walk("G:\Modding Stuff\Hydro Stuff\Hydro Shortcuts\Mining\Content"):
	for file in files:
		if file.endswith(".uexp"):
			reading = open(os.path.join(subdir, file), 'rb')
			content = list(reading.read())
			for x in range (0, len(HeilosGUID)):
				GUIDGRAB = find_sublist(HeilosGUID[x], content)
				if GUIDGRAB > -1:
					rawr = 0
					for y in range (GUIDGRAB, GUIDGRAB+16):
						content[y-1] = MaxGUID[x][rawr]
						rawr = rawr+1
					print(file)
					reading.close()
					reading = open(os.path.join(subdir, file), 'wb')
					reading.write(bytearray(content))
			reading.close()