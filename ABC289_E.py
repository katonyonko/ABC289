import io
import sys

_INPUT = """\
6
3
4 4
0 1 0 1
1 2
2 3
1 3
2 4
3 3
0 1 0
1 2
2 3
1 3
6 6
0 0 1 1 0 1
1 2
2 6
3 6
4 6
4 5
2 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  T=int(input())
  for _ in range(T):
    inf=10**10
    N,M=map(int,input().split())
    C=list(map(int,input().split()))
    G=[[] for i in range(N)]
    for i in range(M):
      u,v=map(lambda x: int(x)-1, input().split())
      G[u].append(v)
      G[v].append(u)
    D=[inf]*(N**2)
    D[N-1]=0
    dq=deque()
    dq.append(N-1)
    while dq:
      x=dq.popleft()
      i,j=x//N,x%N
      for u in G[i]:
        for v in G[j]:
          if C[u]!=C[v] and D[u*N+v]>D[x]+1:
            D[u*N+v]=D[x]+1
            dq.append(u*N+v)
    if D[(N-1)*N]<10**10: print(D[(N-1)*N])
    else: print(-1)