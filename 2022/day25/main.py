is_test = False
filename = "test_input.txt" if is_test else "input.txt"
c_to_v = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
v_to_c = {v: k for k, v in c_to_v.items()}


def from_snafu(s):
    total = 0
    for c in s:
        total = 5 * total + c_to_v[c]
    return total


def to_snafu(v):
    s = ""
    while v:
        remainder = v % 5
        v //= 5
        if remainder > 2:
            v += 1
            remainder -= 5
        s = v_to_c[remainder] + s

    return s


print(to_snafu(sum(from_snafu(line.strip()) for line in open(filename).readlines())))
