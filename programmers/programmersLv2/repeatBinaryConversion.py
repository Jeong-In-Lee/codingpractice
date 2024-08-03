def solution(s):
    answer = [0, 0]
    while s != "1":
        one = s.count("1")
        answer[0] += 1
        answer[1] += len(s) - one
        s = format(one, "b")
    return answer
