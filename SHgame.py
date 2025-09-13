import numpy as np
from elections import Elections
from fascist_board import FascistBoard
from liberal_board import LiberalBoard
from roles import Roles
from pick_government import PickGovernment
from deck import Deck

class SecretHitler_3P:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.elections = Elections()
        self.fascist_board = FascistBoard()
        self.liberal_board = LiberalBoard()
        self.roles = Roles(num_players)
        self.pick_government = PickGovernment()
        self.deck = Deck()
    
    def start(self):
        print("")
        self.roles.assign_roles()
        self.elections.begin()
        