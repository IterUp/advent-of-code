class Valve:
    def __init__(self, line):
        parts = line.strip().split()
        self.label = parts[1]
        self.rate = int(parts[4][5:-1])
        self.tunnels = [part.removesuffix(',') for part in parts[9:]]

class Valves:
    def __init__(self, valves):
        self.all_valves = dict((valve.label, valve) for valve in valves)
        self.rate_valves = dict((valve.label, valve) for valve in valves if valve.rate)

    def release_pressure(self, time, pos, opened, visited):
        result = 0
        time -= 1
        if time == 0:
            return 0

        valve = self.valves[pos]
        if valve.rate != 0 and valve.label != opened:
            result = time * valve.rate
            new_opened = opened.copy()
            new_opened.add(valve.label)
            result += self.release_pressure(time, pos, new_opened, set())

        visited = visited.copy()
        visited.add(valve.label)

        for tunnel in valve.tunnels:
            if tunnel not in visited:
                result = max(result, self.release_pressure(time, tunnel, opened, visited))

        return result

    def get_rate_distances(self, pos):
        to_visit = [(pos, 0)]
        visited = set()
        visited.add(pos)
        distances = []

        while to_visit:
            pos, dist = to_visit.pop(0)
            valve = self.all_valves[pos]
            if valve.rate and dist != 0:
                distances.append((valve.label, dist))
            for tunnel in valve.tunnels:
                if tunnel not in visited:
                    to_visit.append((tunnel, dist + 1))
                    visited.add(tunnel)
        return distances

    def make_rate_graph(self):
        for valve in self.rate_valves.values():
            visited = set()
            visited.add(valve.label)
            distances = self.get_rate_distances(valve.label)
            valve.rate_tunnels = distances

    def dump(self):
        for valve in self.rate_valves.values():
            print(valve.label, min(x[1] for x in valve.rate_tunnels))

    def calc_upper_bounds(self, max_time):
        min_distance = min(min(x[1] for x in self.rate_valves[valve.label].rate_tunnels) for valve in self.rate_valves.values())
        min_step = min_distance + 1
        print("min_distance:", min_distance)
        rates = [valve.rate for valve in self.rate_valves.values()]
        rates.sort(reverse=True)
        print("Rates:", rates)
        upper_bounds = []
        for time in range(max_time + 1):
            # print("Time:", time)
            total = 0
            for i in range(time//min_step):
                if i < len(rates):
                    total += rates[i] * (time - (min_step*(i+1)))
                    # print("i:", i, rates[i], time, (min_step*(i+1)), total)
            upper_bounds.append(total)
        return upper_bounds

valves = Valves([Valve(line) for line in open("test_input.txt")])
valves.make_rate_graph()
valves.dump()
distances = valves.get_rate_distances("AA")
print(distances)
upper_bounds = valves.calc_upper_bounds(30)
print(upper_bounds)
