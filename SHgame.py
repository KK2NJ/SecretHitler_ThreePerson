import numpy as np
from elections import Elections


class SecretHitler_3P:
    def __init__(self, num_players=3):
        self.num_players = num_players
        self.elections = Elections()
