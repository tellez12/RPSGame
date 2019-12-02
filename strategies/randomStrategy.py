import random
from models.enumms import Move
from strategies.baseStrategy import BaseStrategy


class RandomStrategy(BaseStrategy):
    def __init__(self,top = 2):
        self.top = top

    def get_next_move(self, stage: int, opponent_move: Move, last_round_won: bool) -> Move:
        # Most override
        m = Move(random.randint(0, self.top))
        return m

