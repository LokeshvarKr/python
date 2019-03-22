## Read input as specified in the question.
## Print output as specified in the question.
import queue
v,e=input().split(' ')
v,e=int(v),int(e)
edges=[[0 for x in range(v)] for y in range(v)]

for i in range(e):
  f,s=input().split(' ')
  f,s=int(f),int(s)
  edges[f][s]=1
  edges[s][f]=1

  
start,end=input().split(' ')
start,end=int(start),int(end)

def hasPath(edges,v,start,end,visited):
  q=queue.Queue(maxsize=v)
  q.put(start)
  visited[start]=1
  while q.empty():
    x=q.get()
    if(x is end):
      return True
    for i in range(v):
      if(i is not st and edges[st][i] is True and visited[i] is False):
        q.put(i)
        visited[i]=True
  
  return False


visited=[0 for i in range(v)]
result=hasPath(edges,v,start,end,visited)
if(result):
  print("true")
else:
  print("false")
