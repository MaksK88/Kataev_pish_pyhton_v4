n = int(input())
if n <= 100:
      for i in range(1, n + 1):
          print(i, i ** 2, i ** 3)
else:  
     print('Число больше 100')