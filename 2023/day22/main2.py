from typing import NamedTuple


def make_pos(pos_string: str):
    return Pos(*[int(v) for v in pos_string.split(",")])


class Pos(NamedTuple):
    x: int
    y: int
    z: int


class Brick:
    def __init__(self, line, index):
        self.pos, high = [make_pos(pos_str) for pos_str in line.split("~")]
        self.size = Pos(*[y - x for x, y in zip(self.pos, high)])
        self.index = index
        self.supporting = []
        self.supported_by = []

    @property
    def top(self):
        return self.pos.z + self.size.z

    @property
    def bottom(self):
        return self.pos.z

    def overlaps(self, brick):
        return (
            (self.pos.x <= brick.pos.x + brick.size.x)
            and (brick.pos.x <= self.pos.x + self.size.x)
            and (self.pos.y <= brick.pos.y + brick.size.y)
            and (brick.pos.y <= self.pos.y + self.size.y)
        )

    def drop_to(self, bricks):
        new_height = max(
            [
                brick.top
                for brick in bricks
                if brick.top < self.bottom and self.overlaps(brick)
            ],
            default=0,
        )
        self.pos = Pos(self.pos.x, self.pos.y, new_height + 1)

    def num_in_chain(self):
        gone = set()
        gone.add(self)
        layer = [self]
        while layer:
            next_layer = []
            for curr_brick in layer:
                for upper in curr_brick.supporting:
                    if all(
                        lower_supporting in gone
                        for lower_supporting in upper.supported_by
                    ):
                        gone.add(upper)
                        next_layer.append(upper)
            layer = next_layer
        return len(gone) - 1


bricks = [
    Brick(line, index)
    for index, line in enumerate(open("input.txt").read().splitlines())
]

bricks.sort(key=lambda b: b.pos.z)

for i, brick in enumerate(bricks):
    brick.drop_to(bricks[:i])

for supporter in bricks:
    for supported in bricks:
        if supported.bottom == supporter.top + 1 and supported.overlaps(supporter):
            supporter.supporting.append(supported)
            supported.supported_by.append(supporter)

print(sum(brick.num_in_chain() for brick in bricks))
