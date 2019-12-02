from main import Game, Move
import pytest


def test_increase_score_no_stack():
    g = Game()
    g.increase_score(g.p1)
    assert g.p1.score == 1
    assert g.p2.score == 0

    g.p2.score = 10
    g.increase_score(g.p2)
    assert g.p1.score == 1
    assert g.p2.score == 11


def test_increase_score_with_stack():
    g = Game()
    assert g.p1.score == 0
    assert g.p2.score == 0
    g.stack = 10
    g.increase_score(g.p1)
    assert g.p1.score == 11
    assert g.p2.score == 0

    g.p2.score = 10
    g.increase_score(g.p2)

def test_rock_beat_Scissors():
    g = Game()
    winner = g.evaluate_turn(Move.Rock, Move.Scissors)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Scissors, Move.Rock)
    assert winner == g.p2


def test_scissors_beat_paper():
    g = Game()
    winner = g.evaluate_turn(Move.Scissors, Move.Paper)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Paper, Move.Scissors)
    assert winner == g.p2

def test_paper_beat_rock():
    g = Game()
    winner = g.evaluate_turn(Move.Paper, Move.Rock)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Rock, Move.Paper)
    assert winner == g.p2

def test_water_beat_bomb():
    g = Game()
    winner = g.evaluate_turn(Move.Water, Move.Bomb)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Bomb, Move.Water)
    assert winner == g.p2

def test_bomb_beat_any_but_water():
    g = Game()
    # Test for p1
    winner = g.evaluate_turn(Move.Bomb, Move.Paper)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Bomb, Move.Scissors)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Bomb, Move.Rock)
    assert winner == g.p1
    # Test for p2
    winner = g.evaluate_turn(Move.Paper, Move.Bomb)
    assert winner == g.p2
    winner = g.evaluate_turn(Move.Scissors, Move.Bomb)
    assert winner == g.p2
    winner = g.evaluate_turn(Move.Rock, Move.Bomb)
    assert winner == g.p2

def test_water_lose_against_all_but_bomb():
    g = Game()
    # Test for p1
    winner = g.evaluate_turn(Move.Paper, Move.Water)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Scissors, Move.Water)
    assert winner == g.p1
    winner = g.evaluate_turn(Move.Rock, Move.Water)
    assert winner == g.p1
    #Test for p2
    winner = g.evaluate_turn(Move.Water, Move.Paper)
    assert winner == g.p2
    winner = g.evaluate_turn(Move.Water, Move.Scissors)
    assert winner == g.p2
    winner = g.evaluate_turn(Move.Water, Move.Rock)
    assert winner == g.p2

def test_tie_increase_stack_and_no_winner():
    g = Game()
    assert g.stack == 0
    winner = g.evaluate_turn(Move.Scissors, Move.Scissors)
    assert not winner
    assert g.stack == 1
    winner = g.evaluate_turn(Move.Rock, Move.Rock)
    assert not winner
    assert g.stack == 2
    winner = g.evaluate_turn(Move.Paper, Move.Paper)
    assert not winner
    assert g.stack == 3
    winner = g.evaluate_turn(Move.Bomb, Move.Bomb)
    assert not winner
    assert g.stack == 4
    winner = g.evaluate_turn(Move.Water, Move.Water)
    assert not winner
    assert g.stack == 5
