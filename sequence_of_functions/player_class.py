from abc import ABC
from typing import List

from card import Card


class Participant:
    def __init__(self):
        self.name = None

    def get_cards(self) -> List[Card]:
        raise NotImplementedError

    def clear_cards(self):
        raise NotImplementedError

    def add_a_card(self, card: Card):
        raise NotImplementedError

    def make_a_choice(self, table_state: List[Card]):
        raise NotImplementedError


class Player(Participant, ABC):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.money = 100
        self._cards = []

    def __str__(self):
        cards_str = ''
        self._cards.sort(key=lambda ele: ele.rank.value)
        for card in self._cards:
            cards_str += str(card) + ' '
        return self.name + "(cards: " + cards_str + ')\n'

    def get_cards(self) -> List[Card]:
        return self._cards

    def clear_cards(self):
        self._cards.clear()

    def add_a_card(self, card):
        self._cards.append(card)

    def make_a_choice(self, table_state: List[Card]) -> str:
        choice = ""
        while choice not in ['H', 'P']:
            print('Table cards are: ', end='')
            print(*table_state)

            print(self.name + ', your cards are: ', end='')
            print(*self._cards)
            choice = input("Choose to [H]old or [P]ass\n")

        return choice


class Bot(Participant, ABC):
    def __init__(self):
        super().__init__()
        self.name = input("Wprowadz imie bota: ")  # do zrobienia dynamiczną numeracje przy wpisywaniu
