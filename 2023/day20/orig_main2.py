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

    def flop_state(self):
        return ""

    def record(self):
        pass

    def dump(self):
        pass

    def name_plus(self):
        if type(self) == Conjunction:
            return "&" + self.name
        if type(self) == FlipFlop:
            return "%" + self.name
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
        self.num_flips = 0
        self.prev_state = self.state
        self.current_run = 0
        self.history = []

    def receive(self, pulse, source):
        if pulse == 0:
            self.state = 1 - self.state
            self.num_flips += 1
            return self.broadcast(self.state)
        else:
            return []

    def flop_state(self):
        return "#" if self.state == 1 else "."

    def record(self):
        return
        if self.state != self.prev_state:
            if self.history and self.history[-1][0] == self.current_run:
                self.history[-1][1] += 1
            else:
                self.history.append([self.current_run, 1])
                if self.history[-2:] == self.history[-4:-2]:
                    self.history[-4:] = [self.history[-2:], 2]
                elif len(self.history) > 2 and self.history[-2:] == self.history[-3][0]:
                    self.history = self.history[:-2]
                    self.history[-1][1] += 1
            self.current_run = 1
        else:
            self.current_run += 1

    def dump(self):
        print(f"Dump: {self.name} {self.history}")


class Conjunction(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.sources = {}

    def receive(self, pulse, source):
        self.sources[source] = pulse
        result = self.broadcast(0 if all(self.sources.values()) else 1)
        if len(self.sources) > 1:
            if result == 0:
                print("Conjunction:", self.name, num_presses)
        return result

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

    def press_until_finished(self, sorted_order=None, bits=None):
        global num_presses
        modules = self.modules
        num_presses = 0
        while not getattr(self.modules["rx"], "has_finished", False):
            pulses = modules["button"].push()
            num_presses += 1
            if num_presses % 10000 == 0:
                print(f"num_presses={num_presses}")
            while pulses:
                src, dst, pulse = pulses.pop(0)
                if dst in modules:
                    out_pulses = modules[dst].receive(pulse, src)
                    pulses.extend(out_pulses)
            print(
                "Totals:",
                [
                    sum(2**i for i, m in enumerate(curr_bits) if modules[m].state)
                    for curr_bits in bits.values()
                ],
            )
            if False:
                period = 2 ** (len(bits) - 2) if bits else 1
                if sorted_order and ((num_presses % period) == 0):
                    total = sum(
                        2**i for i, m in enumerate(bits) if modules[m].state == 1
                    )
                    t2 = "".join(m if modules[m].state else "  " for m in bits)
                    print(
                        "".join(modules[m].flop_state() for m in sorted_order),
                        t2,
                        total // period,
                    )
                # print("".join(m.flop_state() for m in modules.values()))

            if False:
                if num_presses % 2**14 == 0:
                    flips = [
                        (m.num_flips, m.name)
                        for m in modules.values()
                        if hasattr(m, "num_flips")
                    ]
                    flips.sort()
                    print("Flips:", flips, num_presses)
            if False:
                for m in modules.values():
                    m.record()
                if num_presses % 2**14 == 0:
                    for m in modules.values():
                        m.dump()

    def get_sorted(self):
        visited = []
        distance = 0
        layer = [self.modules["button"].name]
        visited.append("button")
        while layer:
            print(distance, ":", [self.modules[name].name_plus() for name in layer])
            distance += 1
            next_layer = []
            for module in layer:
                for dst in self.modules[module].destinations:
                    if dst not in visited:
                        next_layer.append(dst)
                        visited.append(dst)
            layer = next_layer
        return [v for v in visited if type(self.modules[v]) == FlipFlop]

    def dump_conjunctions(self):
        print("Conjunctions")
        for m in self.modules.values():
            if type(m) == Conjunction:
                print(
                    f"{m.name}: {[self.modules[dst].name_plus() for dst in m.destinations]}"
                )
        print("Sources")
        for m in self.modules.values():
            if type(m) == Conjunction:
                print(f"{m.name}: {[dst for dst in m.sources]}")

    def dump_dot(self):
        print("digraph day20 {")
        for module in self.modules.values():
            if type(module) == Conjunction:
                print(f"  {module.name} [shape=box]")
        for module in self.modules.values():
            for dst in module.destinations:
                print(f"  {module.name} -> {dst}")
        print("}")


modules = Modules()
modules.dump_conjunctions()
if False:
    sorted_order = modules.get_sorted()
    for i, module in enumerate(sorted_order, 1):
        print(f"{i}: {module}")
else:
    sorted_order = None

if True:
    bits = {
        "sl": ["rq", "xd", "mm", "ql", "fz", "jc", "fk", "cc", "gv", "jl", "mr", "dc"],
        "fv": ["cn", "kp", "pq", "lx", "gs", "xt", "gn", "hk", "jx", "bf", "jr", "bc"],
        "rt": ["bs", "mk", "kt", "bt", "fn", "vj", "rr", "hv", "zz", "jg", "vm", "pn"],
        "gk": ["bz", "sc", "sm", "mx", "rl", "rh", "vq", "ng", "vz", "lg", "rk", "sb"],
    }

    modules.press_until_finished(sorted_order, bits)
    print(counts[0] * counts[1])

# modules.dump_dot()
