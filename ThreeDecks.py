t = int(input())


for test_case in range(t):
    a, b, c = map(int, input().split())

    if ((a+b+c) % 3 != 0):
        print("NO")
        continue
    else:
        avg = (a+b+c) // 3

        if (avg < a or avg < b):
            print("NO")
            continue
        else:
            add_a = avg - a
            add_b = avg - b
            sub_c = c - avg
            if (add_a + add_b != sub_c):
                print("NO")
                continue
            else:
                print("YES")
                continue



