def solution(number):
    count = 0
    for i in range(1, number + 1):  # 1부터 number까지
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            current = current // 10  # 10으로 나누어 while 문 안에서 돌도록
    return count

# 테스트
number = 40
ret = solution(number)
print("solution 함수의 반환 값은", ret, "입니다.")