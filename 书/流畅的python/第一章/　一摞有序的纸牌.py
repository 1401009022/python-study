#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, postion):
        return self._cards[postion]

    suit_values = dict(spades=3, hearts =2, diamonds=1, clubs=0)

    def spades_high(card):
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = FrenchDeck.ranks.index(card.ranl)
        return rank_value * len(suit_values) +suit_values[card.suit]




















