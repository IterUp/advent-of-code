def process(line):
    _, line = line.split(':')
    winning, numbers = line.split('|')
    winning = set(winning.split())
    numbers = numbers.split()
    count = sum(number in winning for number in numbers)
    return 2 ** (count - 1) if count else 0

print(sum(process(line) for line in open("input.txt").readlines()))
