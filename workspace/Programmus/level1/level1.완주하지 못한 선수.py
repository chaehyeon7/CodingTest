import collections


# 'Collections'
# import collections
# collections에 내장된 함수인 Counter()는 Dic과 같이 hash형 자료들의 값의 개수를 셀 때 사용
# Dic처럼 {key:value} 형식으로 만들어짐
# Counter() 객체끼리 빼는 것도 가능
# 0 (zero) 나 음수 (minus)의 값들도 가능
# 해당하는 값이 없더라도 error가 아닌 0을 반환

# collections.Counter() 형식

def solution(participant, completion):
    participant.sort()
    completion.sort()
    result = collections.Counter(participant) - collections.Counter(completion)

    return list(result)[0]