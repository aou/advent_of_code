with open("./day_01_depths.txt", "rt") as f:
    depths_str = f.read()

depths = [int(depth) for depth in depths_str.split("\n") if depth.strip()]


def simple_measurement():

    prev = None
    num_increase = 0

    for depth in depths:
        if prev is None:
            prev = depth
            continue
        if depth > prev:
            num_increase += 1
        prev = depth


def three_measurement_window():

    buf = []
    prev = None
    cur = None
    num_increase = 0

    for depth in depths:

        buf.append(depth)

        if len(buf) < 4:
            continue
        prev = buf[-4] + buf[-3] + buf[-2]
        cur = buf[-3] + buf[-2] + buf[-1]

        if cur > prev:
            num_increase += 1

        buf = buf[1:]
