# 유클리드 호재법 GCD
def gcd(a, b) -> int:
    if (max(a, b) % min(a, b)) == 0:
        return min(a, b)
    else:
        return gcd((max(a, b) % min(a, b)), min(a, b))


# print(gcd(192, 162))

# 음료수 얼려먹기 - O(NMp) p = 0의 개수 // DFS로 품. (quece 이용)
from collections import deque


def iceCreamNum():
    N = int(input())
    M = int(input())
    ice = [list(map(int, input())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    count = 0

    for i in range(N):
        for j in range(M):
            if ice[i][j] == 0:
                count += 1
                ice[i][j] = 10
                queue.append((i, j))

                while len(queue) != 0:
                    newI, newJ = map(int, queue.popleft())
                    for m in range(4):
                        x = newI + dx[m]
                        y = newJ + dy[m]
                        if x >= N or x < 0 or y < 0 or y >= M:
                            continue
                        if ice[x][y] == 0:
                            queue.append((x, y))
                            ice[x][y] = 10
    return count


print(iceCreamNum())
