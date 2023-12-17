def hash(input):
    v = 0
    for c in input:
        v = ((v + ord(c)) * 17) % 256
    return v


def add_to_box(content, label, lens):
    for i, v in enumerate(content):
        if v[0] == label:
            content[i] = (label, lens)
            return
    content.append((label, lens))


boxes = [[] for i in range(256)]


def as_str(boxes):
    return "\n".join(f"[Box {i}: " + str(box) for i, box in enumerate(boxes) if box)


for line in open("input.txt").readline().strip().split(","):
    if "-" in line:
        label, _ = line.split("-")
        box = hash(label)
        boxes[box] = [v for v in boxes[box] if v[0] != label]
    else:
        label, lens = line.split("=")
        box = hash(label)
        add_to_box(boxes[box], label, int(lens))

print(
    sum(
        i * sum(box_id * t[1] for box_id, t in enumerate(box, 1))
        for i, box in enumerate(boxes, 1)
    )
)
