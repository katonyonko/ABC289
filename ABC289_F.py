import io
import sys

_INPUT = """\
6
1 2
7 8
7 9 0 3
0 0
8 4
5 5 0 0
1 4
1 4
100 200 300 400
22 2
16 7
14 30 11 14
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  sx,sy=map(int,input().split())
  tx,ty=map(int,input().split())
  a,b,c,d=map(int,input().split())
  flg=0
  x,y=tx-sx,ty-sy
  if x%2==0 and y%2==0:
    x,y=x//2,y//2
    if (x==0 or a!=b) and (y==0 or c!=d):
      ans1=[]
      ans2=[]
      if x>0:
        for i in range(x): ans1.append(a); ans1.append(a+1)
      elif x<0:
        for i in range(-x): ans1.append(a+1); ans1.append(a)
      if y>0:
        for i in range(y): ans2.append(c); ans2.append(c+1)
      elif y<0:
        for i in range(-y): ans2.append(c+1); ans2.append(c)
      ans=[]
      for i in range(max(len(ans1),len(ans2))):
        if i>=len(ans1): ans.append((a,ans2[i]))
        elif i>=len(ans2): ans.append((ans1[i],c))
        else: ans.append((ans1[i],ans2[i]))
      print('Yes')
      for i in range(len(ans)):
        print(*ans[i])
      flg=1
  x,y=tx+sx,ty+sy
  if flg==0 and x%2==0 and y%2==0:
    x,y=x//2,y//2
    flg2=0
    if x==0 or a!=b:
      ans1=[a]
      for i in range(a): ans1.append(a+1); ans1.append(a)
      if x>0:
        for i in range(x): ans1.append(a); ans1.append(a+1)
      elif x<0:
        for i in range(-x): ans1.append(a+1); ans1.append(a)
    elif x==a:
      ans1=[a]
    else: flg2=1
    if y==0 or c!=d:
      ans2=[c]
      for i in range(c): ans2.append(c+1); ans2.append(c)
      if y>0:
        for i in range(y): ans2.append(c); ans2.append(c+1)
      elif y<0:
        for i in range(-y): ans2.append(c+1); ans2.append(c)
    elif y==c:
      ans2=[c]
    else: flg2=1
    if flg2==0:
      ans=[]
      for i in range(max(len(ans1),len(ans2))):
        if i>=len(ans1): ans.append((a,ans2[i]))
        elif i>=len(ans2): ans.append((ans1[i],c))
        else: ans.append((ans1[i],ans2[i]))
      print('Yes')
      for i in range(len(ans)):
        print(*ans[i])
      flg=1
  if flg==0: print('No')