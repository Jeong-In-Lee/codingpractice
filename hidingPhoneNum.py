def solution(phone_number):
    answer = ""

    for i in range(len(phone_number)):
        left = len(phone_number) - i
        if left <= 4:
            answer = answer + phone_number[i:]
            break
        answer = answer + "*"

    return answer
