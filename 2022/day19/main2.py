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
    def __init__(self, line, num_cycles):
        _, line = line.split(":")
        rules = line.split(".")[:-1]
        self.rules = [Rule(rule) for rule in rules]
        self.max_costs = [max(rule.costs[i] for rule in self.rules) for i in range(4)]
        self.max_costs[-1] = num_cycles**2
        self.cache = {}
        self.best = 0
        self.num_cycles = num_cycles

    def next_steps(self, robots, resources):
        for rule in self.rules:
            if robots[rule.robot_type] < self.max_costs[rule.robot_type]:
                resources_after_build = rule.build(resources)
                if resources_after_build is not None:
                    new_resources = tuple(
                        x + y for x, y in zip(robots, resources_after_build)
                    )
                    yield rule.make_robot(robots), new_resources

        new_resources = tuple(
            min(x + y, max_cost) if x == max_cost else x + y
            for max_cost, x, y in zip(self.max_costs, robots, resources)
        )
        yield robots, new_resources

    def _get_num_geodes(self, cache, remaining_cycles, robots, resources):
        hit = cache.get((remaining_cycles, robots, resources))
        if hit is not None:
            return hit

        geode_robots = robots[-1]
        upper_bound = (
            resources[-1]
            + (2 * geode_robots + remaining_cycles - 1) * remaining_cycles // 2
        )

        if upper_bound <= self.best:
            # print(f"{upper_bound=} {self.best
            cache[(remaining_cycles, robots, resources)] = 0
            return 0

        if remaining_cycles == 0:
            result = resources[-1]
            if result > self.best:
                self.best = result
                print(f"Best: {result=}")

            return result

        result = max(
            self._get_num_geodes(
                cache, remaining_cycles - 1, next_robots, next_resources
            )
            for next_robots, next_resources in self.next_steps(robots, resources)
        )
        cache[(remaining_cycles, robots, resources)] = result
        return result

    def get_num_geodes(self):
        cache = {}
        return self._get_num_geodes(cache, self.num_cycles, (1, 0, 0, 0), (0, 0, 0, 0))


blueprints = [Blueprint(line, 32) for line in open("input.txt")]
import math

print(math.prod(blueprint.get_num_geodes() for blueprint in blueprints[:3]))
