def global_all(A,B):
	M=[[0]*(len(B)+1) for i in range(len(A)+1)]
	for i in range(len(M[0])):
		M[0][i]= -2 * i
	for i in range(len(M)):
		M[i][0]= -2 * i
	for i in range(1,len(M)):
		for j in range(1,len(M[0])):
			if A[i-1]==B[j-1]:
				score = 1
			else:
				score = -1
			d = M[i-1][j-1] + score
			o = M[i][j-1] - 2
			v = M[i-1][j] - 2
			M[i][j]=max(d,o,v)
	for i in range(len(M)):
		print(M[i])

global_all("ATCCAATTTT","ATGGCCATT")

def local_all(A,B):
	M=[[0]*(len(B)+1) for i in range(len(A)+1)]
	for i in range(1,len(M)):
		for j in range(1,len(M[0])):
			if A[i-1]==B[j-1]:
				score = 1
			else:
				score = -1
			d = M[i-1][j-1] + score
			o = M[i][j-1] - 2
			v = M[i-1][j] - 2
			M[i][j]=max(d,o,v,0)
	for i in range(len(M)):
		print(M[i])


#local_all("BGCA","AGC")


def semiglobal_all(A,B):
	M=[[0]*(len(B)+1) for i in range(len(A)+1)]
	for i in range(1,len(M)):
		for j in range(1,len(M[0])):
			if A[i-1]==B[j-1]:
				score = 1
			else:
				score = -1
			d = M[i-1][j-1] + score
			o = M[i][j-1] - 2
			v = M[i-1][j] - 2
			M[i][j]=max(d,o,v)
	print(M)
