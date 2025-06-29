# https://codeforces.com/contest/2117/problem/A

t = int(input())

for test_case in range(t):

    n, x = map(int, input().split())

    a = list(map(int, input().split()))

    first_closed = -1

    last_closed = n

    for room in range(len(a)):
        if a[room] == 1 and first_closed == -1:
            first_closed = room

        if a[n - 1 - room] == 1 and last_closed == n:
            last_closed = n - 1 - room
        
        if first_closed != 0 and last_closed != n:
            continue

    print("yes" if x > (last_closed - first_closed) else "no")
    # print(first_closed, last_closed)
