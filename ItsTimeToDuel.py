# https://codeforces.com/problemset/problem/2109/A

t = int(input())

for test_case in range(t):
    false = 0
    n = int(input())
    a_list = list(map(int, input().split()))

    if sum(a_list) == 0 or sum(a_list) >= n:
        print("yes")
        continue

    for i in range(n-1):
        if a_list[i] == 0 and a_list[i+1] == 0:
            print("yes")
            false = 1
            break
    
    if false == 0:
        print("no")

