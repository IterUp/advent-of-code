is_test = False

d = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_literal(stream):
    total = 0
    continues = 1
    while continues:
        continues = stream.read_int(1)
        total = 16 * total + stream.read_int(4)
    stream.round()
    return total


class Packet:
    def __init__(self, stream):
        self.packets = []
        self.version = stream.read_int(3)
        self.type = stream.read_int(3)
        if self.type == 4:
            self.value = read_literal(stream)
        elif stream.read_int(1):
            num_packets = stream.read_int(11)
            self.packets = [Packet(stream) for i in range(num_packets)]
        else:
            num_bytes = stream.read_int(15)
            new_stream = BinaryStream(stream.read(num_bytes))
            while not new_stream.is_empty():
                self.packets.append(Packet(new_stream))

    def sum_versions(self):
        return self.version + sum(p.sum_versions() for p in self.packets)


class BinaryStream:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def read(self, num_bits):
        start = self.pos
        self.pos += num_bits
        return self.data[start : self.pos]

    def read_int(self, num_bits):
        return int(self.read(num_bits), 2)

    def round(self):
        return
        self.pos += 4 - (self.pos % 4) % 4

    def is_empty(self):
        return self.pos >= len(self.data)


def part1(line):
    stream = BinaryStream(line)
    p = Packet(stream)
    return p.sum_versions()


def part2(line):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    return "".join(d[c] for c in open(filename).readline().strip())


main(read_input("test_input/day16.txt" if is_test else "input/day16.txt"))
