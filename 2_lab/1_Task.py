def f(x):
    if -2 <= x < 2:
        return x ** 2
    if x >= 2:
        return x ** 2 + 4 * x + 5
    if x < -2:
        return 4
x = int(input())
print(f(x))