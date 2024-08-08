"""
https://youtu.be/5Lu34WIx2Us?si=JGks0ENMBt0-FIZj
영상 학습 및 실습
"""


def antFood():
    N = int(input())
    food = list(map(int, input().split()))
    dp = [0]
    dp.append(food[0])

    for i in range(1, N):
        dp.append(max(dp[i], (dp[i - 1] + food[i])))
    return dp.pop()


# print(antFood())


def makeOne():
    X = int(input())
    dp = [0 for _ in range(X + 1)]

    for i in range(2, X + 1):
        dp[i] = d[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)


# print(makeOne())


def efficientMoney():
    N, M = map(int, input().split())
    coins = []
    for i in range(N):
        coins.append(int(input()))
    d = [20000 for _ in range(11000)]

    count = 0
    d[0] = count
    for index in range(M + 1):
        if d[index] == 20000:
            continue
        count = d[index] + 1
        for coin in coins:
            d[index + coin] = min(count, d[index + coin])

    if d[M] == 20000:
        return -1
    return d[M]


# print(efficientMoney())


def goldGang():
    T = int(input())
    for testcase in range(T):
        N, M = map(int, input().slit())
        temp = list(map(int, input().split()))
        d = [temp[i : i + M] for i in range(0, len(temp), M)]
