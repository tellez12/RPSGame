import string

from strategies.baseStrategy import BaseStrategy
from strategies.randomStrategy import RandomStrategy


class Player:
    def __init__(self, max_bombs: int = 3, name: string = '', strategy: BaseStrategy = None):
        self.score = 0
        self.rounds_won = 0
        self.games_won = 0
        self.maxBomb = max_bombs
        self.bomb = max_bombs
        self.name = name
        self.strategy = strategy if strategy else RandomStrategy()

    def init_for_game(self):
        self.bomb = self.maxBomb
        self.score = 0

