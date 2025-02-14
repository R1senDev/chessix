from .definitions import *
from typing       import TypeVar, Type, Tuple


class ComplexMoves:

    def __init__(self, distances: list[tuple[int, int]]) -> None:
        self.dists = distances


class Moves:

    def __init__(
            self,
            forwards:           list[int] = [0],
            sideways:           list[int] = [0],
            backwards:          list[int] = [0],
            diagonal_forwards:  list[int] = [0],
            diagonal_backwards: list[int] = [0]
    ) -> None:
        self.forwards           = forwards
        self.sideways           = sideways
        self.backwards          = backwards
        self.diagonal_forwards  = diagonal_forwards
        self.diagonal_backwards = diagonal_backwards


class PieceProperties:

    def __init__(self) -> None:

        self.times_moved = 0


class PieceBase:
    '''
    Base class for any chiece pess.
    '''

    def __init__(
            self,
            notation: str,
            cost: int | float,
            color: Color,
    ):
        self.notation = notation
        self.color = color
        self.cost = cost

        self.layer = 0 # Well, that's a weird attribute. Read NOTES.md, "Pieces ant their properties", point #1.

        self.can_jump_over      = 0          # Can ignore N pieces on its way.
        self.can_move_anywhere  = False      # Read NOTES.md, "Pieces ant their properties", point #2.
        self.can_move_to_danger = True       # Can end its move on the square, attacked by the opponent. Does nothing if self.complex_move is True.
        self.can_be_captured    = True       # That's basically invincibility.
        self.multi_move         = False      # Can be moved any times before player's move ends, but cannot end its move in the same location where it started moving.
        self.must_be_moved      = False      # If player have at least one piece with this property, he must move it. If have many of those, may choose any of them.
        self.must_jump_over     = 0          # Must jump over N pieces to make the move.
        self.must_leave_danger  = False      # If under any threat, piece should leave it.
        self.promotion_rank     = 0          # If piece will reach this rank, it have to be promoted to any of pieces, defined in self.promotion_targets. 0 for no promotion.
        self.promotion_to       = ()         # Defines pieces in which this piece can be promoted.
        self.scheme_moving      = (Moves(),) # Piece's moving scheme.
        self.scheme_first_move  = (Moves(),) # Piece's first move scheme. Can't capture this way if not allowed by self.scheme_capturing. Extends self.scheme_moving.
        self.scheme_capturing   = (Moves(),) # Piece's capturing scheme.

        self._properties = PieceProperties()

    @property
    def complex_move(self) -> bool:
        return  any([isinstance(elem, ComplexMoves) for elem in self.scheme_moving]) or \
                any([isinstance(elem, ComplexMoves) for elem in self.scheme_capturing])

AnyPiece = TypeVar('AnyPiece', bound = PieceBase)


class Piece:

    class Standart:

        class Pawn(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('', Cost.PAWN, color)
                self.promotion_rank = SpecialTerms.FURTHEST_RANK
                self.promotion_to = (
                    Piece.Standart.Rook,
                    Piece.Standart.Knight,
                    Piece.Standart.Bishop,
                    Piece.Standart.Queen
                )
                self.scheme_moving     = Moves(forwards = Distance.exactly_n(1))
                self.scheme_first_move = Moves(forwards = Distance.exactly_n(2))
                self.scheme_capturing  = Moves(diagonal_forwards = Distance.exactly_n(1))

        class Knight(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('N', Cost.KNIGHT, color)
                self.scheme_moving = ComplexMoves([(2, 1)])
                self.scheme_capturing = self.scheme_moving

        class Bishop(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('B', Cost.BISHOP, color)
                self.scheme_moving = Moves(
                    diagonal_forwards  = Distance.any(),
                    diagonal_backwards = Distance.any()
                )
                self.scheme_capturing = self.scheme_moving

        class Rook(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('R', Cost.ROOK, color)
                self.scheme_moving = Moves(
                    forwards           = Distance.any(),
                    sideways           = Distance.any(),
                    backwards          = Distance.any()
                )
                self.scheme_capturing = self.scheme_moving

        class Queen(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('Q', Cost.QUEEN, color)
                self.scheme_moving = Moves(
                    forwards           = Distance.any(),
                    sideways           = Distance.any(),
                    backwards          = Distance.any(),
                    diagonal_forwards  = Distance.any(),
                    diagonal_backwards = Distance.any()
                )
                self.scheme_capturing = self.scheme_moving

        class King(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('K', Cost.GAME, color)
                self.can_move_to_danger = False
                self.can_leave_danger   = False
                self.scheme_moving = Moves(
                    forwards           = Distance.exactly_n(1),
                    sideways           = Distance.exactly_n(1),
                    backwards          = Distance.exactly_n(1),
                    diagonal_forwards  = Distance.exactly_n(1),
                    diagonal_backwards = Distance.exactly_n(1)
                )
                self.scheme_capturing = self.scheme_moving
    
    class Animals:

        class Camel(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('C', Cost.KNIGHT, color)
                self.scheme_moving = ComplexMoves([(3, 1)])
                self.scheme_capturing = self.scheme_moving

        class Duck(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('D', Cost.NULL, color)
                self.layer = 1
                self.can_move_anywhere = True
                self.can_be_captured = False

        class Elephant(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('E', 2, color)
                self.can_jump_over = True
                self.scheme_moving = Moves(
                    diagonal_forwards  = Distance.exactly_n(2),
                    diagonal_backwards = Distance.exactly_n(2)
                )
                self.scheme_capturing = self.scheme_moving

        class Zebra(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('Z', Cost.KNIGHT, color)
                self.scheme_moving = ComplexMoves([(3, 2)])
                self.scheme_capturing = self.scheme_moving

    class Random:

        class Cannon(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('Ca', 4, color)
                self.scheme_moving = Moves(
                    forwards           = Distance.any(),
                    sideways           = Distance.any(),
                    backwards          = Distance.any()
                )
                self.scheme_capturing = self.scheme_moving
                self.can_jump_over = 1
                self.must_jump_over = 1
    
    class WeirdAndUnbalanced:

        class Rider(PieceBase):
            def __init__(self, color: Color) -> None:
                super().__init__('Ri', 5, color)
                self.scheme_moving = ComplexMoves([(2, 1)])
                self.scheme_capturing = self.scheme_moving
                self.multi_move = True