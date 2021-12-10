def solution(cards):
    answer = 0 #총합 더할 곳
    c = [0,0,0]
    for i in cards:
        answer += int(i[1]) #총합은 더해놓고 c에 색깔 세는 공간 저장
        if i[0] == "blue" : c[0]+= 1    #정해놓은 색이 나오면 1씩 증가
        elif i[0] == "red" : c[1]+= 1
        else: c[2] += 1
    answer = answer * max(c[0], c[1], c[2])     # 그 중에 가장 큰 수로 종합 곱하기

    return answer

cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)

print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)

print("solution 함수의 반환 값은", ret2, "입니다.")