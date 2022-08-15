
n = int(input().strip())
if n % 2 == 0 and n in range(1, 5):
    print('Not Weird')
elif n % 2 == 0 and n in range(5, 20):
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')