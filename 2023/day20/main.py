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


class Broadcaster(Module):
    def receive(self, pulse, source):
        return self.broadcast(pulse)


class FlipFlop(Module):
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


modules = dict((m.name, m) for m in (make_module(line) for line in open("input.txt")))
modules["button"] = Button("button", "broadcaster")
for module in modules.values():
    for dst in module.destinations:
        if dst in modules:
            modules[dst].add_source(module)

for i in range(1000):
    pulses = modules["button"].push()
    while pulses:
        src, dst, pulse = pulses.pop(0)
        if dst in modules:
            out_pulses = modules[dst].receive(pulse, src)
            pulses.extend(out_pulses)

print(counts[0] * counts[1])
