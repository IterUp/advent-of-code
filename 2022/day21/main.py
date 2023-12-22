lines = [line.split(":") for line in open("input.txt")]
locals = {}

while "root" not in locals:
    for variable, expression in lines:
        try:
            locals[variable] = eval(expression, {}, locals)
        except NameError:
            pass

print(int(locals["root"]))
