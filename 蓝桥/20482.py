#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import curses
import random
from collections import defaultdict
from itertools import chain


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def spawn(self):
        new_element = 4 if random.randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height)
                        if self.field[i][j] ==0 ])
        self.field[i][j] = new_element

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string +'\n')

        def draw_hor_separator():
            line = '+' ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda :line)
            if not hasattr(draw_hor_separator,"counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5}'.format(num) if num > 0 else '|' for num in row) + '|')
            screen.clear()
            cast('SCORE: ' + str(self.score))
            if self.highscore != 0:
                cast("HIGHSCORE: ")



def is_win(self):
    return max(chain(*self.field)) >= self.win_value

def is_gameover(self):
    return not any(self.move_is_possible(move) for move in actions)

def move_is_possible(self, direction):
    def row_is_left_movable(row):
        def change(i):




def main(stdscr):

    def init():
        # 重置游戏棋盘
        return 'Game'

    def not_game(state):
        responses = defaultdict(lambda :state)
        responses['Restart'],responses['Exit'] = 'Init','Exit'
        return responses[action]

    def game():

        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        elif action = "Exit":
            return 'Exit'
        if game_field.is_win():
            return 'Win'
        elif gae_field.is_gameover():
            return 'Gameover'
        return 'Game'


    state_actions = {
        'Init':init,
        'Win':lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }


    curses.use_default_colors()
    game_field = GameField(win=2048)

    state = "Init"

    while state != 'Exit':
        state = state_actions[state]()
































