from .definitions import *
from .pieces      import *
from typing       import Type, Iterable


class Location:

    def __init__(self, file: ChessFile, rank: ChessRank) -> None:

        self.file = file
        self.rank = rank

    def as_tuple(self) -> tuple[ChessFile, ChessRank]:
        return self.file, self.rank
    
    def as_notation_tuple(self) -> tuple[str, str]:
        return self.file.string, self.rank.string
    
    def as_indices_tuple(self) -> tuple[int, int]:
        return self.file.index, self.rank.index


class Square:

    def __init__(self, color: Color, location: Location, piece: Type[PieceBase] | None) -> None:
        self.color    = color
        self.location = location


def standart_piece_on(board_size: tuple[int, int], position: tuple[int, int]) -> Type[PieceBase] | None:
    if position[1] == 2:
        return Piece.Standart.Pawn
    return None
    


class Board:

    def __init__(
            self,
            width:  int = 8,
            height: int = 8
    ) -> None:
        if width > 255 or height > 255:
            raise ValueError('board can\'t be wider/higher than 255 squares.')
        self.squares = [[Square(Color.BLACK if x + y % 2 else Color.WHITE, Location(ChessFile(x), ChessRank(y)), standart_piece_on((width, height), (x, y))) for x in range(width)] for y in range(height)]