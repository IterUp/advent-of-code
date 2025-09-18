import heapq

f = open("input.txt")

grid = [line.strip() for line in f.readlines()]


def find_pos(grid, to_find):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == to_find:
                return (x, y)


deltas = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def get_scores(grid):
    pos = find_pos(grid, "S")
    d = 0
    scores = {}
    stack = [(0, pos, d, False)]
    scores[(pos, d)] = 0
    while stack:
        score, pos, d, was_turn = heapq.heappop(stack)  # stack.pop()
        # assert score == scores[(pos, d)]
        delta = deltas[d]
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
        if grid[next_pos[1]][next_pos[0]] != "#":
            new_score = score + 1
            key = (next_pos, d)
            if key not in scores or new_score < scores[key]:
                scores[key] = new_score
                heapq.heappush(
                    stack, (new_score, next_pos, d, False)
                )  # stack.append((next_pos, d, False))
        if not was_turn:
            for turn in (-1, 1):
                new_score = score + 1000
                new_d = (d + turn) % 4
                key = (pos, new_d)
                if key not in scores or new_score < scores[key]:
                    scores[key] = new_score
                    heapq.heappush(
                        stack, (new_score, pos, new_d, True)
                    )  # stack.append((pos, new_d, True))

    return scores


def part1(grid):
    scores = get_scores(grid)
    end_pos = find_pos(grid, "E")
    return min(scores[(end_pos, d)] for d in range(4) if (end_pos, d) in scores)


def part2(grid):
    scores = get_scores(grid)
    end_pos = find_pos(grid, "E")
    best_score = min(scores[(end_pos, d)] for d in range(4) if (end_pos, d) in scores)

    visited = set()
    positions = [
        (end_pos, d) for d in range(4) if scores.get((end_pos, d)) == best_score
    ]
    while positions:
        curr = positions.pop()
        pos, d = curr
        if curr not in visited:
            visited.add(curr)
            delta = deltas[d]
            prev_pos = (pos[0] - delta[0], pos[1] - delta[1])
            if scores[curr] - 1 == scores.get((prev_pos, d)):
                positions.append((prev_pos, d))
            for turn in (-1, 1):
                new_d = (d + turn) % 4
                if scores[curr] - 1000 == scores.get((pos, new_d)):
                    positions.append((pos, new_d))

    visited_without_direction = set([pos for pos, _ in visited])
    return len(visited_without_direction)


print("Part 1 =", part1(grid))
print("Part 2 =", part2(grid))
