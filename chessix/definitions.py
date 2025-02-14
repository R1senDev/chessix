from enum import Enum


class Cost:
    GAME   = float('inf')
    QUEEN  = 7
    ROOK   = 5
    KNIGHT = 3
    BISHOP = 3
    PAWN   = 1
    NULL   = 0 # Please use only for invincible pieces.



class Distance:
    @classmethod
    def exactly_n(cls, n: int) -> list[int]:
        return [n]
    @classmethod
    def up_to_n(cls, n: int) -> list[int]:
        return [i for i in range(1, n + 1)]
    @classmethod
    def n_or_more(cls, n: int) -> list[int]:
        return [i for i in range(n, 510)]
    @classmethod
    def from_n_to_m(cls, n: int, m: int) -> list[int]:
        return [i for i in range(n, m + 1)]
    @classmethod
    def any(cls) -> list[int]:
        return [i for i in range(1, 510)]


class SpecialTerms(Enum):
    FIRST_RANK    = 0x00
    FURTHEST_RANK = 0x01


class ChessRank:

    def __init__(self, rank: str | int) -> None:

        if isinstance(rank, str):
            rank = int(rank)
        self.index = rank

    def __str__(self) -> str:
        return str(self.index)

    @property
    def string(self) -> str:
        return self.__str__()
    

class ChessFile:

    def __init__(self, file: str | int) -> None:

        if isinstance(file, str):
            file = int(file, 16) - 9
        self.index = file

    def __str__(self) -> str:
        return hex(self.index + 9)[-1]

    @property
    def string(self) -> str:
        return self.__str__()


class Color(Enum):
    WHITE = 0
    BLACK = 1