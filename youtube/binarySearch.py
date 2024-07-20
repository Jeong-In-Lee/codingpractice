"""
https://youtu.be/94RC-DsGMLo?si=OXCDGtJns0pFlGN8
영상 학습 및 실습
"""


# 떡볶이 떡 만들기
def binarySearch(d, M, start, end, bestH):
    if end < start:
        return None
    mid = (start + end) // 2
    sum = 0

    for i in range(len(d)):
        sub = d[i] - mid
        if sub > 0:
            sum += sub

    if sum >= M:
        bestH.append(mid)
        return binarySearch(d, M, mid + 1, end, bestH)
    else:
        return binarySearch(d, M, start, mid - 1, bestH)


import time


def ddeok():
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    startTime = time.time()
    d.sort()  # 필수 아님!
    bestH = []

    binarySearch(d, M, 0, d[-1], bestH)

    return [max(bestH), startTime]


# r = ddeok()
# print(r[0])
# endTime = time.time()
# print("걸린시간", endTime - r[1])


# 특정 수의 개수 구하기 - O(logn) 이여야 함
from bisect import bisect_left, bisect_right


def particularNum():
    N, x = map(int, input().split())
    num = list(map(int, input().split()))
    start = bisect_left(num, x)
    end = bisect_right(num, x)
    if start == end:
        return -1
    else:
        return end - start


print(particularNum())
