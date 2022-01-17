def condition1(u, u1, eps):
    max = abs(u[0] - u1[0])

    for i in range(1, len(u)):
        if abs(u[i] - u1[i]) >= max:
            max = abs(u[i] - u1[i])

    if max > eps:
        return True

    return False


def condition2(u, u1, eps):
    sum = 0

    for i in range(len(u)):
        sum += abs(u[i] - u1[i])

    if sum > eps:
        return True

    return False


def condition3(u, u1, eps):
    norm = 0

    for i in range(len(u)):
        norm += float(u[i] - u1[i]) ** 2

    if norm ** 0.5 > eps:
        return True

    return False


def condition4(u, u1, eps):
    norm = 0

    for i in range(len(u)):
        norm += float(u[i] - u1[i]) ** 4

    if norm ** 0.25 > eps:
        return True

    return False
