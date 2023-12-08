from collections import defaultdict

def santize(line):
    return ''.join([c if c.isdigit() else '.' if c != '*' else '*' for c in line.strip()])

class Schematic:
    def __init__(self, lines):
        self.lines = [santize(line) for line in lines]

    def get_numbers(self):
        all_gears = defaultdict(list)
        for row, line in enumerate(self.lines):
            number_str = ""
            gears = []
            for column, c in enumerate(line):
                latest_gears = []
                for row2 in range(row-1, row+2):
                    if self.is_symbol(row2, column):
                        latest_gears.append((row2, column))
                gears.extend(latest_gears)
                if c.isdigit():
                    number_str += c
                else:
                    if number_str:
                        number = int(number_str)
                        print(">>", number, gears)
                        for gear in gears:
                            all_gears[gear].append(number)
                    number_str = ""
                    gears = latest_gears
                # print(row, column, is_valid_number, number_str)
        print(all_gears)
        total = 0
        for k, v in all_gears.items():
            print(k, v)
            if len(v) == 2:
                total += v[0]*v[1]
        return total



    def is_symbol(self, row, column):
        return 0 <= row < len(self.lines) and 0 <= column < len(self.lines[0]) and self.lines[row][column] == '*'


f = open("input.txt")
s = Schematic(f.readlines())

print(s.get_numbers())
