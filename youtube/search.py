'''
https://youtu.be/7C9RgOcvkvo?si=awRQ9v_2emGyVw4P
영상 학습 및 실습
'''

# 유클리드 호재법 GCD
def gcd(a, b) -> int:
    if (max(a, b) % min(a, b)) == 0:
        return min(a, b)
    else:
        return gcd((max(a, b) % min(a, b)), min(a, b))


# print(gcd(192, 162))

# 음료수 얼려먹기 - O(NMp) p = 0의 개수 // BFS로 품. (quece 이용)
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


# print(iceCreamNum())

'''
#영상 코드 dfs (graph, n ,m는 원래 파라미터로 안받음 but 내 코드는 다 함수로 만든거라 파라미터로 제공함)
def dfs(x,y, graph, n ,m):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y]==0:
        graph[x][y] = 1
        dfs(x-1, y, graph, n ,m)
        dfs(x, y-1, graph, n ,m)
        dfs(x+1, y, graph, n ,m)
        dfs(x, y+1, graph, n ,m)
        return True
    return False

def mainDFS():
    n, m = map(int, input().split())
    graph=[]
    for i in range(n):
        graph.append(list(map(int, input())))

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result+=1
    return result
'''



# 미로탈출
def mazeEscape():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N, M = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(N)]
    queue = deque()
    count = 0
    flag = True
    maze[0][0] = 9
    queue.append((0,0))

    while flag:
        flagInside = False
        x, y = map(int, queue.popleft())
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if newX <0 or newY <0 or newX>=N or newY>=M:
                continue
            if maze[newX][newY] ==1:
                queue.append((newX,newY))
                maze[newX][newY]=9
                flagInside = True
            if newX==(N-1) and newY==(M-1):
                flag = False
                break
        if flagInside:
            count+=1

    return count+1

# print(mazeEscape())

'''
#교재 코드
def bfs(x,y, n, m, graph):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x,y))\

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx <0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if graph[nx][ny] ==0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

def mainBFS():
    n, m = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(N)]
    print(bfs(0,0, n, m, graph))
            
'''