#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

import curses #用来在终端上显示图形界面
from random import randrange,choice # 生成随机数
from collections import defaultdict
# collections 提供了一个字典的子类 defaultdict。可以指定 key 值不存在时，value 的默认值。

action =""

def init():
    """初始化游戏棋盘"""
    return 'Game'

def not_game(state):
    """
    展示游戏结束界面
    读取用户输入得到action，判断是重启游戏还是结束游戏

    :param state:
    :return:
    """
    #defaultdict 参数是callable类型 所以需要传递一个函数
    responses = defaultdict(lambda : state)
    #在字典中新建两个键值对
    responses['Restart'], responses['Exit'] = 'Init','Exit'
    return responses[action]

def game():
    """
    画出当前棋盘状态
    读取用户输入得到action
    :return:
    """
    if action == 'Restart':
        return 'Init'
    elif action == 'Exit':
        return 'Exit'
    # if 成功移动了一步


    return 'Game'

state_actions = {
    'Init':init,
    'Win':lambda : not_game('Win'),
    'Gameover':lambda : not_game('Gameover'),
    'Game':game
}

def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        # 返回按下键位的 ASCII 值
        char = keyboard.getch()
    # 返回输入键位对应的行为
    return actions_dict[char]

def spawnnumber(self):
    # 从 100 中取一个随机数，如果这个随机数大于 89，new_element 等于 4，否则等于 2
    new_element = 4 if randrange(100) > 89 else 2
    #得到一个随机空白位置的元组坐标
    (i,j) = choice([i,j] for i in range(self.width) for j in range(self.height) if
                   self.field[i][j] == 0)
    self.field[i][j] = new_element

def reset(self):
    #更新分数
    if self.score > self.highscore:
        self.highscore = self.score
    self.score = 0
    #初始化游戏开始界面
    self.field = [[0 for i in range(self.width)]
                  for j in range(self.height)]
    self.spawn()
    self.spawn()

def move_row_left(self,row):
    def tighten(row):
        """把零散的非零单元挤到一块"""
        # 先将非0的元素全拿出来加入到新列表
        new_row = [i for i in row if i != 0]
        # 按照原列表的大小，给新列表后面补0
        new_row += [0 for i in range(len(row) - len(new_row))]
        return new_row
    def merge(row):
        '''对临近元素进行合并'''
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                 # 合并后，加入乘 2 后的元素在 0 元素后面
                new_row.append(2 * row[i])
                # 更新分数
                self.score += 2 * row[i]
                pair = False
            else:
                #判断相邻元素能否合并
                if i +1 < len(row) and row[i] == row[i+1]:
                    pair = True
                    # 可以合并时，新列表加入元素 0
                    new_row.append(0)
                else:
                    #不能合并，新列表中加入该元素
                    new_row.append(row[i])
        # 断言合并后不会改变行列大小，否则报错
        assert len(new_row) == len(row)
        return new_row
    #先挤到一块再合并再挤到一块
    return tighten(merge(tighten(row)))

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::1] for row in field]

def move(self, direction):
    # 创建 moves 字典，把不同的棋盘操作作为不同的 key，对应不同的方法函数
    moves = {}
    moves['Left'] = lambda field : [move_row_left(row) for row in field]
    moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
    moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
    moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))
    # 判断棋盘操作是否存在且客行
    if direction in moves:
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn
            return True
        else:
            return False

def move_is_possible(self, direction):
    '''
    传入要移动的方向
    判断能否向这个方向移动
    :param self:
    :param direction:
    :return:
    '''
    def row_is_left_movable(row):
        '''判断这一行里面能否有元素进行左移动或合并'''
        def change(i):
            # 当左边有空位（0），右边有数字时，可以向左移动
            if row[i] == 0 and row[i+1] !=0 :
                return True
            # 当左边有一个数和右边的数相等时，可以向左合并
            if row[i] != 0 and row[i+1] == row[i]:
                return True
            return False
        return any(change(i) for i in range(len(row) - 1))

    # 检查能否移动 （合并也可以看作是在移动）
    check = {}
    # 判断矩阵每一行有没有可以左移动的元素
    check['Left'] = lambda field: any(row_is_left_movable(row)
                                      for row in field)
    # 判断矩阵每一行有没有可以右移动的元素。这里只用进行判断，所以矩阵变换之后，不用再变换复原
    check['Right'] = lambda field: check['Left'](invert(field))
    check['Up'] = lambda field: check['Left'](transpose(field))
    check['Down'] = lambda field: check['Right'](transpose(field))
    # 如果 direction 是“左右上下”即字典 check 中存在的操作，那就执行它对应的函数
    if direction in check:
        # 传入矩阵，执行对应函数
        return check[direction](self.field)
    else:
        return False

def is_win(self):
    # 任意一个位置的数大于设定的win值时，游戏胜利
    return any(any(i >= self.win_value for i in row) for row in self.field)

def is_gameover(self):
    # 无法移动和合并时，游戏失败
    return not any(self.move_is_possible(move) for move in actions)




class GameFiel(object):
    """
    棋盘类
    """
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win    # 过关分数
        self.score = 0          # 当前分数
        self.highscore = 0      # 最该分
        self.reset()            # 棋盘重置

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        # 绘制函数
        def cast(string):
            # addstr()方法将传入的内容展示到终端
            screen.addstr(string + '\n')

        # 绘制水平分割线的函数
        def draw_hor_separator():
            line = '+' + ('+------'*self.width +'+'[1:])
            cast(line)

        # 绘制竖直分割线的函数
        def draw_

state = 'Init'

# 状态机开始循环
while state != 'Exit':
    state = state_actions[state]()









#用户的行为 上下左右移动、游戏重置、退出
actions = ['Up','Left','Down','Right','Restart','Exit']

# ord() 函数以一个字符作为参数，返回参数对应的 ASCII 数值，便于和后面捕捉的键位关联
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
#将输入与行为关联
actions_dict = dict(zip(letter_codes, actions*2))
print(actions_dict)

























