from dataclasses import dataclass, replace
from functools import reduce

COMPASS = ['N', 'E', 'S', 'W']
VECTORS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

@dataclass
class Rover(object):
    position: (int, int)
    facing: str

    def right(self):
        return self.turn(COMPASS)

    def left(self):
        reversed_compass = COMPASS.copy()
        reversed_compass.reverse()
        return self.turn(reversed_compass)

    def turn(self, compass):
        current = compass.index(self.facing)
        turned_facing = compass[(current+1) % len(compass)]
        return replace(self, facing=turned_facing)

    def forward(self):
        return self.move(VECTORS[COMPASS.index(self.facing)])

    def back(self):
        opposite_orientation = (COMPASS.index(self.facing) + 2) % len(COMPASS)
        vector = VECTORS[opposite_orientation]
        return self.move(vector)

    def move(self, vector):
        curr_position = self.position
        new_pos = (curr_position[0] + vector[0], curr_position[1] + vector[1])
        return replace(self, position=new_pos)

    def get_command(self, instruction):
        commands = {
            'L': lambda: self.left(),
            'R': lambda: self.right(),
            'F': lambda: self.forward(),
            'B': lambda: self.back(),
        }
        return commands[instruction]

    def go(self, instruction):
        return reduce(lambda rover, instruction: \
                      rover.get_command(instruction).__call__(),\
                      instruction, self)

