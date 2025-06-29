# https://codeforces.com/contest/2121/problem/B

t = int(input())

for test_case in range(t):

    n = int(input())

    s = input()

    

    for i in range(1, len(s)-1):
        a = s[0:i]
        b = s[i]
        c = s[i+1:]

        # print(a, b, c)


        if b in a or b in c:
            print("yes")
            break

    else:
        print("no")
        