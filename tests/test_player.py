"""
        # When flying gravity has no effect and speed is increased.
        self.flying = False

        # Strafing is moving lateral to the direction you are facing,
        # e.g. moving to the left or right while continuing to face forward.
        #
        # First element is -1 when moving forward, 1 when moving back, and 0
        # otherwise. The second element is -1 when moving left, 1 when moving
        # right, and 0 otherwise.
        self.strafe = [0, 0]

        # Current (x, y, z) position in the world, specified with floats. Note
        # that, perhaps unlike in math class, the y-axis is the vertical axis.
        self.position = (0, 0, 0)

        # First element is rotation of the player in the x-z plane (ground
        # plane) measured from the z-axis down. The second is the rotation
        # angle from the ground plane up. Rotation is in degrees.
        #
        # The vertical plane rotation ranges from -90 (looking straight down)
        #  to 90 (looking straight up).
        # The horizontal rotation range is unbounded.
        self.rotation = (0, 0)

        # Which sector the player is currently in.
        self.sector = None

        # The crosshairs at the center of the screen.
        self.reticle = None

        # Velocity in the y (upward) direction.
        self.dy = 0

        # A list of blocks the player can place. Hit num keys to cycle.
        self.inventory = [BRICK, GRASS, SAND]

        # The current block the user can place. Hit num keys to cycle.
        self.block = self.inventory[0]
"""

from model.player import Player


def test_player_should_start_clean():
    player = Player()
    assert not player.flying
    assert player.position == (0, 0, 0)
    assert player.rotation == (0, 0)


def test_player_move_forward():
    player = Player()
    x_before = player.position[0]
    player.move(1, 0, 0)
    x_after = player.position[0]
    assert x_after == x_before + 1


def test_player_rotates():
    player = Player()
    rot_before = player.rotation[0]
    player.rotate(90)
    rot_after = player.rotation[0]
    assert rot_after == rot_before + 90


def test_player_doesnt_rotate_over_90_degrees():
    player = Player()
    player.rotation = (85, 0)
    player.rotate(10)
    assert (5, 0) == player.rotation


def test_player_tilts():
    player = Player()
    tilt_before = player.rotation[1]
    player.tilt(45)
    tilt_after = player.rotation[1]
    assert tilt_after == tilt_before + 45
