from math import prod


class RangeSplitter:
    def __init__(self, line):
        self.key = line[0]
        self.operation = line[1]
        self.value = int(line[2:])

    def __call__(self, range):
        exact_range = range[self.key]
        value = self.value

        if (value <= exact_range[0] and self.operation == "<") or (
            value >= exact_range[1] and self.operation == ">"
        ):
            return None

        if (value < exact_range[0] and self.operation == ">") or (
            value > exact_range[1] and self.operation == "<"
        ):
            new_range = range.copy()
            for c in "xmas":
                del range[c]
            return new_range

        new_range = range.copy()
        if self.operation == "<":
            new_range[self.key] = (exact_range[0], value - 1)
            range[self.key] = (value, exact_range[1])
        else:
            assert self.operation == ">"
            range[self.key] = (exact_range[0], value)
            new_range[self.key] = (value + 1, exact_range[1])

        return new_range


class Condition:
    def __init__(self, line):
        parts = line.split(":")
        self.destination = parts[-1]
        self.splitter = RangeSplitter(parts[0]) if len(parts) > 1 else None

    def split_range(self, range):
        return self.destination, (self.splitter(range) if self.splitter else range)


class Workflow:
    def __init__(self, line):
        self.conditions = [Condition(part) for part in line.split(",")]


class Workflows:
    def __init__(self, f):
        self.workflows = {}
        while line := f.readline().strip():
            label, remainder = line.split("{")
            self.workflows[label] = Workflow(remainder[:-1])

    def num_accepted(self, range, curr="in"):
        if curr == "A":
            return prod(y - x + 1 for x, y in range.values())
        if curr == "R":
            return 0

        total = 0
        workflow = self.workflows[curr]
        for condition in workflow.conditions:
            if range:
                new_curr, new_range = condition.split_range(range)
                if new_range is not None:
                    total += self.num_accepted(new_range, new_curr)

        return total


f = open("test_input.txt")
workflows = Workflows(f)
range = dict(x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000))

print(workflows.num_accepted(range))
