from collections import deque


def solution(maps):
    m = len(maps[0])
    n = len(maps)
    depth = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        if depth <= maps[y][x]:
            depth += 1
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if newX < 0 or newY < 0 or newX >= m or newY >= n:
                continue
            if maps[newY][newX] == 1:
                queue.append((newX, newY))
                maps[newY][newX] = depth
                if newX == (m - 1) and newY == (n - 1):
                    return depth
    return -1
