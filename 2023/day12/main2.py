def process_pattern(pattern, sizes, cache):
    if not sizes:
        return 0 if "#" in pattern else 1

    if not pattern:
        return 0

    cache_hit = cache.get((len(pattern), len(sizes)))
    if cache_hit is not None:
        return cache_hit

    result = 0
    if pattern[0] in ("#", "?"):
        curr_size = sizes[0]
        if len(pattern) >= curr_size and all(
            c in ("#", "?") for c in pattern[:curr_size]
        ):
            if len(pattern) == curr_size:
                result = 1 if len(sizes) == 1 else 0
            else:
                next_char = pattern[curr_size]
                result = (
                    0
                    if next_char == "#"
                    else process_pattern(pattern[curr_size + 1 :], sizes[1:], cache)
                )
        else:
            result = 0

    if pattern[0] in (".", "?"):
        result += process_pattern(pattern[1:], sizes, cache)

    cache[(len(pattern), len(sizes))] = result
    return result


def process_line(line):
    pattern, hit_sizes = line.split()
    hit_sizes = [int(size) for size in hit_sizes.split(",")]
    is_part_2 = True
    if is_part_2:
        multiple = 5
        pattern = "?".join(multiple * [pattern])
        hit_sizes = multiple * hit_sizes
    cache = {}
    return process_pattern(pattern, hit_sizes, cache)


print(sum(process_line(line.strip()) for line in open("input.txt")))
