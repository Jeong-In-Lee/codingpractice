def solution(friends, gifts):
    # 주고 받은 선물을 이차원 리스트로 표기
    graph = [[0] * len(friends) for i in range(len(friends))]
    for s in gifts:
        temp = s.split()
        sender = friends.index(temp[0])
        receiver = friends.index(temp[1])
        graph[sender][receiver] += 1

    # 선물지수 구하기
    presentValue = []
    for person in friends:
        sendNum = 0
        receiveNum = 0
        for i in range(len(friends)):
            if i != friends.index(person):
                sendNum += graph[friends.index(person)][i]
                receiveNum += graph[i][friends.index(person)]
        presentValue.append(sendNum - receiveNum)

    # 최고 값 구하기
    best = 0
    for person in friends:
        now = 0
        for i in range(len(friends)):
            if i != friends.index(person):
                if graph[friends.index(person)][i] > graph[i][friends.index(person)]:
                    now += 1
                elif graph[friends.index(person)][i] == graph[i][friends.index(person)]:
                    if presentValue[friends.index(person)] > presentValue[i]:
                        now += 1
                    else:
                        continue
                else:
                    continue
        if now > best:
            best = now
    return best
