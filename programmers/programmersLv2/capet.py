def solution(brown, yellow):
    sumCR = brown / 2 + 2
    mulCR = yellow - 4 + 2 * sumCR

    col = mulCR // 2
    while col > 0:
        if mulCR % col == 0:
            row = mulCR / col
            if sumCR == (col + row):
                return [col, row]
        col -= 1
