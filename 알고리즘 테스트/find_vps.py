import sys

input = sys.stdin.readline
N = int(input())
for n in range(N):
    s = input().rstrip()
    cnt = 0

    for i in s :
        if i == '(' :
            cnt += 1
        elif i == ')' :
            cnt -= 1
        if cnt < 0 :
            
            break
    if cnt != 0 :
        print('NO')
    else :
        print('YES')