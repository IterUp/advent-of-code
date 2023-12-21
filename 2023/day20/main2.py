counts = [0, 0]


class Module:
    def __init__(self, src, dst):
        self.name = src[1:] if src[0] in ("&", "%") else src
        self.destinations = dst.split(", ")
        self.state = 0

    def broadcast(self, pulse):
        counts[pulse] += len(self.destinations)
        return [(self, dst, pulse) for dst in self.destinations]

    def add_source(self, source):
        pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Button(Module):
    def push(self):
        return self.broadcast(0)

    def receive(self, pulse, source):
        if pulse == 0:
            self.has_finished = True
        return []


class Broadcaster(Module):
    def receive(self, pulse, source):
        return self.broadcast(pulse)


class FlipFlop(Module):
    def __init__(self, *args):
        super().__init__(*args)

    def receive(self, pulse, source):
        if pulse == 0:
            self.state = 1 - self.state
            return self.broadcast(self.state)
        else:
            return []


class Conjunction(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.sources = {}

    def receive(self, pulse, source):
        self.sources[source] = pulse
        return self.broadcast(0 if all(self.sources.values()) else 1)

    def add_source(self, source):
        self.sources[source] = False


factories = {"b": Broadcaster, "%": FlipFlop, "&": Conjunction}


def make_module(line):
    src, dst = line.strip().split(" -> ")
    return factories[src[0]](src, dst)


class Modules:
    def __init__(self):
        self.modules = dict(
            (m.name, m) for m in (make_module(line) for line in open("input.txt"))
        )
        self.modules["button"] = Button("button", "broadcaster")
        self.modules["rx"] = Button("rx", "button")
        for module in self.modules.values():
            for dst in module.destinations:
                if dst in self.modules:
                    self.modules[dst].add_source(module)

    def dump_dot(self):
        print("digraph day20 {")
        for module in self.modules.values():
            if type(module) == Conjunction:
                print(f"  {module.name} [shape=box]")
        for module in self.modules.values():
            for dst in module.destinations:
                print(f"  {module.name} -> {dst}")
        print("}")

    def calc_cycles(self):
        for start in self.modules["broadcaster"].destinations:
            curr = self.modules[start]
            index = 0
            total = 0
            while curr:
                if any(
                    isinstance(self.modules[dst], Conjunction)
                    for dst in curr.destinations
                ):
                    total += 2**index
                next_names = curr.destinations
                curr = None
                for next_name in next_names:
                    next_module = self.modules[next_name]
                    if isinstance(next_module, FlipFlop):
                        curr = next_module
                index += 1
            yield total


modules = Modules()
import math

print(math.lcm(*modules.calc_cycles()))
