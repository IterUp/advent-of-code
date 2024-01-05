from math import prod

is_test = False

def clip_range(a, b):
    return range(max(a, -50), min(b, 50))

def make_cubes(steps):
    cubes = set()
    for step_num, (is_on, cube) in enumerate(steps):
        print(f"{step_num=} {cube=}")
        for x in clip_range(*cube[0]):
            for y in clip_range(*cube[1]):
                for z in clip_range(*cube[2]):
                    if is_on:
                        cubes.add((x, y, z))
                    else:
                        try:
                            cubes.remove((x, y, z))
                        except KeyError:
                            pass
    return cubes


def make_cubes2(steps):
    maxes = tuple(max(cube[i][1] for _, cube in steps) for i in range(3))
    print(f"{maxes=}")

    grid = [[[False] * maxes[2] for y in range(maxes[1])] for x in range(maxes[0])]

    for step_num, (is_on, cube) in enumerate(steps):
        print(f"{step_num=} {cube=}")
        for x in range(*cube[0]):
            for y in range(*cube[1]):
                for z in range(*cube[2]):
                    assert (x, y, z) != (379, 833, 345)
                    grid[x][y][z] = is_on
    print("make_cubes2")
    return grid


def part1(steps):
    return len(make_cubes(steps))


def make_mini_cube(cube, values_per_axis):
    return tuple(
        tuple(values_per_axis[i].index(v) for j, v in enumerate(cube[i]))
        for i in range(3)
    )


def cube_size(cube, values_per_axis):
    assert all(p < len(values) for p, values in zip(cube, values_per_axis)), f"{cube=}"
    try:
        return prod(
            (values[p + 1] - values[p]) for p, values in zip(cube, values_per_axis)
        )
    except:
        print(f"{cube=}")


def part2(steps):
    values_per_axis = [set() for i in range(3)]
    for is_on, cube in steps:
        for i in range(3):
            values_per_axis[i].add(cube[i][0])
            values_per_axis[i].add(cube[i][1])

    values_per_axis = [sorted(v) for v in values_per_axis]
    print(f"{[len(axis) for axis in values_per_axis]=}")

    mini_steps = [
        (is_on, make_mini_cube(cube, values_per_axis)) for is_on, cube in steps
    ]

    grid3d = make_cubes2(mini_steps)

    assert not any(grid3d[-1][-1])
    assert not any(grid3d[-1][i][-1] for i in range(len(grid3d[0])))
    assert not any(grid3d[i][-1][-1] for i in range(len(grid3d)))

    total = 0

    for x, grid2d in enumerate(grid3d):
        print(f"{x=}")
        for y, row in enumerate(grid2d):
            for z, is_on in enumerate(row):
                if is_on:
                    total += cube_size((x, y, z), values_per_axis)
    return total


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def make_range(range_str):
    a, b = range_str[2:].split("..")
    return int(a), int(b) + 1


def make_step(on_str, cube_str):
    return on_str == "on", tuple(
        make_range(range_str) for range_str in cube_str.split(",")
    )


def read_input(filename):
    return ([make_step(*line.strip().split()) for line in open(filename).readlines()],)


main(read_input("test_input/day22.txt" if is_test else "input/day22.txt"))
