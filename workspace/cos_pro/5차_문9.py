def solution(score):
    answer = [1] * len(score)  # score 길이 만큼의 리스트 만들기
    # 한 숫자와 나머지 숫자를 모두 비교하기 위해서 for 반복문을 2번 사용
    for i in range(len(score)):
        for j in range(len(score)):
            if score[i] < score[j]:  # 나보다 큰 숫자가 나올 때 마다 (1부터) 1씩 증가
                answer[i] += 1
    return answer


score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

print("solution 함수의 반환 값은", ret1, "입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

print("solution 함수의 반환 값은", ret2, "입니다.")