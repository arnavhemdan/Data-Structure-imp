import heapq

def main():
  v=int(input("enter no of vertices: "))
  e= int (input("eneter no of edges:")) 
  adj=[[] for _ in range (v)]
  print("enter vertice1: vertice2 : weight")
  for i in range(e):
    v1,e1,w1=map(int,input().split())
    adj[v1].append((e1,w1))   
  #logic
  dis=[float('inf')]*v
  heap=[]
  src=int(input("enter the source node "))
  dis[src]=0  
  vis=[0]*v 
  heapq.heappush(heap,(0,src))
  while heap:
      curr_dis,node=heapq.heappop(heap)
      if vis[node]:
          continue
      vis[node]=1
      for i in range(len(adj[node])):
          ne=adj[node][i][0]
          we=adj[node][i][1]
          if  dis[ne]>we+curr_dis:
               dis[ne]=we+curr_dis
               heapq.heappush(heap,(dis[ne],ne)) 
  print(dis)              
main()                          