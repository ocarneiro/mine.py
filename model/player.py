class Player:
    """
    Defines the character playing the game.
    What it's doing, where it's facing, what he's holding.
    """
    def __init__(self):
        self.flying = False

        # Current (x, y, z) position in the world, specified with floats. Note
        # that, perhaps unlike in math class, the y-axis is the vertical axis.
        self.position = (0, 0, 0)

        # First element is rotation of the player in the x-z plane (ground
        # plane) measured from the z-axis down. The second is the rotation
        # angle from the ground plane up. Rotation is in degrees.
        #
        # The vertical plane rotation ranges from -90 (looking straight down)
        # to 90 (looking straight up).
        # The horizontal rotation range is unbounded.
        self.rotation = (0, 0)

    def move(self, x, y, z):
        """
        Changes the position of the player in increments for each axis.
        ex: move(1, 0, 0) moves the player 1 unit in x direction
        """
        oldx, oldy, oldz = self.position
        self.position = (oldx + x, oldy + y, oldz + z)
