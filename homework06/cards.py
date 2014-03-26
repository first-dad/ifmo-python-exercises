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

    def get_cards(self, amount):
        if len(self.cards) < amount:
            print 'Not enough cards in deck'
        else:
            return [self.cards.pop() for card in range(amount)]


class Player(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    print deck.trump

    for card in deck.cards:
        print card.suit, card.rank

    for card in deck.get_cards(5):
        print card.suit, card.rank
