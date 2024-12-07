is_enabled = True

def process_line(line):
    global is_enabled
    total = 0
    while True:
        pos = line.find("mul(")
        if pos == -1:
            return total

        line = line[pos+4:]
        comma_pos = line.find(",")
        close_pos = line.find(")")

        if (comma_pos != -1) and (comma_pos < close_pos):
            left, right = line[:comma_pos], line[comma_pos+1:close_pos]
            if left.isdecimal() and right.isdecimal():
                total += int(left) * int(right)

f = open("input.txt")
print(sum(process_line(line) for line in f.readlines()))
