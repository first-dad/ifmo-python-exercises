#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from random import shuffle, choice


class Card(object):
    suit = None
    rank = None

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck(object):
    cards = None
    max_cards = 54
    suits = ('spade', 'club', 'heart', 'diamond')
    ranks = ('2', '3', '4',
             '5', '6', '7',
             '8', '9', '10',
             'J', 'Q', 'K', 'A')

    def __new__(cls):
        """Singleton"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Deck, cls).__new__(cls)
        return cls.instance

    def __init__(self, trump=choice(suits)):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

        if self.__is_valid_suit(trump):
            self.trump = trump
        else:
            raise Exception('Trump suit is not valid')

    def __is_valid_suit(self, suit):
        return suit in self.suits

    def shuffle(self):
        shuffle(self.cards)

    def get_cards(self, amount=6):
        if len(self.cards) < amount:
            raise Exception('Not enough cards in deck')
        else:
            return [self.cards.pop() for _ in range(amount)]


class Player(object):
    name = None
    hand = []

    def __init__(self, name):
        self.name = name

    def fill_hand(self, hand):
        self.hand += hand

    def get_hand(self):
        return self.hand


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    alex = Player('Alex')
    john = Player('John')

    a = deck.get_cards()
    b = deck.get_cards()

    for card in a:
        print card.rank, card.suit
    print
    for card in b:
        print card.rank, card.suit
    print

    alex.fill_hand(a)
    john.fill_hand(b)

    for card in john.get_hand():
        print card.rank, card.suit