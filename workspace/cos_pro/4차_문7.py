def func_a(scores1, scores2):  # 최댓값 구하기
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer

def func_b(scores1, scores2):  # 최솟값 구하기
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score1 - score2)  # 문제에서 순서를 변경하여 훼이크를 줌
    return answer

# 아래 함수 내에서 수정
def solution(mid_scores, final_scores):
    up = func_a(mid_scores, final_scores)
    down = func_b(final_scores, mid_scores)
    answer = [up, down]
    return answer

# 테스트
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)
print("solution 함수의 반환 값은", ret, "입니다.")