# Important notes

## Pieces and their properties

1. `PieceBase.layer` (`0` by default): *player have to move exactly one piece from each layer.* Example:
    - In **standart chess** every piece is on the layer `0`.
    - In **chess with a Duck** *(`Pieces.Animals.Duck` by the way)*, every piece excluding Duck is on the layer 0. Duck is special. Duck is on the layer `1`. So player have to move any standart piece **and** the Duck on the same move.

    For your custom pieces I recommend to use layers `2`, `3`, etc. It's for the built-in Duck compatibility. But if this is the expected behavior, then who am I to stop you from using `PieceBase.layer = 1`?

1. `PieceBase.can_move_anywhere` (`False` by default): if `True`, this piece will override its moves schemes and can be placed to any free square. Those pieces can't capture, but they're can be captur**ed** if `can_be_captured` is `True`.
   > ### There are important consequences to know!
   > Setting this will make irrelevant following properties:
   > - `can_jump_over`
   > - `multi_move`
   > - `must_jump_over`
   > - Every `scheme`.
   >
   > So you can stay calm about setting up them.