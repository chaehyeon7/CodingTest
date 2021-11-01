def func_a(scores, score):  # 같은 점수 찾기
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def func_b(arr):  # 내림차순 정리
    arr.sort(reverse=True)

def func_c(arr, n):  # n번 값 저장
    return arr[n]

def solution(scores, n):
    score = func_c(scores, n)
    func_b(scores)
    answer = func_a(scores, score)
    return answer

# 테스트
scores = [20, 60, 98, 59]
n = 3
ret = solution(scores, n)
print("solution 함수의 반환 값은", ret, "입니다.")