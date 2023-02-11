import io
import sys

_INPUT = """\
6
3
3 4 5
4
4 5 6 8
15
4
2 3 4 5
4
3 4 5 6
8
4
2 5 7 8
5
2 9 10 11 19
20
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  M=int(input())
  B=set(map(int,input().split()))
  X=int(input())
  dp=[0]*(X+1)
  dp[0]=1
  for i in range(X):
    if dp[i]==1:
      for j in range(N):
        if i+A[j]<=X and i+A[j] not in B: dp[i+A[j]]=1
  if dp[-1]==1: print('Yes')
  else: print('No')