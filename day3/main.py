def santize(line):
    return ''.join([c if c.isdigit() else '.' if c == '.' else '*' for c in line.strip()])

class Schematic:
    def __init__(self, lines):
        self.lines = [santize(line) for line in lines]

    def get_numbers(self):
        for row, line in enumerate(self.lines):
            number_str = ""
            had_symbol = False
            is_valid_number = False
            for column, c in enumerate(line):
                has_symbol = any([self.is_symbol(row-1, column), self.is_symbol(row, column), self.is_symbol(row+1, column)])
                is_valid_number = is_valid_number or has_symbol
                if c.isdigit():
                    number_str += c
                else:
                    if number_str:
                        if is_valid_number:
                            yield int(number_str)
                        else:
                            print("Skipping", number_str)
                    number_str = ""
                    is_valid_number = has_symbol
                # print(row, column, is_valid_number, number_str)


    def is_symbol(self, row, column):
        return 0 <= row < len(self.lines) and 0 <= column < len(self.lines[0]) and self.lines[row][column] == '*'


f = open("input.txt")
s = Schematic(f.readlines())

for num in s.get_numbers():
    print("> ", num)

print(sum(s.get_numbers()))
