

def nod(a, b):
    smallest = min(a, b)
    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return f'Наибольший общий делитель чисел, {a}, и, {b}, равен {i}'
    return f'Наибольший общий делитель чисел, {a}, и, {b}, не найден'


def logic(a):
    sum = 0
    total = 1

    while a != 0:
        sum += a % 10
        total *= a % 10
        a //= 10
    return sum == total


def summa(a):
    sum = 0
    while a != 0:
        sum += a % 10
        a //= 10
    return sum

