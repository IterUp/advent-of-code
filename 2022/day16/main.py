class Valve:
    def __init__(self, line):
        parts = line.strip().split()
        self.label = parts[1]
        self.rate = int(parts[4][5:-1])
        self.tunnels = [part.removesuffix(',') for part in parts[9:]]
        self.was_visited = False

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
            print(f"Label {valve.label}: {valve.rate} {valve.rate_tunnels}")

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

    def search(self, pos, time, upper_bounds, total = 0, path = ()):
        global best
        # print("search", time, total, best)
        time -= 1
        if time <= 0:
            if total > best:
                print("Best:", total, path)
                print([v.label for v in self.rate_valves.values() if v.was_visited])
                best = total
            return
        curr_valve = self.rate_valves[pos]
        if curr_valve.was_visited:
            return
        total += curr_valve.rate * time
        path = path + ((pos, time, curr_valve.rate),)
        curr_valve.was_visited = True
        for neighbour, dist in curr_valve.rate_tunnels:
            self.search(neighbour, time - dist, upper_bounds, total, path)
        curr_valve.was_visited = False

valves = Valves([Valve(line) for line in open("input.txt")])
valves.make_rate_graph()
valves.dump()
start_distances = valves.get_rate_distances("AA")
print("start_distances:", start_distances)
upper_bounds = valves.calc_upper_bounds(30)
print(upper_bounds)
best = 0
for start_pos, start_dist in start_distances:
	valves.search(start_pos, 30 - start_dist, upper_bounds)
