def solution(storey):
    answer = 0
    sStorey = str(storey)
    while storey > 0:
        if int(sStorey[len(sStorey) - 1]) > 5:
            answer += 10 - int(sStorey[len(sStorey) - 1])
            storey += 10 - int(sStorey[len(sStorey) - 1])
            storey //= 10
            sStorey = str(storey)
        elif int(sStorey[len(sStorey) - 1]) == 5:
            if len(sStorey) == 1 or int(sStorey[len(sStorey) - 2]) < 5:
                answer += int(sStorey[len(sStorey) - 1])
                storey -= int(sStorey[len(sStorey) - 1])
                storey //= 10
                sStorey = str(storey)
            else:
                answer += 10 - int(sStorey[len(sStorey) - 1])
                storey += 10 - int(sStorey[len(sStorey) - 1])
                storey //= 10
                sStorey = str(storey)
        else:
            answer += int(sStorey[len(sStorey) - 1])
            storey -= int(sStorey[len(sStorey) - 1])
            storey //= 10
            sStorey = str(storey)
    return answer
