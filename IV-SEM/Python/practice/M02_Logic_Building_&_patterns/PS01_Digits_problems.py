'''n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

n = int(input())

while n > 0:
    s = n % 10
    if s % 2 == 0:
        print(s, end=" ")
    n = n // 10


n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)


n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)
'''
n = int(input())
temp = reversed(n)