from deck import Deck
from sequence_of_functions.player_class import Player
from table import Table

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    players = [Player('asdf'), Player('zcvz')]

    table = Table(players=players, deck=deck)
    table.initialize_game()

    while len(table.cards) <= 5:
        table.play_a_round()
