def summa(a):
    sum = 0
    while a != 0:
        sum += a % 10
        a //= 10
    return sum
a = int(input())
print(summa(a))