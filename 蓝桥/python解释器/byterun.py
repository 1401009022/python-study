#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

import collections
import operator
import dis
import sys
import types
import inspect



class VirtualMachineError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self):
        # 调用栈
        self.frames = []
        # 当前运行的帧
        self.frame = None
        # frame 返回时的返回值
        self.return_value = None
        self.last_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        """
        运行 Python 程序的入口，程序编译后生成 code_obj
        这里 code_obj 在参数 code 中
        run_code 根据输入的 code_obj 新建一个 frame 并开始运行
        """
        frame = self.make_frame(code, global_names=global_names,local_names=local_names)
        self.run_frame(frame)

class Frame(object):
    def __init__(self, code_obj, global_names, local_names, prev_frame):
        self.code_obj = code_obj
        self.f_globals = global_names
        self.f_locals = local_names
        self.prev_frame = prev_frame
        # 数据栈
        self.stack = []
        # block 栈
        self.block_stack = []
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtin__']
            if hasattr(self.builtin_names,'__dict__'):
                self.builtin_names = self.builtin_names.__dict__
        # 最后运行的指令，初始为0
        self.last_instruction = 0
        






















