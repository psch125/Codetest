import torch


# 모의고사
def solution(answers):
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    
    score = {1 : a,
              2 : b,
              3 : c}
    a, b, c = 0, 0, 0
    
    for i in range(len(answers)):
        if A[a] == answers[i]:
            score[1] += 1
        if B[b] == answers[i]:
            score[2] += 1
        if C[c] == answers[i]:
            score[3] += 1
            
        a += 1
        b += 1
        c += 1
        
        if a == len(A):
            a = 0
        if b == len(B):
            b = 0
        if c == len(C):
            c = 0 
            
    score = sorted(score.items(), key=lambda x:x[1], reverse=True) 
    max_value = max(score.values())
    answer = []
    for i in score:
        if i[1] == max_value:
            answer.append(i[0])
    return answer

# 삼각 달팽이
def solution(rows, columns, queries=None):
    array = [[0] * columns for i in range(rows)]  
    
    count = 0
    for i in range(rows):
        for j in range(columns):
            count += 1
            array[i][j] = count
    
    minimum_value = []
    for index in range(len(queries)):
        x1, y1, x2, y2 = queries[index][0]-1, queries[index][1]-1, queries[index][2]-1, queries[index][3]-1
        
        up_next_array = []
        up_next_index = []
        for i in range(y1, y2):
            up_next_array.append(array[x1][i])
            up_next_index.append((x1, i+1))
            
        right_next_array = []
        right_next_index = []
        for i in range(x1, x2):
            right_next_array.append(array[i][y2])
            right_next_index.append((i+1, y2))
            
        down_next_array = []
        down_next_index = []
        for i in range(y1+1, y2+1):
            down_next_array.append(array[x2][i])
            down_next_index.append((x2, i-1))
        
        left_next_array = []
        left_next_index = []
        for i in range(x1+1, x2+1):
            left_next_array.append(array[i][y1])
            left_next_index.append((i-1, y1))
            
        down_next_array = list(reversed(down_next_array))
        down_next_index = list(reversed(down_next_index))
        left_next_array = list(reversed(left_next_array))
        left_next_index = list(reversed(left_next_index))

        rotate_array = up_next_array+right_next_array+down_next_array+left_next_array
        rotate_index = up_next_index+right_next_index+down_next_index+left_next_index
        
        for i in range(len(rotate_array)):
            x, y = rotate_index[i]
            array[x][y] = rotate_array[i]
            
        minimum_value.append(min(rotate_array))
    return minimum_value


# 거리두기
def make_5X5(array):
    boxx = []
    for line in array:
        line_box = []
        for word in line:
            line_box.append(word)
        boxx.append(line_box)
    return boxx

def get_answer(bbox):
    for i in range(len(bbox)):
        for j in range(len(bbox[i])):
            # P 일때 확인
            if bbox[i][j] == 'P':
                # print(f'bbox[i][j] : {bbox[i][j]}, i : {i}, j : {j}')
                # 오른쪽의 경우
                if j+1 <= 4:
                    # print('오른쪽 공간 존재')
                    if bbox[i][j+1] == 'P':
                        return 0
                    # 맨해튼 거리가 2일 때
                    # 오른쪽 두 칸 확인
                    if j+2 <= 4:
                        if bbox[i][j+1] == 'O' and bbox[i][j+2] == 'P':
                            return 0
                    # 아래, 오른쪽 대각선 확인
                    if i+1 <= 4:
                        if bbox[i+1][j+1] == 'P':
                            if bbox[i+1][j] == 'O' or bbox[i][j+1] == 'O':
                                return 0         
                # 아래의 경우
                if i+1 <= 4:
                    # print('아래쪽 공간 존재')
                    if bbox[i+1][j] == 'P':
                        return 0
                    # 맨해튼 거리가 2
                    # 아래 쪽 두칸 확인
                    if i+2 <= 4:
                        if bbox[i+1][j] == 'O' and bbox[i+2][j] == 'P':
                            return 0
                        
                    # 아래 왼쪽 대각선 확인
                    if j-1 >= 0:
                        if bbox[i+1][j-1] == 'P':
                            if bbox[i+1][j] == 'O' or bbox[i][j-1] == 'O':
                                return 0
                # 왼쪽의 경우            
                if j-1 >= 0:
                    # print('왼쪽 공간 존재')
                    if bbox[i][j-1] == 'P':
                        return 0
                    # 맨해튼 거리가 2
                    # 왼쪽 두칸 확인
                    if j-2 >= 0:
                        if bbox[i][j-1] == 'O' and bbox[i][j-2] == 'P':
                            return 0
                        
                    # 위 왼쪽 대각선 확인
                    if i-1 >= 0:
                        if bbox[i-1][j-1] == 'P':
                            if bbox[i][j-1] == 'O' or bbox[i-1][j] == 'O':
                                return 0
                # 위쪽의 경우
                if i-1 >= 0:
                    # print('위쪽 공간 존재')
                    if bbox[i-1][j] == 'P':
                        return 0
                    # 맨해튼 거리가 2
                    # 위쪽 두칸 확인
                    if i-2 >= 0:
                        if bbox[i-1][j] == 'O' and bbox[i-2][j] == 'P':
                            return 0
                        
                    # 오른쪽 위 대각선 확인
                    if j+1 <= 4:
                        if bbox[i-1][j+1] == 'P':
                            if bbox[i][j+1] == 'O' or bbox[i-1][j] == 'O':
                                return 0           
    return 1
        
def solution(places): 
    answer = []
    for event in places:
        bbox = make_5X5(event)      
        # print('-'* 150)
        answer.append(get_answer(bbox))
    # print(answer)
    return answer