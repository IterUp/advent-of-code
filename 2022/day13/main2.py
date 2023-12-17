packets = [eval(line) for line in open("input.txt") if line.strip()]


def to_list(x):
    return [x] if type(x) is int else x


def is_ordered(left, right):
    # print(left, right)
    if type(left) != type(right):
        return is_ordered(to_list(left), to_list(right))

    if type(left) == int:
        return -1 if left < right else 0 if left == right else 1

    if not left:
        return -1 if right else 0

    if not right:
        return 1

    cmp = is_ordered(left[0], right[0])
    if cmp == 0:
        return is_ordered(left[1:], right[1:])

    return cmp

low, high = [
    sum(is_ordered(packet, divider) == -1 for packet in packets) for divider in ([[2]], [[6]])
]

print(low, high)
print((low + 1) * (high + 2))
