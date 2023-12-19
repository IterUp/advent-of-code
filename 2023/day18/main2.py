directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "3": (-1, 0),
    "1": (1, 0),
    "2": (0, -1),
    "0": (0, 1),
}

should_convert_colour = True


def assert_valid(scan_line):
    prev = None
    for interval in scan_line:
        assert interval[0] < interval[1], interval
        if prev is not None:
            assert prev[1] < interval[0]
        prev = interval


class DigInstruction:
    def __init__(self, line):
        direction, distance, colour = line.strip().split()
        if should_convert_colour:
            self.direction = directions[colour[-2]]
            self.distance = int(colour[-7:-2], 16)
            assert colour[-8] == "#"
        else:
            self.direction = directions[direction]
            self.distance = int(distance)

    def move(self, pos):
        return tuple(p + self.distance * d for p, d in zip(pos, self.direction))


def make_interval(x, y):
    return (x, y) if x < y else (y, x)


def insert_scan_line(new_interval, scan_intervals):
    assert_valid(scan_intervals)
    if not scan_intervals:
        scan_intervals.append(new_interval)
        return
    if len(scan_intervals) == 1 and scan_intervals[0] == new_interval:
        scan_intervals.pop()
        return

    for i, existing_interval in enumerate(scan_intervals):
        combined_interval = combine_intervals(existing_interval, new_interval)

        if combined_interval is not None:
            if combined_interval[0] == combined_interval[1]:
                scan_intervals.pop(i)
                return

            scan_intervals[i] = combined_interval
            if (
                i + 1 < len(scan_intervals)
                and scan_intervals[i + 1][0] == combined_interval[1]
            ):
                scan_intervals[i] = (
                    combined_interval[0],
                    scan_intervals[i + 1][1],
                )
                scan_intervals.pop(i + 1)
            while (
                i + 1 < len(scan_intervals)
                and scan_intervals[i + 1][1] < new_interval[1]
            ):
                scan_intervals.pop(i + 1)
            return

        if (
            new_interval[0] < existing_interval[0]
            and existing_interval[1] < new_interval[1]
        ):
            scan_intervals[i] = new_interval
            while (
                i + 1 < len(scan_intervals)
                and scan_intervals[i + 1][1] < new_interval[1]
            ):
                scan_intervals.pop(i + 1)
            return

        if (
            existing_interval[0] < new_interval[0]
            and new_interval[1] < existing_interval[1]
        ):
            scan_intervals[i] = (existing_interval[0], new_interval[0])
            scan_intervals.insert(i + 1, (new_interval[1], existing_interval[1]))
            return

        if new_interval[1] < existing_interval[0]:
            scan_intervals.insert(i, new_interval)
            return

    scan_intervals.append(new_interval)


def combine_intervals(old, new):
    return (
        (new[0], old[1])
        if old[0] == new[1]
        else (old[0], new[1])
        if old[1] == new[0]
        else make_interval(old[0], new[0])
        if old[1] == new[1]
        else make_interval(old[1], new[1])
        if old[0] == new[0]
        else None
    )


def scan_line_size(intervals):
    return sum(y - x + 1 for x, y in intervals)


def combined_scan_line_size(old, new):
    intervals = old + new
    intervals.sort()
    start, end = intervals[0]
    total = 0
    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            total += end - start + 1
            start, end = interval
    return total + end - start + 1


class DigInstructions:
    def __init__(self, f):
        self.instructions = [DigInstruction(line) for line in f]

    def get_verts(self, start_pos=(0, 0)):
        pos = start_pos
        yield pos
        for instruction in self.instructions:
            pos = instruction.move(pos)
            yield pos

    def get_horizontal_intervals(self):
        g = self.get_verts()
        try:
            fixed_coord = None
            while True:
                v1 = next(g)
                v2 = next(g)
                if fixed_coord is None:
                    fixed_coord = 0 if v1[0] == v2[0] else 1
                    free_coord = 0 if fixed_coord == 1 else 1
                yield v1[fixed_coord], make_interval(v1[free_coord], v2[free_coord])
        except StopIteration:
            pass

    def get_intervals_per_row(self):
        sorted_intervals = list(d.get_horizontal_intervals())
        sorted_intervals.sort()

        intervals_in_curr_row = []
        curr_row_index = 0

        for next_row_index, next_interval in sorted_intervals:
            if intervals_in_curr_row and next_row_index != curr_row_index:
                yield curr_row_index, intervals_in_curr_row
                intervals_in_curr_row = []
            curr_row_index = next_row_index
            intervals_in_curr_row.append(next_interval)
        yield curr_row_index, intervals_in_curr_row

    def count_lava(self):
        scan_intervals = []
        total = 0
        prev_row_index = 0
        for row_index, intervals_in_row in self.get_intervals_per_row():
            orig_scan_size = scan_line_size(scan_intervals)
            total += orig_scan_size * (row_index - prev_row_index - 1)
            prev_row_index = row_index
            old_scan_intervals = scan_intervals[:]
            for interval in intervals_in_row:
                insert_scan_line(interval, scan_intervals)
            total += combined_scan_line_size(old_scan_intervals, scan_intervals)
        assert not scan_intervals
        return total


d = DigInstructions(open("input.txt"))
print(d.count_lava())
