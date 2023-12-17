f = open("input.txt")
line = True
index = 0
total = 0

def to_list(x):
    return [x] if type(x) is int else x

def is_order(left, right):
    # print(left, right)
    if type(left) != type(right):
        return is_order(to_list(left), to_list(right))

    if type(left) == int:
        return -1 if left < right else 0 if left == right else 1

    if not left:
        return -1 if right else 0

    if not right:
        return 1

    cmp = is_order(left.pop(0), right.pop(0))
    if cmp == 0:
        return is_order(left, right)

    return cmp

while line:
    index += 1
    left, right = eval(f.readline()), eval(f.readline())
    line = f.readline()
    print(f"Index {index}:", left, right)
    if is_order(left, right) == -1:
        print(index)
        total += index

print("Total:", total)
