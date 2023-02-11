import io
import sys

_INPUT = """\
6
5 3
1 3 4
5 0

10 6
1 2 3 7 8 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  a=set(list(map(int,input().split())))
  ans=[]
  tmp=[]
  for i in range(N):
    if i+1 in a: tmp.append(i+1)
    else: tmp.append(i+1); ans+=tmp[::-1]; tmp=[]
  print(*ans)