import re
def solution(dartResult):
    cnt=[0,0,0]
    p=re.compile("(\d*\D{1}\W?|\d*\D{1}\W?)")
    m=p.findall(dartResult)
    for i in range(len(m)):

        if m[i][1]=='S' or (m[i][1]=='0' and m[i][2]=='S'):
            if m[i][0] == '1' and m[i][1] == '0':
                cnt[i] = 10
            else:
                cnt[i]=int(m[i][0])

        elif m[i][1]=='D'or (m[i][1]=='0' and m[i][2]=='D'):
            if m[i][0] == '1' and m[i][1] == '0':
                cnt[i] = 100
            else:
                cnt[i]=pow(int(m[i][0]),2)
        elif m[i][1]=='T'or (m[i][1]=='0' and m[i][2]=='T'):
            if m[i][0] == '1' and m[i][1] == '0':
                cnt[i] = 1000
            else:
                cnt[i]=pow(int(m[i][0]),3)

        if 3<=len(m[i]):
            print(m[i])
            if m[i][-1]=='#':
                cnt[i]=cnt[i]*(-1)
            elif m[i][-1]=='*':
                for j in range(i-1,i+1):
                    cnt[j]=cnt[j]*2

    return sum(cnt)