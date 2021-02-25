#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2020/1/3 下午10:37
# ide： PyCharm

import zlib
import struct

filename = 'flag.png'
with open(filename, 'rb') as f:
    all_b = f.read()
    data_f = all_b[:12]
    # data = all_b[12:29]
    # print(data)
    data_r = all_b[29:]
    data_idch = all_b[12:17]
    data_l = all_b[25:29]
    # width = all_b[17:21]
    # height = all_b[21:25]
    # print(width, height)
    crc32key = int(all_b[29:33].hex(), 16)
    data = ''
    for w in range(184570, 184577):
        for h in range(22790, 22793):
            width = struct.pack('>i', w)
            height = struct.pack('>i', h)
            data = data_idch + width + height + data_l
            print(data)
            # print(len(data))
            if zlib.crc32(data) == crc32key:
                print(w, h)
                with open('r.png', 'wb') as f1:
                    f1.write(data_f + data + data_r)
                    break
