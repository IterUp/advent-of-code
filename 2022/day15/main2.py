upper = 4000000

class Sensor:
    def __init__(self, line):
        a, b = line.split(": closest beacon is at x=")
        self.pos = [int(x) for x in a[12:].split(", y=")]
        self.beacon = [int(x) for x in b.split(", y=")]
        self.dist = abs(self.pos[0] - self.beacon[0]) + abs(self.pos[1] - self.beacon[1])

    def get_interval(self, y):
        offset = self.dist - abs(self.pos[1] - y)
        if offset >= 0:
            return (self.pos[0] - offset, self.pos[0] + offset)

class Sensors:
    def __init__(self, f):
        self.sensors = [Sensor(line) for line in f]

    def missing_positions(self, y, low, high):
        total = 0
        begin = low
        end = low - 1
        for interval in self.get_intervals(y):
            if interval[0] <= end + 1:
                end = max(end, interval[1])
            else:
                for x in range(end + 1, interval[0]):
                    yield x
                end = interval[1]

    def get_intervals(self, y):
        intervals = []
        for sensor in self.sensors:
            interval = sensor.get_interval(y)
            if interval is not None:
                intervals.append(interval)
        intervals.sort(key = lambda x: x[0])
        return intervals


sensors = Sensors(open("input.txt"))

for y in range(0, upper+1):
    if y % 100000 == 0:
        print(y//100000)
    for x in sensors.missing_positions(y, 0, upper):
        print(4000000*x + y)
