def solution(height):
    count = 0
    for x in range(4):  # 0~3 인덱스 반복
        for y in range(4):  # 0~3 인덱스 반복
            # [x][y]가 위쪽보다 크면 pass
            if x > 0 and height[x-1][y] < height[x][y]:
                pass
            # [x][y]가 아래쪽보다 크면 pass
            elif x < 3 and height[x+1][y] < height[x][y]:
                pass
            # [x][y]가 왼쪽보다 크면 pass
            elif y > 0 and height[x][y-1] < height[x][y]:
                pass
            # [x][y]가 오른쪽보다 크면 pass
            elif y < 3 and height[x][y+1] < height[x][y]:
                pass
            # 조건을 만족하지 못하고 작은 경우, count가 1 증가
            else:
                count += 1
    return count

# 테스트
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)
print("solution 함수의 반환 값은", ret, "입니다.")