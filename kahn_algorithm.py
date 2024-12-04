from collections import deque
def main():
  v=int(input("enter no of vertices: "))
  e= int (input("eneter no of edges:")) 
  adj=[[] for _ in range (v)]
  print("enter vertice1: vertice2 ")
  for i in range(e):
    v1,e1=map(int,input().split())
    adj[v1].append(e1)   
  vis=[0]*v
  ind=[0]*v
  for i in range(v):
      for j in range(len(adj[i])):
          ind[adj[i][j]]+=1
  q=deque()
  for i in range(v):
      if not ind[i]:
          q.append(i)
  ans=[]
  while q:
      node=q.popleft()
      ans.append(node)
      for i in range(len(adj[node])):
          ind[adj[node][i]]-=1
          if ind[adj[node][i]]==0:
              q.append(adj[node][i])
  print(ans)            
          
main()                          