def block_check(m,n,board):
    sustainable=0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]==None or board[i+1][j]==None or board[i + 1][j+1]==None or board[i][j+1]==None:
                # print(i,j,board[i][j]==None,board[i+1][j]==None)
                pass
            else:
                check=[]
                # print(board[i][j])
                check.append(board[i][j].lower() == board[i][j + 1].lower())
                check.append(board[i][j].lower() == board[i + 1][j].lower())
                check.append(board[i][j].lower() == board[i + 1][j + 1].lower())
                if sum(check)==3:
                    sustainable=1
                    board[i][j] = board[i][j].lower()
                    board[i][j+1] = board[i][j+1].lower()
                    board[i+1][j] = board[i+1][j].lower()
                    board[i+1][j+1] = board[i+1][j+1].lower()
    return board, sustainable

def score_check(m, n, b,score):
    for i in range(m):
        for j in range(n):
            if b[i][j]==None:
                pass
            elif (b[i][j].islower())==True:
                score+=1
                b[i][j]=None

    return score,b

def solution(m, n, board):
    score = 0

    # str to list
    b = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append((board[i][j]))
        b.append(temp)

    while True:
        # 4 block check
        b,sustainable = block_check(m, n, b)
        p(b)
        score,b=score_check(m,n,b,score)

        if not sustainable:
            break

        for i in range(n):
            for j in range(m-1,-1,-1):
                temp=b[j][i]
                if temp==None:
                    for k in range(j,-1,-1):
                        if b[k][i]==None:
                            pass
                        else:
                            b[j][i]=b[k][i]
                            b[k][i]=None
                            break
    return score
