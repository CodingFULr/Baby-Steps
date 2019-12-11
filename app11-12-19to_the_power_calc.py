
def to_the_power(base_num, power):
    base = 1
    for index in range(power):
        base = base * base_num
    return base

print(to_the_power(10, 9))