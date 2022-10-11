# 행렬을 회전시키기전 그곳에 있는 가장 작은 숫자를 찾아서 answer에 삽입
# 왼쪽 상단부터 시계방향으로 돌면서 한칸씩 미루어 배열에 담기

def solution(rows, columns, queries):
    answer = []

    matrix = []

    num = 1
    # rows*columns 행렬 생성
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(num)
            num+=1
        matrix.append(row)

    # 회전을 적용하면서
    # 최솟값 찾고
    # 시계방향으로 1칸씩 미루기
    for query in queries:
        x1 = query[0]-1
        y1 = query[1]-1
        x2 = query[2]-1
        y2 = query[3]-1

        rotate = []
        
        for i in range(y1,y2):
            rotate.append(matrix[x1][i])
        for i in range(x1,x2):                
            rotate.append(matrix[i][y2])
        for i in range(y2,y1,-1):
            rotate.append(matrix[x2][i])
        for i in range(x2,x1,-1):
            rotate.append(matrix[i][y1])

        rotate.insert(0,rotate.pop())
        count = 0
        answer.append(min(rotate))

        for i in range(y1,y2):
            matrix[x1][i] = rotate[count]
            count+=1
        for i in range(x1,x2):                
            matrix[i][y2] = rotate[count]
            count+=1
        for i in range(y2,y1,-1):
            matrix[x2][i] = rotate[count]
            count+=1
        for i in range(x2,x1,-1):
            matrix[i][y1] = rotate[count]
            count+=1

    return answer

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))