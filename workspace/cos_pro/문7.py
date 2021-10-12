def solution(sentence):
    tmp = ""

    for i in range(len(sentence)):
        if sentence[i] != " " and sentence[i] != ".":
            tmp += sentence[i]

    for i in range(len(tmp)):
        if tmp[i] == tmp[len(tmp) - 1 - i]:
            return True
        else:
            return False


sentence = "never odd or even."
answer = solution(sentence)

print(answer)