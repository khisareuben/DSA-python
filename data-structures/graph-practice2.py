'''
this is an undirected graph
you can go forward as well as backwards
'''


graph = {
	"a" : ["b", "c"],
	"b" : ["a", "f", "d"],
	"c" : ["a"],
	"d" : ["b", "g", "i"],
	"e" : ["f", "h"],
	"f" : ["b", "e"],
	"g" : ["d", "h"],
	"h" : ["e", "g"],
	"i" : ["d"]
}


def has_path(src, dst, graph, visited):
  if src == dst:
    return True
  visited.add(src)
  ans = True
  for neighbors in graph[src]:
    if neighbors not in visited:
      ans = ans or has_path(src, dst, graph, visited)
  return ans

visited = set()
src = input("Enter source: ")
dst = input("Enter destination: ")
print(has_path(src, dst, graph, visited))
print()

