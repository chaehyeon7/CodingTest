def solution(data):
    avg = sum(data) / len(data)
    cnt = 0

    for i in data:
        if i <= avg:
            cnt += 1

    return cnt


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = solution(data)

print(answer)

data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
answer = solution(data)

print(answer)