from collections import defaultdict

directions = ((0, -1), (0, 1), (-1, 0), (1, 0))


def offsets(pos, direction):
    [[p + (v if v != 0 else i) for p, v in zip(pos, direction)] for i in range(-1, 2)]


def calc_next_pos(curr_pos, elves, start_turn):
    if (
        sum(
            (curr_pos[0] + x, curr_pos[1] + y) in elves
            for x in range(-1, 2)
            for y in range(-1, 2)
        )
        == 1
    ):
        return curr_pos

    for i in range(4):
        turn = (start_turn + i) % 4
        direction = directions[turn]
        positions_to_check = [
            tuple(p + (v if v != 0 else i) for p, v in zip(curr_pos, direction))
            for i in range(-1, 2)
        ]

        if all(pos not in elves for pos in positions_to_check):
            return positions_to_check[1]

    return curr_pos


lines = open("input.txt").read().splitlines()
elves = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            elves.add((x, y))


def print_elves(elves):
    min_corner, max_corner = [
        tuple(f(p[i] for p in elves) for i in (0, 1)) for f in (min, max)
    ]

    for y in range(min_corner[1], max_corner[1] + 1):
        print(
            "".join(
                "#" if (x, y) in elves else "."
                for x in range(min_corner[0], max_corner[0] + 1)
            )
        )

    print(
        (max_corner[0] - min_corner[0] + 1) * (max_corner[1] - min_corner[1] + 1)
        - len(elves)
    )


num_moved = -1
turn = 0
while num_moved != 0:
    proposals = []
    proposal_counts = defaultdict(int)
    num_moved = 0
    for elf in elves:
        next_pos = calc_next_pos(elf, elves, turn)
        num_moved += (elf != next_pos)
        proposals.append((elf, next_pos))
        proposal_counts[next_pos] += 1
    elves = [new if proposal_counts[new] == 1 else old for old, new in proposals]
    print(f"End of Round {turn + 1} {num_moved=}")
    turn += 1
    # print_elves(elves)
