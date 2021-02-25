#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

from scapy.all import *
# ls() 查看信息
eth = EtherDA()
eth.dst = "22:22:22:22:22:22"
eth.src = "11:11:11:11:11:11"
eth.type = 0x0800
eth._show()
sendp(eth)


















