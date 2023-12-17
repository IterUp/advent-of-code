y = 2000000
intervals = []
beacons = set()
for line in open("input.txt"):
    a, b = line.split(": closest beacon is at x=")
    sensor = [int(x) for x in a[12:].split(", y=")]
    beacon = [int(x) for x in b.split(", y=")]
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    offset = dist - abs(sensor[1] - y)
    if offset >= 0:
        intervals.append((sensor[0] - offset, sensor[0] + offset))
    if beacon[1] == y:
        beacons.add(beacon[0])

def calc_overall(intervals):
    total = 0
    begin = None
    end = None
    for interval in intervals:
        if begin is None:
            begin, end = interval
        elif interval[0] <= end + 1:
            end = max(end, interval[1])
        else:
            total += end - begin + 1
            begin = None
    if begin is not None:
        total += end - begin + 1
    return total

def count_beacons(intervals, beacons):
    print("beacons:", beacons)
    for beacon in beacons:
        v = any(interval[0] <= beacon <= interval[1] for interval in intervals)
        print("Beacon:", beacon, v)
    return sum(any(interval[0] <= beacon <= interval[1] for interval in intervals) for beacon in beacons)

print(intervals)
intervals.sort(key = lambda x: x[0])
print(intervals)
print(calc_overall(intervals) - count_beacons(intervals, beacons))
