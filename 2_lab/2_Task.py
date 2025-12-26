def nod(a, b):
    smallest = min(a, b)
    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
a, b = int(input()), int(input())
print('Наибольший общий делитель чисел', a, 'и', b, 'равен', nod(a, b))