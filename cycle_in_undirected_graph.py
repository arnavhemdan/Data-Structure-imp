from collections import deque

def cycle(node,vis,adj):
    q=deque()
    q.append((node,-1))
    vis[node]=1
    while q:
        node,parent=q.popleft()
        for i  in range(len(adj[node])):
            if parent== adj[node][i]:
                 continue
            if vis[adj[node][i]]:
                return 1
            if not vis[adj[node][i]]:
                vis[adj[node][i]]=1
                q.append((adj[node][i],node))
    return 0        

def main():
  v=int(input("enter no of vertices: "))
  e= int (input("eneter no of edges:")) 
  adj=[[] for _ in range (v)]
  print("enter vertice1: vertice2 ")
  for i in range(e):
    v1,e1=map(int,input().split())
    adj[v1].append(e1)
    adj[e1].append(v1)
   
  vis=[0]*v
  for i in range(v):
      if not vis[i] and cycle(i,vis,adj):
          return 1
  
  return 0    
        
x=main()  
if x==1:
    print("cycle")
else:
    print("no cycle")
        