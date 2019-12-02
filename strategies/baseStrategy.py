from models.enumms import Move


class BaseStrategy:
    def get_next_move(self, stage: int, opponent_move: Move, last_round_won: bool) -> Move:
        # Most override
        return Move.Water
