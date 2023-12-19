class Condition:
    def __init__(self, line):
        parts = line.split(":")
        self.condition = parts[0] if len(parts) > 1 else "True"
        self.destination = parts[-1]

    def accepts(self, part):
        return eval(self.condition, {}, part)


class Workflow:
    def __init__(self, line):
        self.conditions = [Condition(part) for part in line.split(",")]

    def next(self, part):
        for condition in self.conditions:
            if condition.accepts(part):
                return condition.destination
        assert False


class Workflows:
    def __init__(self, f):
        self.workflows = {}
        while line := f.readline().strip():
            label, remainder = line.split("{")
            self.workflows[label] = Workflow(remainder[:-1])

    def is_accepted(self, part):
        curr = "in"
        while curr not in ("A", "R"):
            curr = self.workflows[curr].next(part)

        return curr == "A"


def read_parts(f):
    while line := f.readline().strip():
        yield eval(f"dict({line[1:-1]})")


f = open("input.txt")
workflows = Workflows(f)
accepted = [part for part in read_parts(f) if workflows.is_accepted(part)]
print(sum([sum(part.values()) for part in accepted]))
