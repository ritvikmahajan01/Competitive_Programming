# https://codeforces.com/contest/1475/problem/A

t = int(input())

def power_of_two(n):
    while n % 2 == 0:
        n //= 2
    return n == 1


for test_case in range(t):
    n = int(input())

    if n % 2 != 0:
        print("YES")
        continue
    else:
        if power_of_two(n):
            print("NO")
            continue
        else:
            print("YES")
            continue