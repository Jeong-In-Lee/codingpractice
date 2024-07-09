def solution(s):
    num = list(map(int, s.split()))
    num.sort()
    answer = str(num[0]) + ' ' + str(num[len(num)-1])
    return answer