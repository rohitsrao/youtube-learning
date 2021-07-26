from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Rover(object):

    facing: str

    def go(self, instruction):
        if self.facing == 'N':
            return replace(self, facing = 'E')
        return replace(self, facing='S')
