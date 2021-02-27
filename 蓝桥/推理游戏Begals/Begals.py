#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import random

NUM_DIGITS = 3   #猜测的数字长度
MAX_GUESS = 10   #最多猜测的次数

def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10)) # 获取0-9
    random.shuffle(numbers)   # 打乱顺序
    secretNum = ''
    for i in range(NUM_DIGITS):   # 循环猜测数字的次数
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    # 返回一个由 Pico, Fermi 和 Bagels 组成的，用来提示用户的字符串
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        # else:
        #     clues.append('wrong')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()   # sort() 按照字母顺序或数字顺序重新排列列表中的元素
    return ' '.join(clues)

def isOnlyDigits(num):
    # 如果字符串只包含数字，返回真 否则返回假
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))
    guessesTaken = 1
    while guessesTaken < MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()
        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break














