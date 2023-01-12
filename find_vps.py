import sys
input = sys.stdin.readline
N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))
A_dic = {i : 1 for i in A_list}

for i in range(M):
    print(A_dic.get(B_list[i], 0))