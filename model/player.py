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

    def rotate(self, angle):
        """
        Rotates player around y axis (turns from side to side)
        """
        old_angle, tilt = self.rotation
        new_angle = old_angle + angle
        while new_angle > 90:
            new_angle = new_angle - 90
        while angle < -90:
            new_angle = new_angle + 90
        self.rotation = (new_angle, tilt)

    def tilt(self, angle):
        """
        Tilts player around x or z axis (looks up or down)
        """
        rot_angle, old_tilt = self.rotation
        new_tilt = old_tilt + angle
        while new_tilt > 90:
            new_tilt = new_tilt - 90
        while angle < -90:
            new_tilt = new_tilt + 90
        self.rotation = (rot_angle, new_tilt)
