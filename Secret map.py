def solution(n, arr1, arr2):
    answer = []
    temp=[]
    temp2=[]

    for i in range(n):
        temp.insert(i,list(bin(arr1[i])[2:]))
        if len(temp[i]) < n:
            diff=n-len(temp[i])
            for _ in range(diff):
                temp[i].insert(0, '0')
    for i in range(n):
        temp2.insert(i,list(bin(arr2[i])[2:]))
        if len(temp2[i]) < n:
            diff=n-len(temp2[i])
            for _ in range(diff):
                temp2[i].insert(0, '0')

    for i in range(n):

        str = ''
        for j in range(n):
            if temp[i][j]=='1' or temp2[i][j]=='1':
                str=str+'#'
            else:
                str=str+' '

        answer.insert(i,str)
    return answer