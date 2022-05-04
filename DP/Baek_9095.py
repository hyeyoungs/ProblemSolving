def get_methods_num(N):
    dp = [0] * (N + 1)
    dp[0] = 0
    if N >= 1:
        dp[1] = 1
    if N >= 2:
        dp[2] = 2
    if N >= 3:
        dp[3] = 4

    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[N]


test_case = int(input())
for _ in range(test_case):
    N = int(input())
    print(get_methods_num(N))
