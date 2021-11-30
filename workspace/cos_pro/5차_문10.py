def solution(time_table, n):
    answer = 0
    for i in range(n):
        x = 0
        for j in range(len(time_table)):
            if j % n == i:
                x += time_table[j]
            if answer < x:
                answer = x
    return answer

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")