def solution(s):
    listS = list(s)
    num = [0, 0]
    answer = 0
    x = "X"

    for s in listS:
        if x == "X":
            x = s
            num[0] += 1
            continue
        if s != x:
            num[1] += 1
            if num[0] == num[1]:
                x = "X"
                answer += 1
                num[0] = 0
                num[1] = 0
        else:
            num[0] += 1

    if num[0] != 0 or num[1] != 0:
        answer += 1
    return answer
