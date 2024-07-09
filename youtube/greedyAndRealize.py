'''
https://youtu.be/2zjoKjt97vQ?si=U6H3lZd1J3EJE84p
영상 학습 및 실습
'''


# Greedy : 곱하기 혹은 더하기 문제 - O(n) (n=사람 수)
def multOrAdd():
    numbers = list(map(int, input()))
    result = 0
    for num in numbers:
        if num <= 1 or result<=1:
            result+=num
        else:
            result*=num
    return result
    
# print(multOrAdd())


# Greedy : 모험가 길드 문제 - O(nlog n) (n = 모험가 수)
def adventurer():
    N = int(input())
    fear = list(input().split())
    fear = list(map(int, fear))
    fear.sort()
    result = 0
    group = []

    for p in fear:
        group.append(p)
        if p <= len(group):
            result +=1
            group = []
    
    return result

# print(adventurer())

# 구현 : 상하좌우 문제 - O(d) - d = 입력된 이동 수
def LRUD():
    N = int(input())
    directions = list(str(input().split()))
    pos = [0,0]

    for d in directions:
        if d == 'L' and pos[1] != 0:
            pos[1] -=1
        elif d == 'R' and pos[1] != N-1:
            pos[1] +=1
        elif d == 'U' and pos[0] != 0:
            pos[0] -= 1
        elif d == 'D' and pos[0] != N-1:
            pos[0] += 1
        else:
            pass
    
    print(pos[0]+1, pos[1]+1)

# LRUD()

# 구현 : 시각 - O(N)
def numOf3():
    N = int(input())
    result =0
    for i in range(N+1):
        if str(i).find('3') == -1:
            result += (6*10*6*10 - 5*9*5*9) #전체 개수에서 3 없는거 빼기
        else:
            result += (6*10*6*10) #N에 3이 포함된 경우 모든 경우 더하기
    return result

# print(numOf3())


#구현 : 왕실의 나이트 - O(1)
def knight():
    pos = str(input())
    count = 0
    dx = [2, 2, -2, -2, 1, 1, -1, -1] # 열 움직임
    dy = [1, -1, 1, -1, 2, -2, 2, -2] # 행 움직임

    for i in range(len(dx)):
        x = ord(pos[0]) - ord('a')
        y = ord(pos[1]) - ord('1')
        moveX = x + dx[i]
        moveY = y + dy[i]
        if (moveX >=0 and moveX <=7 and moveY>=0 and moveY<=7):
            count+=1
        
    return count

# print(knight())

#구현 : 문자열 재정렬 - O(n) n은 문자열 길이
def reSort():
    S = str(input())
    word = []
    num = 0

    for w in S:
        if ord(w) >= ord('A') and ord(w) <= ord('Z'):
            word.append(w)
        else:
            num += (ord(w) - ord('0'))
    word.sort()

    if num != 0:
        result = ''.join(word) + str(num)
    else:
        result = ''.join(word)

    return result

# print(reSort())
