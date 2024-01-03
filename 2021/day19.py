from collections import deque

is_test = False


def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))


def mult(m, v):
    return tuple(dot(row, v) for row in m)


def sub(v1, v2):
    return tuple(x - y for x, y in zip(v1, v2))


def add(v1, v2):
    return tuple(x + y for x, y in zip(v1, v2))


def matrix_mult(m1, m2):
    m2 = tuple(zip(*m2))
    return tuple(tuple(dot(m1[y], m2[x]) for x in range(3)) for y in range(3))


identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
rotate_x = ((1, 0, 0), (0, 0, 1), (0, -1, 0))
rotate_y = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))


def make_all_rotations():
    rotations = []
    m = identity
    spin_to_face = (
        (),
        (rotate_y,),
        (rotate_y,),
        (rotate_y,),
        (rotate_x, rotate_y),
        (rotate_y, rotate_y),
    )
    for pre_rotations in spin_to_face:
        for pre_rotation in pre_rotations:
            m = matrix_mult(m, pre_rotation)

        for i in range(4):
            rotations.append(m)
            m = matrix_mult(m, rotate_x)

    assert len(rotations) == 24, f"{len(rotations)}"
    assert len(set(rotations)) == 24
    return rotations


class Scanner:
    rotations = make_all_rotations()

    def __init__(self, f, index):
        self.index = index
        self.is_attached = False
        self.beacons = set()
        while line := f.readline().strip():
            self.beacons.add(tuple(int(v) for v in line.split(",")))

    def attach_to(self, fixed_scanner):
        for m in Scanner.rotations:
            curr_beacons = [mult(m, b) for b in self.beacons]

            for b1 in fixed_scanner.beacons:
                for b2 in curr_beacons:
                    offset = sub(b1, b2)
                    beacons = set(add(b, offset) for b in curr_beacons)
                    overlap = len(fixed_scanner.beacons.intersection(beacons))
                    assert overlap >= 1
                    if overlap >= 12:
                        self.beacons = beacons
                        self.is_attached = True
                        return True
        return False


def part1(scanners):
    scanners[0].is_attached = True
    unchecked = deque()
    unchecked.append(scanners[0])

    while unchecked:
        print(f"{sum(s.is_attached for s in scanners)}/{len(scanners)}")
        fixed_scanner = unchecked.popleft()
        for scanner in scanners:
            if not scanner.is_attached and scanner.attach_to(fixed_scanner):
                unchecked.append(scanner)

    assert all(scanner.is_attached for scanner in scanners)

    beacons = set()
    for scanner in scanners:
        beacons.update(set(scanner.beacons))

    return len(beacons)


def part2(scanners):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    f = open(filename)
    scanners = []
    while f.readline():
        scanners.append(Scanner(f, len(scanners)))
    return scanners


main(read_input("test_input/day19.txt" if is_test else "input/day19.txt"))
