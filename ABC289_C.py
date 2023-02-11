import io
import sys

_INPUT = """\
6
3 3
2
1 2
2
1 3
1
2
4 2
2
1 2
2
1 3
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import combinations
  N,M=map(int,input().split())
  s=[]
  ans=0
  for _ in range(M):
    C=int(input())
    a=list(map(int,input().split()))
    a=sum([1<<(a[i]-1) for i in range(C)])
    s.append(a)
  for c in range(2**M):
    if c==0: continue
    p=0
    for i in range(M):
      if (c>>i)&1==1: p|=s[i]
    if p==2**N-1: ans+=1
  print(ans)