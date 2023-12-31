is_test = False
filename = "test_input/day1.txt" if is_test else "input/day1.txt"
seq = [int(line) for line in open(filename).readlines()]
print("Part1:", sum(x < y for x, y in zip(seq, seq[1:])))
seq2 = [sum(z) for z in zip(seq[0:], seq[1:], seq[2:])]
print("Part2:", sum(x < y for x, y in zip(seq2, seq2[1:])))
