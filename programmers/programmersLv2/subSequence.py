'''

# BF - 시간초과로 실패

def solution(sequence, k):
    for i in range(1, len(sequence)+1): # i는 부분 수열의 숫자 개수
        s = 0
        for j in range(len(sequence)-i+1): #i에 해당하는 부분 수열 수
            if sum(sequence[s:s+i])==k: #j+1이 초과되긴 하지만 문제 없음
                answer = [s,s+i-1]
                return answer
            s+=1

'''
#고쳐야함
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