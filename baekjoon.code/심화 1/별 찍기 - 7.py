n = int(input())

for i in range(n):
    for k in range(n-i-1):
        print(' ', end='')
    for j in range(i*2 + 1):
        print('*', end='')
    print()
for i in range(n):
    for k in range(i+1):
        print(' ', end='')
    for j in range((n*2-1) - (i+1)*2):
        print('*', end='')
    print()
