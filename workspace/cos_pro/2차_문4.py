def solution(words):
    answer = ''
    for i in words:
        if len(i) >= 5:
            answer += i
    if answer == '':
        answer = 'empty'
    return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

print("solution 함수의 반환 값은", ret2, "입니다.")