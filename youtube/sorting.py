'''
https://youtu.be/KGyK-pNvWos?si=k4eAilOgR4lNzvxS
영상 학습 및 실습
'''

#두 배열의 원소 교체
def switchList():
    N, K = map(int,  input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    index = -1

    for i in range(K):
        a[i], b[index] = b[index], a[i]
        index -= 1
    return sum(a)

print(switchList())