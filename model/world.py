from model.player import Player

WORLD_SIZE = 160


class World:

    def __init__(self, player=None):
        # model is a dict with positions (x,y,z) as keys
        #   and blocks as values
        self.model = {}

        # size is a measurement of both width and length
        self.size = WORLD_SIZE

        # player is an instance of Player
        # it contains data about characters in the game
        # eg: position, orientation, health
        # TODO should be possible to have more than one
        if not player:
            self.player = Player()
        elif isinstance(player, Player):
            self.player = player
