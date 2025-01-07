'''
this is to check if a path exists between the source and destination
you  can say its like google map :)
'''

graph = {
	"a" : ["b", "c"],
	"b" : ["f", "d"],
	"c" : [],
	"d" : ["g", "i"],
	"e" : ["h"],
	"f" : ["e"],
	"g" : ["h"],
	"h" : [],
	"i" : []
}

def has_path(src, dst, graph):
	if src == dst:
		return True
	ans = False
	for neighbours in graph[src]:
		ans = ans or has_path(neighbours, dst, graph)

	return ans

src = input("Enter the source: ")
dst = input("Enter the destination: ")
print(has_path(src, dst, graph))

