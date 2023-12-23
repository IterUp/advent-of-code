from copy import copy

lines = [line.strip().split(": ") for line in open("input.txt")]
expressions = dict(lines)
del expressions["humn"]
values = {}

had_progress = True
while had_progress:
    remaining = {}
    had_progress = False
    for variable, expression in expressions.items():
        try:
            values[variable] = int(eval(expression, {}, values))
            had_progress = True
        except NameError:
            remaining[variable] = expression
        expressions = remaining

values["humn"] = "humn"
while "root" not in values:
    for variable, expression in expressions.items():
        if variable not in values:
            left, op, right = expression.split()
            try:
                values[variable] = (op, values[left], values[right])
            except KeyError:
                pass

expr = values["root"]

value = 0
assert expr[0] == "+"
expr = ("-", expr[1], expr[2])

while isinstance(expr, tuple):
    op, left, right = expr
    if isinstance(right, int):
        expr = left
        if op == "*":
            value //= right
        elif op == "/":
            value *= right
        elif op == "+":
            value -= right
        elif op == "-":
            value += right
        else:
            assert False, f"Unknown {op=}"
    else:
        expr = right
        if op == "*":
            value //= left
        elif op == "/":
            value = left // value
        elif op == "+":
            value -= left
        elif op == "-":
            value = left - value
        else:
            assert False, f"Unknown {op=}"

print(f"{expr} = {value}")
