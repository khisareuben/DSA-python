graph = {
  "a": ["b", "d"],
  "b": [],
  "c": [],
  "d": ["e","g"],
  "e": ["c"],
  "f": [],
  "g": ["f"]
  
}

def dfs(graph, source):
  stack = []
  stack.append(source)
  while stack:
    node = stack.pop(-1)
    print(node, end=" ")
    for neighbors in graph[node]:
      stack.append(neighbors)
  print()
      
def bfs(graph,src):
  que = []
  que.append(src)
  while que:
    node = que.pop(0)
    print(node, end=" ")
    for neighbors in graph[node]:
      que.append(neighbors)
      
    
dfs(graph, "a")
bfs(graph, "a")