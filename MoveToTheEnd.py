t = int(input())


for test_case in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    suffix_sums = [0] * (n)
    for i in range(n-1, -1, -1):
        if i == n-1:
            suffix_sums[i] = a[i]
        else:
            suffix_sums[i] = a[i] + suffix_sums[i+1]

    max_elements = [0] * n
    max_elements[0] = a[0]

    for i in range(1, n):
        max_elements[i] = max(a[i], max_elements[i-1])
        if i == n-1:
            max_elements[i] = 0

    for k in range(n):
        # print("Currnt k:", k, "Max elements:", max_elements[n-k-2], "Suffix sums:", suffix_sums[n-k-1], "Suffix_sum_-1", (suffix_sums[n-k] if k > 0 else 0))

        max_sum = max(suffix_sums[n-k-1], max_elements[n-k-2] + (suffix_sums[n-k] if k > 0 else 0))
        print(max_sum, end=" ")

    print()

    