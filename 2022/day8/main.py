import math

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def scenic_score_for_direction(lines, pos, direction):
    height = lines[pos[0]][pos[1]]
    count = 0
    while True:
        pos[0] += direction[0]
        pos[1] += direction[1]
        if (0 <= pos[0] < len(lines)) and (0 <= pos[1] < len(lines[0])):
            count += 1
            if lines[pos[0]][pos[1]] >= height:
                return count
        else:
            return count


def scenic_score(lines, row, col):
    return math.prod(
        scenic_score_for_direction(lines, [row, col], direction)
        for direction in directions
    )


lines = [[int(x) for x in line.strip()] for line in open("input.txt")]
print(
    max(
        scenic_score(lines, row, col)
        for row in range(len(lines))
        for col in range(len(lines[0]))
    )
)
