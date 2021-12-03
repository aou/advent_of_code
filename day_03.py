with open("./day_03_input.txt", "rt") as f:
    nums_str = f.read()

nums = [int(num.strip(), 2) for num in nums_str.split("\n") if num.strip()]


def problem_one():
    gamma = 0
    epsilon = 0
    for i in range(12):
        bits = list(map(lambda x: (x >> i) & 1, nums))
        ones = len([x for x in bits if x == 1])
        zeros = 1000 - ones

        assert ones != zeros

        if ones > zeros:
            x = 1
            y = 0
        else:
            x = 0
            y = 1

        gamma += x << i
        epsilon += y << i

        return gamma * epsilon


def problem_two():
    o2_nums = nums

    for i in range(11, -1, -1):
        bits = list(map(lambda x: (x >> i) & 1, o2_nums))
        ones = len([x for x in bits if x == 1])
        zeros = len(bits) - ones

        if ones >= zeros:
            x = 1
        else:
            x = 0

        o2_nums = [o2_num for o2_num in o2_nums if (o2_num >> i) & 1 == x]

        if len(o2_nums) == 1:
            break

    co2_nums = nums

    for i in range(11, -1, -1):
        bits = list(map(lambda x: (x >> i) & 1, co2_nums))
        ones = len([x for x in bits if x == 1])
        zeros = len(bits) - ones

        if ones >= zeros:
            x = 0
        else:
            x = 1

        co2_nums = [co2_num for co2_num in co2_nums if (co2_num >> i) & 1 == x]

        if len(co2_nums) == 1:
            break

    return o2_nums[0] * co2_nums[0]
