""" Draws an ascii version of the map"""


def draw(world, y=-1, x=0, z=0):

    for v in range(-10 + z, 10 + z):
        line = ''
        for h in range(-20 + x, 20 + x):
            key = (h, y, v)
            if int_pos(world.player.position) == key:
                player = symbol_for_rotation(world.player.rotation[0])
                line += player
            elif key in world.model.keys():
                block = world.model[key]
                line += block.madeof[0]
            else:
                line += ' '
        print(line)


def symbol_for_rotation(rotation):
    rotation = int(rotation)
    return "*"


def int_pos(position):
    x, y, z = position
    return (int(x), int(y), int(z))
