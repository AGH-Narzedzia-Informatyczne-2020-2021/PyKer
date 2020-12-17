from typing import List

from deck import Deck
from hand_evaluation.hand_evaluator import HandEvaluator
from hand_evaluation.handquickevaluation import HandQuickEvaluation
from sequence_of_functions.player_class import Participant


class Table:
    def __init__(self, players: List[Participant], deck: Deck):
        self.cards = []
        self.players = players
        self.deck = deck
        # map of players, true if player is still in, false if he passed
        self.round_status = {}

    def initialize_game(self):
        for i in range(3):
            self.cards.append(self.deck.top())

        print('Flop draw: ', end='')
        print(*self.cards)

        for player in self.players:
            self.round_status[player] = True
            for i in range(2):
                player.add_a_card(self.deck.top())

    def reset(self):
        self.deck.shuffle()
        for player in self.players:
            player.clear_cards()

    def position_name(self):
        positions = {1: "Flop", 2: "Flop", 3: "Flop", 4: "Turn", 5: "River"}
        return positions[len(self.cards) + 1]

    def add_card_to_table(self):
        drawn_card = self.deck.top()

        print("Card drawn at " + self.position_name() + ": " + str(drawn_card) + '\n')
        self.cards.append(drawn_card)

    def play_a_round(self):
        if len(self.cards) > 5:
            raise Exception('Too many cards on the table!')

        players_in = list(filter(lambda p: self.round_status[p] is True, self.players))
        if len(players_in) == 1:
            print(players_in[0].name + ' has won the round!\n')
        else:
            for player in players_in:
                choice = player.make_a_choice(self.cards)
                if choice == 'P':
                    self.round_status[player] = False
                    print('Player ' + player.name + ' has resigned!')

        if len(self.cards) == 5:
            self.get_last_round_result(players_in)
        else:
            self.add_card_to_table()

    def get_last_round_result(self, players_in):
        evaluations = self.fill_evaluations(players_in)

        players_with_max_eval = self.get_winning_players(evaluations)
        print('Table cards: ')
        print(*self.cards)
        print('This round winners: ', end='')
        for winner in players_with_max_eval:
            print(str(winner))
            print('winning suit: ' + str(evaluations[winner].quick_eval).split(sep='.')[1])
        exit(0)

    @staticmethod
    def get_winning_players(evaluations):
        players_with_max_eval = []
        max_eval = HandQuickEvaluation.HIGH_CARD
        for player in evaluations:
            evaluation = evaluations[player]
            if evaluation.quick_eval == max_eval:
                players_with_max_eval.append(player)

            if evaluation.quick_eval.value > max_eval.value:
                players_with_max_eval.clear()
                players_with_max_eval.append(player)
        return players_with_max_eval

    def fill_evaluations(self, players_in):
        evaluations = {}
        for player in players_in:
            available_cards = []
            available_cards.extend(player.get_cards())
            available_cards.extend(self.cards)
            evaluations[player] = HandEvaluator.value_hand(available_cards)
        return evaluations
