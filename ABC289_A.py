import io
import sys

_INPUT = """\
6
01
1011
100100001
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  s=input()
  print(''.join(['1' if s[i]=='0' else '0' for i in range(len(s))]))