from model.world import World


def test_initialize_world():
    world = World()


def test_world_should_include_player():
    world = World()
    assert world.player
