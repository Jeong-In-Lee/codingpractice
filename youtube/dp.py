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
        dp[i] = dp[i - 1] + 1

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
        N, M = map(int, input().split())
        temp = list(map(int, input().split()))
        d = [temp[i : i + M] for i in range(0, len(temp), M)]
        dSum = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            dSum[i][0] = d[i][0]

        for col in range(1, M):
            for row in range(N):
                if row == 0:
                    dSum[row][col] = (
                        max(
                            dSum[row][col - 1],
                            dSum[row + 1][col - 1],
                        )
                        + d[row][col]
                    )
                elif row == (N - 1):
                    dSum[row][col] = (
                        max(
                            dSum[row - 1][col - 1],
                            dSum[row][col - 1],
                        )
                        + d[row][col]
                    )
                else:
                    dSum[row][col] = (
                        max(
                            dSum[row - 1][col - 1],
                            dSum[row][col - 1],
                            dSum[row + 1][col - 1],
                        )
                        + d[row][col]
                    )
        answer = 0
        for m in range(N):
            answer = max(answer, dSum[m][M - 1])
        print(answer)


# goldGang()


def subSodier(new):
    before = new[0]
    count = 0
    for i in range(1, len(new)):
        if before <= new[i]:
            count += 1
        else:
            before = new[i]
    return count


def soldier():
    N = int(input())
    people = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    index = []

    dp[N - 1] = N - 1
    for i in range(N - 2, -1, -1):
        new = people[i:]
        newN = len(new)
        for num in index:
            del new[newN - num]
        if dp[i + 1] > (subSodier(new) + i + len(index)):
            dp[i] = subSodier(new) + i + len(index)
        else:
            dp[i] = dp[i + 1]
            index.append(N - i)
        print(f"index : {index} // dp[{i}] : {dp[i]} // new : {new}")

    return dp[0]


def answerSoldier():
    N = int(input())
    people = list(map(int, input().split()))

    people.reverse()

    dp = [1 for _ in range(N)]

    for i in range(1, N):
        for j in range(0, i):
            if people[j] < people[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)


# print(soldier())
