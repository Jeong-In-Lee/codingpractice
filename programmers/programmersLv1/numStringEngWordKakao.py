def solution(s):
    answer = ""
    numS = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    while s:
        flag = True

        for num in numS:
            if s[: len(num)] == num:
                answer = answer + str(numS.index(num))
                s = s[len(num) :]
                flag = False
                break

        if s != "" and flag:
            answer = answer + str(s[0])
            s = s[1:]

    return int(answer)
