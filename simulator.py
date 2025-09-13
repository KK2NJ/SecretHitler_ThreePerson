import numpy as np
import torch
import random

class Simulator:
    liberal_policies_board = [0, 0, 0, 0, 0, 0] # liberalScore
    fascist_policies_board = [0, 0, 0, 0, 0, 0, 0] # fascistScore
    
    def __init__(self, presidentIndex, electionTracker = 0, num_players=7):
        self.numb_players = num_players
        self.electionTracker = electionTracker
        self.presidentIndex = presidentIndex
        self.deck_stack = self.create_deck_stack()

    @staticmethod
    def roles_distribution(num_players=7) -> dict:
        roles = { # initial roles for 7 players
            "player_1": "Liberal",
            "player_2": "Liberal",
            "player_3": "Liberal",
            "player_4": "Liberal",
            "player_5": "Fascist",
            "player_6": "Fascist",
            "player_7": "Hitler",
        }
        # shuffling roles
        temp = list(roles.values())
        random.shuffle(temp)
        #reassigning to keys 
        result_roles = dict(zip(roles.keys(), temp))
        return result_roles

    @staticmethod
    def create_deck_stack() -> list:
        # 6 "B" and 11 "R" cards
        deck = ["B"] * 6 + ["R"] * 11
        random.shuffle(deck)
        return deck

    def pop_top_three(self):
        # Custom pop to grab top 3 cards from the stack
        if len(self.deck_stack) < 3:
            raise ValueError("Not enough cards in the deck to pop 3.")
        top_three = [self.deck_stack.pop() for _ in range(3)]
        return top_three
    def election_votes(player_votes):
        pass
    def chat_claims(self):
        pass

    def investigate(self, player_seat):
        pass

    def state(self):
        pass

    def pick_government(self, president, chancellor):
        pass

    def vote(self, action):
        pass

    def action(self, state):
        pass



