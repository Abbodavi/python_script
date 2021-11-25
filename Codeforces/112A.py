import sys
s = sys.stdin.readlines()
for i in range(len(s)):
	s[i]=s[i].strip().lower()
if s[0]>s[1]:
	print("1")
elif s[0]<s[1]:
	print("-1")
else:
	print("0")