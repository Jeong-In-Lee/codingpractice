import sys
import heapq

N = int(sys.stdin.readline())
h = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0 and len(h) == 0:
        # sys.stdout.write(0)
        print(0)
    elif num == 0:
        print(-1 * heapq.heappop(h))
    else:
        heapq.heappush(h, -1 * num)
