total_time = 26


class Valve:
    def __init__(self, line):
        parts = line.strip().split()
        self.label = parts[1]
        self.rate = int(parts[4][5:-1])
        self.tunnels = [part.removesuffix(",") for part in parts[9:]]
        self.was_visited = [False, False]
        self.is_open = False


class Valves:
    def __init__(self, valves):
        self.all_valves = dict((valve.label, valve) for valve in valves)
        self.rate_valves = dict((valve.label, valve) for valve in valves if valve.rate)

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
            distances = self.get_rate_distances(valve.label)
            valve.rate_tunnels = distances

    def calc_upper_bounds(self, max_time):
        min_distance = min(
            min(x[1] for x in self.rate_valves[valve.label].rate_tunnels)
            for valve in self.rate_valves.values()
        )
        min_step = min_distance + 1
        rates = [valve.rate for valve in self.rate_valves.values()]
        rates.sort(reverse=True)
        upper_bounds = []
        for time in range(max_time + 1):
            total = 0
            for i in range(time // min_step):
                if i < len(rates):
                    total += rates[i] * (time - (min_step * (i + 1)))
            upper_bounds.append(total)
        return upper_bounds

    def search(self, pos_pair, time_pair, total=0):
        global best
        if upper_bounds[time_pair[0]] + upper_bounds[time_pair[1]] + total < best:
            return

        moving_id = 0 if time_pair[0] >= time_pair[1] else 1
        pos = pos_pair[moving_id]
        time = time_pair[moving_id]

        if time <= 1:
            if total > best:
                best = total
            return

        curr_valve = self.rate_valves[pos]
        if curr_valve.was_visited[moving_id]:
            return
        curr_valve.was_visited[moving_id] = True

        old_is_open = curr_valve.is_open
        if not curr_valve.is_open:
            time -= 1
            total += curr_valve.rate * time
            if total > best:
                best = total
            curr_valve.is_open = True
        for neighbour, dist in curr_valve.rate_tunnels:
            if moving_id == 0:
                new_pos_pair = (neighbour, pos_pair[1])
                new_time_pair = (time - dist, time_pair[1])
            else:
                new_pos_pair = (pos_pair[0], neighbour)
                new_time_pair = (time_pair[0], time - dist)
            self.search(new_pos_pair, new_time_pair, total)
        curr_valve.was_visited[moving_id] = False
        curr_valve.is_open = old_is_open


valves = Valves([Valve(line) for line in open("input.txt")])
valves.make_rate_graph()
start_distances = valves.get_rate_distances("AA")
upper_bounds = valves.calc_upper_bounds(total_time)
best = 0
for start_pos_a, start_dist_a in start_distances:
    for start_pos_b, start_dist_b in start_distances:
        if start_pos_a <= start_pos_b:
            valves.search(
                (start_pos_a, start_pos_b),
                (total_time - start_dist_a, total_time - start_dist_b),
            )
print(best)
