def solution(arr, max_n, min_n):
    cnt_arr = [0 for _ in range(1001)]
    answer = 0

    for i in arr:
        cnt_arr[i] += 1

    answer = cnt_arr[max_n] // cnt_arr[min_n]

    return answer


arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
max_num = max(arr)  # 염쌤은 리스트의 내장함수인 max와 min 함수를 사용했어요.
min_num = min(arr)
answer = solution(arr, max_num, min_num)

print(max_num, "이", min_num, "보다 ", answer, "배 많이 들어있다.")