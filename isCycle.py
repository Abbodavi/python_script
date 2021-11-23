node=["A","B","C","D","E","F"]
edge=["AB","BD","DE","AC","BC","AF","EA"]

def adjmatrix(node,edge):
	adj={}
	for n in node:
		linked=[]
		for e in edge:
			if n==e[0]:
				linked.append(e[1])
		adj[n]= linked
	return adj

def BFS(node,adjmatrix,start,):
	explored={}
	for i in node:
		explored[i]=False
	Queue=[]
	Queue.append(start)
	i=0
	while len(Queue):
		i+=1
		examined=Queue.pop(0)
		for element in adjmatrix[examined]:
			if explored[element]==False:
				Queue.append(element)
				explored[element]=True
	if explored[start]==True:
		return True

for n in node:
	res=BFS(node,adjmatrix(node,edge),n)
	if res==True:
		print("There is at least a cycle")
		break