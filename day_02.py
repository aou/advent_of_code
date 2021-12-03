with open("./day_02_movements.txt", "rt") as f:
    moves_str = f.read()

moves = [move.strip() for move in moves_str.split("\n") if move.strip()]


def problem_one():

    x = 0
    z = 0

    for move in moves:
        direction, distance = move.split(" ")
        distance = int(distance)
        if direction == "forward":
            x += distance
        elif direction == "up":
            z -= distance
        elif direction == "down":
            z += distance
        else:
            raise ValueError(f"unknown direction {direction}")

    result = x * z


def problem_two():
    x = 0
    z = 0
    aim = 0

    for move in moves:
        direction, distance = move.split(" ")
        distance = int(distance)
        if direction == "forward":
            x += distance
            z += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
        else:
            raise ValueError(f"unknown direction {direction}")

    result = x * z
