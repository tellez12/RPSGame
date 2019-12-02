from models.enumms import Move
from models.player import Player
from strategies.baseStrategy import BaseStrategy
from strategies.randomStrategy import RandomStrategy


class Game:
    def __init__(self, p1: Player = None, p2: Player = None):

        self.p1 = p1 if p1 else Player()
        self.p2 = p2 if p2 else Player()
        self.rounds = 10
        self.stack = 0

    def increase_score(self, p: Player):
        if p:
            p.score += 1 + self.stack
            self.stack = 0

    def check_bomb(self, p: Player, opponent: Player, m2: Move):
        p.bomb -= 1
        if p.bomb < 0 or m2 == Move.Water:
            return opponent
        return p

    def evaluate_turn(self, m1: Move, m2: Move) -> Player:
        if m1 == m2:
            if m1 == Move.Bomb:
                self.p1.bomb -= 1
                self.p2.bomb -= 1
            self.stack += 1
            return None

        if m1 == Move.Bomb:
            return self.check_bomb(self.p1, self.p2, m2)

        if m2 == Move.Bomb:
            return self.check_bomb(self.p1, self.p2, m2)

        if m1 == Move.Water:
            return self.p2

        if m2 == Move.Water:
            return self.p1

        if m1 == Move.Rock:
            if m2 == Move.Paper:
                return self.p2
            else:
                return self.p1
        elif m1 == Move.Paper:
            if m2 == Move.Scissors:
                return self.p2
            else:
                return self.p1
        elif m1 == Move.Scissors:
            if m2 == Move.Rock:
                return self.p2
            else:
                return self.p1
        else:
            raise ValueError('Something stupid happened.')

    def play(self):
        round = 0
        last_m1 = None
        last_m2 = None
        last_winner = None
        while round < self.rounds:
            round += 1
            m1 = self.p1.strategy.get_next_move(stage=round, opponent_move=last_m2, last_round_won=last_winner == self.p1)
            m2 = self.p2.strategy.get_next_move(stage=round, opponent_move=last_m1, last_round_won=last_winner == self.p2)
            print(f"{self.p1.name}:{m1} vs {self.p2.name}: {m2}")
            last_winner = self.evaluate_turn(m1,m2)
            self.increase_score(last_winner)
            print(f"Round {round}: Player 1:{self.p1.score} vs Player 2: {self.p2.score}")
            last_m1 = m1
            last_m2 = m2
players = []
players.append(Player(name="Random 3 Moves",strategy=RandomStrategy(2)))
players.append(Player(name="Random 5 Moves",strategy=RandomStrategy(4)))
players.append(Player(name="Be Water",strategy=BaseStrategy()))

for p1, in players:
    for p2 in players:
        if p1 == p2:
            continue
        print(f"******************* GAME {p1.name} vs {p2.name} *******************")
        p1.init_for_game()
        p2.init_for_game()
        g = Game(p1, p2)
        g.play()

