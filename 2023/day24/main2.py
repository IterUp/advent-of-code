from itertools import combinations

is_test = False
filename = "test_input.txt" if is_test else "input.txt"


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def cross(u, v):
    return (
        u[1] * v[2] - v[1] * u[2],
        u[2] * v[0] - v[2] * u[0],
        u[0] * v[1] - v[0] * u[1],
    )


def pos(p, v, t):
    return tuple(a + t * b for a, b in zip(p, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def X(h1, h2):
    p1, v1 = h1
    p2, v2 = h2

    return cross(sub(v2, v1), sub(p1, p2))


def Y(h1, h2):
    p1, v1 = h1
    p2, v2 = h2

    return dot(cross(v1, v2), sub(p1, p2))


# getMatrixInverse was from internet...somewhere
def transpose_matrix(m):
    return [list(row) for row in zip(*m)]


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]


def getMatrixDeterminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += (
            ((-1) ** c) * m[0][c] * getMatrixDeterminant(getMatrixMinor(m, 0, c))
        )
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [
            [m[1][1] / determinant, -1 * m[0][1] / determinant],
            [-1 * m[1][0] / determinant, m[0][0] / determinant],
        ]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)

    cofactors = transpose_matrix(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant

    return cofactors


hailstones = [
    [
        tuple(int(v) for v in pos_str.split(", "))
        for pos_str in line.strip().split(" @ ")
    ]
    for line in open(filename).read().splitlines()
]

hailstone_pairs = list(combinations(hailstones[:3], 2))

for h1, h2 in hailstone_pairs:
    print(f"v.{X(h1, h2)} = {Y(h1, h2)}")

matrix = tuple(X(h1, h2) for h1, h2 in hailstone_pairs)
inv_matrix = getMatrixInverse(matrix)
u = tuple(Y(h1, h2) for h1, h2 in hailstone_pairs)
v = tuple(round(dot(u, row)) for row in inv_matrix)
print(f"{v=}")


def mini_cross(v1, v2):
    return v1[0] * v2[1] - v2[0] * v1[1]


def find_pos(p1, v1, p2, v2):
    t0cross = mini_cross(sub(pos(p1, v1, t=0), p2), v2)
    t = 1
    step = 1
    while (result := t0cross * mini_cross(sub(pos(p1, v1, t), p2), v2)) > 0:
        t += step
        step *= 2

    while (result := mini_cross(sub(pos(p1, v1, t), p2), v2)) != 0:
        assert step > 1
        step //= 2
        if result * t0cross > 0:
            t += step
        else:
            t -= step

    return pos(p1, v1, t)


h1, h2 = hailstones[:2]
p1, v1 = h1
p2, v2 = h2

p = find_pos(p1, sub(v1, v), p2, sub(v2, v))
print(f"{p=}")
print("Answer:", sum(p))

# 315844328917588, 196475852174059, 129299668674521
