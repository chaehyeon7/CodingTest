def mon(m):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]    # 인덱스번호와 월을 맞추기 위해서 days[0]에는 0을 넣어주었어요.
    num = 0
    for i in range(m):    # 월에 해당하는 인덱스전까지 모두 더해줄거에요. 2월은 days[1]까지 값이 더해지겠지요.
        num += days[i]
    return num

def solution(sm, sd, em, ed):
    s_cnt = mon(sm) + sd    # 1단계 : sm 이전달 까지 더한 값에 sm월의 일수를 더해줍니다.
    e_cnt = mon(em) + ed    # 2단계
    return e_cnt - s_cnt    # 3단계

start_month = 1
start_day = 2
end_month = 2
end_day = 2
answer = solution(start_month, start_day, end_month, end_day)

print(start_month,"월", start_day,"일과 ", end_month,"월",end_day,"일은 ", answer,"일 만큼 떨어져 있습니다")
