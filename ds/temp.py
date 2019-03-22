# code
from array import array
from math import sqrt

a = array('i', [1 for i in range(0, 405)])
a[0] = 0
a[1] = 0


def update_prime(x):
    i = x * x
    while i < 405:
        if a[i] == 1:
            a[i] = 0

        i += x


for i in range(2, int(sqrt(405))):
    if a[i] == 1:
        update_prime(i)

t = int(input())
while (t):
    t -= 1
    n = int(input())
    if n > 2:
        i = 2
        while i < (n // 2) + 1:
            if (a[i] == 1):
                j = 2
                while i * j <= n:
                    if a[j] == 1:
                        print(i, j, end=" ")
                    j += 1
            i += 1

    print()
