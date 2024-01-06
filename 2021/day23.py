is_test = False


def next_gaps(stack_num, corridor, moved):
    start = 2 + 2 * stack_num

    distance = 0
    c = start
    while c >= 0 and not isinstance(corridor[c], int):
        if corridor[c] is None:
            yield distance, corridor[:c] + (moved,) + corridor[c + 1 :]
        distance += 1
        c -= 1

    distance = 0
    c = start
    while c < len(corridor) and not isinstance(corridor[c], int):
        if corridor[c] is None:
            yield distance, corridor[:c] + (moved,) + corridor[c + 1 :]
        distance += 1
        c += 1


def calc_cost(dist, moved):
    return dist * (10**moved)


def next_moves(stacks, corridor, stack_height):
    for stack_num, stack in enumerate(stacks):
        distance = 0
        if stack and not all(v == stack_num for v in stack):
            moved = stack[-1]
            new_stacks = tuple(
                s if n != stack_num else s[:-1] for n, s in enumerate(stacks)
            )
            distance += stack_height + 1 - len(stack)
            for corridor_distance, new_corridor in next_gaps(
                stack_num, corridor, moved
            ):
                new_cost = calc_cost(distance + corridor_distance, moved)
                yield new_cost, new_stacks, new_corridor

    for pos, stack_num in enumerate(corridor):
        if isinstance(stack_num, int):
            stack = stacks[stack_num]
            if all(v == stack_num for v in stack):
                dst = 2 + 2 * stack_num

                if pos < dst:
                    if all(not isinstance(v, int) for v in corridor[pos + 1 : dst + 1]):
                        new_distance = dst - pos + stack_height - len(stack)
                        new_stacks = tuple(
                            s + (stack_num,) if i == stack_num else s
                            for i, s in enumerate(stacks)
                        )
                        new_corridor = corridor[:pos] + (None,) + corridor[pos + 1 :]
                        yield calc_cost(
                            new_distance, stack_num
                        ), new_stacks, new_corridor
                else:
                    if all(not isinstance(v, int) for v in corridor[dst:pos]):
                        new_distance = pos - dst + stack_height - len(stack)
                        new_stacks = tuple(
                            s + (stack_num,) if i == stack_num else s
                            for i, s in enumerate(stacks)
                        )
                        new_corridor = corridor[:pos] + (None,) + corridor[pos + 1 :]
                        yield calc_cost(
                            new_distance, stack_num
                        ), new_stacks, new_corridor


overall_best = 2**62


def corridor_as_str(corridor):
    return "".join(
        (" " if c is None else (chr(ord("A") + c) if isinstance(c, int) else c))
        for c in corridor
    )


def print_path(path):
    for stacks, corridor, cost in path:
        print(f"{corridor_as_str(corridor)}")
        print(stacks)
        print(cost)


def print_path(path):
    print("|".join(path))


def advance(stacks, corridor, cost, cache, path, stack_height):
    # path = path + ((stacks, corridor, cost),)
    path = path + (corridor_as_str(corridor),)
    if not any(isinstance(c, int) for c in corridor) and all(
        all(v == stack_num for v in stack) for stack_num, stack in enumerate(stacks)
    ):
        global overall_best
        if cost < overall_best:
            print("NEW BEST:", cost)
            # print(f"{path=}")
            print_path(path)
            overall_best = cost
        return cost

    if cost >= overall_best:
        return 2**62

    key = (stacks, corridor)

    if key in cache:
        return cost + cache[key]

    # print(f"{''.join(('.' if c is None else (chr(ord('A') + c) if isinstance(c, int) else c)) for c in corridor)}", overall_best)
    assert len(stacks) == 4
    assert all(len(stack) <= stack_height for stack in stacks)
    assert len(corridor) == 11
    best_cost = 2**62
    for step_cost, next_stacks, next_corridor in next_moves(
        stacks, corridor, stack_height
    ):
        new_cost = advance(
            next_stacks, next_corridor, cost + step_cost, cache, path, stack_height
        )
        best_cost = min(best_cost, new_cost)

    cache[key] = best_cost - cost

    return best_cost


def part1(stacks, corridor):
    return advance(stacks, corridor, 0, {}, (), 2)


def part2(stacks, corridor):
    global overall_best
    overall_best = 2**62

    extra_stacks = ((3, 3), (1, 2), (0, 1), (2, 0))
    stacks = tuple(
        stack[:1] + extra_stack + stack[1:]
        for stack, extra_stack in zip(stacks, extra_stacks)
    )

    return advance(stacks, corridor, 0, {}, (), 4)


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    lines = open(filename).readlines()
    corridor = tuple("X" if i in (2, 4, 6, 8) else None for i in range(11))
    stacks = tuple(
        tuple(ord(lines[r][c]) - ord("A") for r in (3, 2)) for c in range(3, 10, 2)
    )
    return stacks, corridor


main(read_input("test_input/day23.txt" if is_test else "input/day23.txt"))
