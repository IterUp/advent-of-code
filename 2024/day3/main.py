is_enabled = True

def process_line(line):
    global is_enabled
    total = 0
    while True:
        pos = line.find("mul(")
        if pos == -1:
            return total

        do_pos = line.find("do()")
        dont_pos = line.find("don't()")
        if do_pos != -1 and do_pos < pos:
            is_enabled = True
            line = line[:do_pos+4]
        elif dont_pos != -1 and dont_pos < pos:
            is_enabled = False
            line = line[:dont_pos+7]
        else:
            line = line[pos+4:]
            comma_pos = line.find(",")
            close_pos = line.find(")")

            if (comma_pos != -1) and (comma_pos < close_pos):
                left, right = line[:comma_pos], line[comma_pos+1:close_pos]
                if left.isdecimal() and right.isdecimal():
                    total += int(left) * int(right)

f = open("input.txt")
print(sum(process_line(line) for line in f.readlines()))
