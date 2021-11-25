import sys
s = sys.stdin.readlines()
for i in range(len(s)):
	s[i]=s[i].strip()
j=0
for row in range(0,len(s)):
	if "1" in (s[row]):
		for n in s[row].split():
			if n=="1":
				break
			else:
				j+=1
		break
print(abs(j-2)+abs(row-2))