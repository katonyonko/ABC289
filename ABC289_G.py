import io
import sys

_INPUT = """\
6
5 4
100 200 300 400 500
120 370 470 80
4 4
0 2 10 2
13 13 0 4
12 15
16 592 222 983 729 338 747 61 451 815 838 281
406 319 305 519 317 590 507 946 365 5 673 478 340 176 2
5 5
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  deq = deque()
  def check(f1, f2, f3):
      return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
  def f(f1, x):
      return f1[0]*x + f1[1]

  # add f_i(x) = a*x + b
  def add_line(a, b):
      f1 = (a, b)
      while len(deq) >= 2 and check(deq[-2], deq[-1], f1):
          deq.pop()
      deq.append(f1)

  # min f_i(x)
  def query(x):
      while len(deq) >= 2 and f(deq[0], x) >= f(deq[1], x):
          deq.popleft()
      return f(deq[0], x)

  N,M=map(int,input().split())
  B=list(map(int,input().split()))
  C=list(map(int,input().split()))
  B.sort(reverse=True)
  C=sorted([(C[i],i) for i in range(M)])
  for i in range(N):
    add_line(-i-1,-(i+1)*B[i])
  ans=[-1]*M
  for i in range(M):
    p=query(C[i][0])
    ans[C[i][1]]=-p
  print(*ans)