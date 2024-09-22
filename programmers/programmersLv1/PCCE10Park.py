def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    for mat in mats:
        if answer != -1:
            break
        for i in range(len(park)):
            if len(park) - i < mat:
                break
            for j in range(len(park[i])):
                if len(park[i]) - j < mat:
                    break
                if park[i][j] == "-1":
                    flag = False
                    for k in range(mat):
                        for l in range(mat):
                            if park[i + k][j + l] != "-1":
                                flag = True
                            if flag == True:
                                break
                        if flag == True:
                            break
                    if flag == False:
                        answer = mat

    return answer
