def solution(triangle):
    
    for depth, line in enumerate(triangle):
        if depth == 0:
            continue
        for idx in range(len(line)):
            if idx > 0 and idx < len(line)-1:
                line[idx] += max(triangle[depth-1][idx-1], triangle[depth-1][idx])
            elif idx == 0:
                line[idx] += triangle[depth-1][idx]
            else:
                line[idx] += triangle[depth-1][idx-1]
    
    answer = max(triangle[-1])
    return answer

if __name__ =='__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))