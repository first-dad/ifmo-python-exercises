#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


from random import shuffle, choice

""""
свойства
стат методы
абстрактные
метод класса
мета класса
"""

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
        """ Singleton """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Deck, cls).__new__(cls)
        return cls.instance

    def __init__(self, trump=choice(suits)):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

        if trump in self.suits:
            self.trump = trump
        else:
            raise Exception('Trump suit is not valid')

    def shuffle(self):
        shuffle(self.cards)

    def get_cards(self, amount=6):
        if len(self.cards) < amount:
            raise Exception('Not enough cards in deck')
        else:
            return [self.cards.pop() for _ in range(amount)]


class Human(object):
    @staticmethod
    def get_quote():
        return 'Homo homini lupus est'


class Person(Human):
    name = None
    surname = None
    age = None

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return 'Имя: %s\n' \
               'Фамилия: %s\n' \
               'Возраст: %d' \
               % (self.name, self.surname, self.age)


class Player(Person):
    def __init__(self, *data):
        super(Player, self).__init__(*data)
        self.hand = []

    def fill_hand(self, cards):
        # self.hand = self.hand + cards
        self.hand += cards

    def get_hand(self):
        return self.hand

    def get_card(self):
        if len(self.hand) > 0:
            return self.hand.pop()


class Durak():
    players = None

    def __init__(self, cards, *players):
        if len(players) != 2:
            raise Exception('Need two players')
        else:
            self.players = players

        self.deck = cards

    def play(self):
        card = choice(self.players[0].hand)
        print card.rank
        print deck.ranks.index(card.rank)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    alex = Player('Dave', 'Grohl', 45)
    john = Player('John', 'Smith', 50)

    alex.fill_hand(deck.get_cards())
    john.fill_hand(deck.get_cards())

    a = 7
    while a > 0:
        print alex.get_card()
        a -= 1

    for card in alex.get_hand():
        print card.suit, card.rank

    # durak = Durak(deck, alex, john)
    # durak.play()