def initBoard(N, board, pos):
    for i in range(N):
        for j in range(N):
            if board[i][j] == ".":
                board[i][j] = int(0)
            else:
                pos.append((i, j))


def setBoard(N, board, pos):
    for i, j in pos:
        # 벽 확인해서 숫자 벽 생성
        if i != 0 and j != 0 and board[i - 1][j - 1] != "*":
            board[i - 1][j - 1] += 1
        if i != 0 and board[i - 1][j] != "*":
            board[i - 1][j] += 1
        if i != 0 and j != N - 1 and board[i - 1][j + 1] != "*":
            board[i - 1][j + 1] += 1
        if j != 0 and board[i][j - 1] != "*":
            board[i][j - 1] += 1
        if j != N - 1 and board[i][j + 1] != "*":
            board[i][j + 1] += 1
        if i != N - 1 and j != 0 and board[i + 1][j - 1] != "*":
            board[i + 1][j - 1] += 1
        if i != N - 1 and board[i + 1][j] != "*":
            board[i + 1][j] += 1
        if i != N - 1 and j != N - 1 and board[i + 1][j + 1] != "*":
            board[i + 1][j + 1] += 1


def makeBox(N, i, j, count, newBoard):
    if i != 0 and j != 0:
        newBoard[i - 1][j - 1] = count
    if i != 0:
        newBoard[i - 1][j] = count
    if i != 0 and j != N - 1:
        newBoard[i - 1][j + 1] = count
    if j != 0:
        newBoard[i][j - 1] = count
    newBoard[i][j] = count
    if j != N - 1:
        newBoard[i][j + 1] = count
    if i != N - 1 and j != 0:
        newBoard[i + 1][j - 1] = count
    if i != N - 1:
        newBoard[i + 1][j] = count
    if i != N - 1 and j != N - 1:
        newBoard[i + 1][j + 1] = count


def checkNewBoard(N, i, j, count, newBoard) -> int:
    if newBoard[i][j] == 0:  # 자신이 속한 상자 존재x -> 새로 상자 생성 및 전파
        count += 1
        makeBox(N, i, j, count, newBoard)
    else:  # 자신이 속한 상자 존재 -> 8방향으로 전파
        makeBox(N, i, j, int(newBoard[i][j]), newBoard)
    return count


def minNum(N, board, pos) -> int:
    count = 0
    # new의 0은 자신의 상자(집합)이 정의되지 않은 것임.
    newBoard = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count = checkNewBoard(N, i, j, count, newBoard)

    for i in range(N):
        count += newBoard[i].count(0)

    count -= len(pos)
    return count


T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    pos = []
    board = [list(input()) for _ in range(N)]

    initBoard(N, board, pos)
    setBoard(N, board, pos)
    # for i in range(N):
    #     print(board[i])

    result = minNum(N, board, pos)

    print(f"#{test_case} {result}")
