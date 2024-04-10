import sys


class Player:

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*map(lambda x: int(x) if x.isdigit() else x, line.split('; '))) for line in lst_in]

players_filtered = list(filter(bool, players))


"""
Input:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0
"""