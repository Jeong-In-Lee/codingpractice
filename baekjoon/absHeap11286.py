import sys
import heapq

N = int(sys.stdin.readline())
minH = []  # 양수 전용
maxH = []  # 음수 전용

for i in range(N):
    num = int(sys.stdin.readline())
    if num < 0:
        heapq.heappush(maxH, -1 * num)
    elif num > 0:
        heapq.heappush(minH, num)
    else:
        if len(minH) == 0 and len(maxH) == 0:
            print(0)
        elif len(minH) == 0:
            print(-1 * heapq.heappop(maxH))
        elif len(maxH) == 0:
            print(heapq.heappop(minH))
        else:
            left = maxH[0]
            right = minH[0]
            if left < right:
                print(-1 * heapq.heappop(maxH))
            elif left == right:
                print(-1 * heapq.heappop(maxH))
            else:
                print(heapq.heappop(minH))
