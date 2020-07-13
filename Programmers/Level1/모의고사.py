def solution(answers):
    data = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    sol = [0] * 3
    for i in range(len(data)):
        tmp = len(answers) // len(data) + 1
        data[i] *= tmp
        
        for j in range(len(answers)):
            if answers[j] == data[i][j]:
                sol[i] += 1
    res = []
    cnt = max(sol)
    for i in range(len(sol)):
        if cnt == sol[i]:
            res.append(sol.index(sol[i])+1)
            sol[i] = 0
                    
    return res

    # 1
    answers = [1,2,3,4,5]
    # 2
    answers = [1,3,2,4,2]