#graph data structure basis input and traversal methods

#using depth for search
from collections import deque

def dfs(node,vis,result):
     vis[node]=1
     result.append(node)
     for i in range(len(adj[node])):
         if not vis[adj[node][i]]:
             dfs(adj[node][i],vis,result)
     
#using  breadth for search
def bfs(adj,v,result2):
    visted=[0]*v
    q=deque()
    q.append(0)
    visted[0]=1
    while len(q):
        node=q.popleft()
        result2.append(node)
        for i in range (len(adj[node])):
            if not visted[adj[node][i]]:
                q.append(adj[node][i])
                visted[adj[node][i]]=1
                
                
#main starts here
if __name__=="__main__":
    v=int(input("enter no of vertiecs "))
    u=int(input("enter no of edges "))
    
#creaating a adjency list 
    adj=[[] for _ in range (v)]
    print("eneter vertices1 to vertice2 in manner v1 v2")
    for i in range(u):
        #both for undirected graph
        v1,u1=map(int,input().split())
        adj[v1].append(u1)
        adj[u1].append(v1)
    print(adj)
    # call for dfs
    result=[] 
    vis=[0] *v
    #loop for discoonected graph  
    for i in range (v): 
        if not vis[i]:
            dfs(i,vis,result)
    print(result)
    #call for bfs
    result2=[]
    bfs(adj,v,result2)
    print(result2)

