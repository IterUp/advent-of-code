resource_names = ("ore", "clay", "obsidian", "geode")


def make_cost(input):
    cost, resource = input.split()
    return resource, int(cost)


class Rule:
    def __init__(self, description):
        split = description[6:].split(" robot costs ")
        resource_name, costs_strings = split
        self.robot_type = resource_names.index(resource_name)
        costs = dict(make_cost(cost) for cost in costs_strings.split(" and "))
        self.costs = tuple(costs.get(resource, 0) for resource in resource_names)

    def make_robot(self, robots):
        return tuple(
            num_robots + (self.robot_type == i) for i, num_robots in enumerate(robots)
        )

    def build(self, resources):
        return (
            tuple(r - c for r, c in zip(resources, self.costs))
            if all(r >= c for r, c in zip(resources, self.costs))
            else None
        )


class Blueprint:
    def __init__(self, line):
        _, line = line.split(":")
        rules = line.split(".")[:-1]
        self.rules = [Rule(rule) for rule in rules]
        self.max_costs = [max(rule.costs[i] for rule in self.rules) for i in range(4)]
        self.max_costs[-1] = 24**2
        self.cache = {}
        self.best = 0

    def next_steps(self, robots, resources):
        for rule in self.rules:
            if robots[rule.robot_type] < self.max_costs[rule.robot_type]:
                resources_after_build = rule.build(resources)
                if resources_after_build is not None:
                    new_resources = tuple(
                        x + y for x, y in zip(robots, resources_after_build)
                    )
                    yield rule.make_robot(robots), new_resources

        new_resources = tuple(x + y for x, y in zip(robots, resources))
        yield robots, new_resources

    def _get_num_geodes(self, cache, num_cycles, robots, resources, path):
        hit = cache.get((num_cycles, robots, resources))
        if hit is not None:
            return hit

        if num_cycles == 0:
            result = resources[-1]
            cache[(num_cycles, resources)] = result
            if result > self.best:
                self.best = result
                print(f"Best: {result=}")

            return result

        day = f"Minute {24-num_cycles}:"
        result = max(
            self._get_num_geodes(
                cache,
                num_cycles - 1,
                next_robots,
                next_resources,
                path + ((day, robots, resources),),
            )
            for next_robots, next_resources in self.next_steps(robots, resources)
        )
        cache[(num_cycles, robots, resources)] = result
        return result

    def get_num_geodes(self):
        cache = {}
        result = self._get_num_geodes(cache, 24, (1, 0, 0, 0), (0, 0, 0, 0), ())
        print("Blueprint:", result)
        return result


blueprints = [Blueprint(line) for line in open("input.txt")]
print(sum(blueprint.get_num_geodes() * i for i, blueprint in enumerate(blueprints, 1)))
