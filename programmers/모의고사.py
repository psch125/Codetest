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