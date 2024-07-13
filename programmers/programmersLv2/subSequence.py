"""

# BF - 시간초과로 실패

def solution(sequence, k):
    for i in range(1, len(sequence)+1): # i는 부분 수열의 숫자 개수
        s = 0
        for j in range(len(sequence)-i+1): #i에 해당하는 부분 수열 수
            if sum(sequence[s:s+i])==k: #j+1이 초과되긴 하지만 문제 없음
                answer = [s,s+i-1]
                return answer
            s+=1

"""

"""
# 시간 초과 ^^
def solution(sequence, k):
    N = len(sequence)
    answer= []
    for i in range(1, N+1): # i는 부분 수열의 숫자 개수
        if sum(sequence[-i:])<k:
            continue
        else:
            for j in range(N-i+1): #i에 해당하는 부분 수열 수
                if sum(sequence[N-j-1-i:N-j-1])==k: #j+1이 초과되긴 하지만 문제 없음
                    answer = [N-j-1-i,N-j-2]
            return answer
"""


"""
#어떻게 이게 시간초과?
# 절반씩 나눠서 탐색해보자.
def solution(sequence, k):
    N = len(sequence)
    for i in range(1, N+1): # i는 부분 수열의 숫자 개수
        if sum(sequence[-i:])<k:
            continue
        else:
            p = N // 2
            while True:
                if sum(sequence[p:p+i])==k:
                    temp = sequence.index(sequence[p])
                    if sum(sequence[temp:temp+i])==k:
                        return [temp, temp+i-1]
                    else:
                        return [p, p+i-1]
                elif sum(sequence[p:p+i])>k:
                    p = p //2
                else:
                    p = (N-p)//2 + p
                
    return answer
"""


# 슬라이딩 윈도우 기법
def solution(sequence, k):
    N = len(sequence)
    left = 0
    right = 0
    sum = 0
    answer = []
    while left != N:
        if sum == k:
            if len(answer) == 0:
                answer = [left, right - 1]
            else:
                if (answer[1] - answer[0]) > (right - left - 1):
                    answer = [left, right - 1]
        elif sum > k:
            sum -= sequence[left]
            left += 1
            continue
        else:
            pass

        if right == N:
            sum -= sequence[left]
            left += 1
        else:
            sum += sequence[right]
            right += 1

    return answer
