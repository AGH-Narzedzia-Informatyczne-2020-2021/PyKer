from deck import Deck
from sequence_of_functions.player_class import Player
from table import Table

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    players = []
    player_count = int(input('Please enter player count:\n'))
    for i in range(player_count):
        players.append(Player(input('Please enter the name for player no. ' + str(i + 1) + '\n')))

    table = Table(players=players, deck=deck)
    table.initialize_game()

    while len(table.cards) <= 5:
        table.play_a_round()
