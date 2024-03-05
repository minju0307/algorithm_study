def solution(triangle):
    dp = triangle[-1][:] ## dp 테이블 초기화 (삼각형의 맨 마지막 줄)
    print(dp)
    
    depth = len(triangle) - 1 ## 삼각형의 마지막에서 두번째줄부터 시작
    
    for d in reversed(range(depth)):
        print(f"***{d}***")
        for idx in range(len(triangle[-1])):
            print(f"idx: {idx}, num: {triangle[-1][idx]}")
            print(triangle[d])
            if idx > 0 and idx <= d:
                dp[idx] += max(triangle[d][idx-1], triangle[d][idx])
            elif idx == 0 :
                dp[idx] += triangle[d][idx]
            else:
                dp[idx] += triangle[d][idx-1]
    
    answer = max(dp)
    return answer

if __name__ =='__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))