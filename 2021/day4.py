is_test = False
filename = "test_input/day4.txt" if is_test else "input/day4.txt"
f = open(filename)


def read_board(f):
    board = []
    while line := f.readline().strip():
        board.append([int(v) for v in line.split()])
    return board


def read_boards(f):
    boards = []

    while True:
        board = read_board(f)
        if board:
            boards.append(board)
        else:
            return boards


def is_winner(board, numbers):
    return any(all(v in numbers for v in row) for row in board) or any(
        all(v in numbers for v in row) for row in zip(*board)
    )


def find_winner(boards, numbers):
    for board in boards:
        if is_winner(board, numbers):
            return board


def find_winners(boards, numbers):
    return [board for board in boards if is_winner(board, numbers)]


def score(board, numbers):
    return sum(v for row in board for v in row if v not in numbers)


def part1(numbers_list, boards):
    numbers = set()
    for number in numbers_list:
        numbers.add(number)
        winner = find_winner(boards, numbers)
        if winner:
            return number * score(winner, numbers)
    assert False, "There was no winner"


def part2(numbers_list, input_boards):
    boards = input_boards[:]
    numbers = set()
    for number in numbers_list:
        numbers.add(number)
        winners = find_winners(boards, numbers)
        for winner in winners:
            boards.remove(winner)
            the_score = score(winner, numbers)
            last_score = number * score(winner, numbers)
            if not boards:
                return last_score
    assert False, "There was no winner"


def main():
    numbers_list = [int(n) for n in f.readline().split(",")]
    f.readline()
    boards = read_boards(f)

    print("Part 1:", part1(numbers_list, boards))
    print("Part 2:", part2(numbers_list, boards))


main()
