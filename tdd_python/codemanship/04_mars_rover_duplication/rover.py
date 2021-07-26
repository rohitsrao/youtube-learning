from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover(object):

    facing: str

    def go(self, instruction):
        compass = ['N', 'E', 'S', 'W']
        current = compass.index(self.facing)
        return replace(self, facing=compass[(current + 1) % 4])
