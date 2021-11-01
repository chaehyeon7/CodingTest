def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s < 800:  # 범위 변경
            count += 1
    return count

# 테스트
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 880]
ret = solution(scores)
print("solution 함수의 반환 값은", ret, "입니다.")

