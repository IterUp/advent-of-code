is_test = False

matched = {")": "(", "]": "[", "}": "{", ">": "<"}

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

scores2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def syntax_check(line):
    stack = []
    for c in line:
        if c in matched:
            if stack and stack[-1] == matched[c]:
                stack.pop()
            else:
                return scores[c]
        else:
            stack.append(c)
    return 0


def part1(lines):
    return sum(syntax_check(line) for line in lines)


def syntax_check2(line):
    stack = []
    for c in line:
        if c in matched:
            if stack and stack[-1] == matched[c]:
                stack.pop()
            else:
                return 0
        else:
            stack.append(c)
    return sum(scores2[c] * 5**i for i, c in enumerate(stack))


def part2(lines):
    scores = []
    for line in lines:
        score = syntax_check2(line)
        if score:
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    return open(filename).read().splitlines()


main(read_input("test_input/day10.txt" if is_test else "input/day10.txt"))
