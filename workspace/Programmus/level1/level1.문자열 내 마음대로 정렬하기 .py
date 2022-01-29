def solution(strings, n):
    n_answer = []

    for string in strings:
        n_answer.append(string[n] + string)

    n_answer.sort()
    answer = []

    for i in n_answer:
        answer.append(i[1:])
    return answer