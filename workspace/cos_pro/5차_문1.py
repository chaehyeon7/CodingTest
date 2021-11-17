def solution(ladders, win):
    answer = 0
    player = [1, 2, 3, 4, 5, 6]
    for e in ladders:
        # 가로줄 타기 전 위치와 타고 난 이후 위치를 바꾸어 저장하기
        temp = player[e[0]-1]  # 가로줄 타기 전 위치
        player[e[0] - 1] = player[e[1] - 1]  # 바꾸어 저장
        player[e[1] - 1] = temp  # 가로줄 타고 나서의 위치
    answer = player[win-1]
    return answer

# 테스트
ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)
print("solution 함수의 반환 값은", ret, "입니다.")
