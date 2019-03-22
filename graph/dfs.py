from array import *

def printgraph(edges,v,start,visited):
	print(start)
	visited[start]=True
	for i in range(v):
		if(i is not start and edges[start][i] is not False and visited[i] is not True):
			printgraph(edges,v,i,visited)
		



v=int(input("No. of vertices: "))
e=int(input("No. of edges: "))
edges=[[False for x in range(v)] for x in range(v)]
for i in range(e):
	f,s=input("enter edge {} : ".format(i),).split()
	f,s=int(f),int(s)
	edges[f][s]=True
	edges[s][f]=True

visited=[False for x in range(v)]
printgraph(edges,v,0,visited)