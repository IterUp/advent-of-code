def process(line):
    _, line = line.split(':')
    winning, numbers = line.split('|')
    winning = set(winning.split())
    numbers = numbers.split()
    return sum(number in winning for number in numbers)

lines = open("input.txt").readlines()
cards = [1]*len(lines)
for i, line in enumerate(lines):
    count = process(line)
    for j in range(i+1, i+1+count):
        cards[j] += cards[i]
print(sum(cards))
