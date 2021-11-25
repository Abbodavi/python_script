s=input()
s=s.split("+")
for i in range(1,len(s)):
	j=i
	while True:
		if s[j]<s[j-1] and j>0:
			temp=s[j-1]
			s[j-1]=s[j]
			s[j]=temp
		else:
			break
		j=j-1
print("+".join(s))
