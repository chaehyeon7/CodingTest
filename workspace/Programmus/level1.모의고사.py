def solution(answers):
    # 찍는방식 정의
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 맞힌 갯수 정의
    count_a, count_b, count_c = 0, 0, 0
    answer = []

    # 정답의 갯수만큼 for문을 돌린다.
    for i in range(0, len(answers)):
        # 찍는 방식의 문제번호가 갯수를 넘었을때 처음부터 같은방식으로 찍기위해
        # 문제 번호를 찍는방식의 갯수만큼 나누고 나머지를 찾는다.
        if answers[i] == a[i % len(a)]:
            count_a += 1
        if answers[i] == b[i % len(b)]:
            count_b += 1
        if answers[i] == c[i % len(c)]:
            count_c += 1

    max_count = max(count_a, count_b, count_c)
    # 문제를 가장 많이 맞춘사람을 찾기위해 if문을 사용한다.
    # 동점자가 있을수도 있기때문에 elif문이 아닌 if를 세번 사용한다.
    if max_count == count_a:
        answer.append(1)
    if max_count == count_b:
        answer.append(2)
    if max_count == count_c:
        answer.append(3)

    return answer