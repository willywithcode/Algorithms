
import sys
sys.setrecursionlimit(50000)
from collections import defaultdict


class Graph:
	def __init__(self,vertices,Virtices):
		self.V = vertices
		self.graph = defaultdict(list)
		self.Virtices = Virtices


	def addEdges(self,u,v):
		self.graph[u].append(v)


	def DFSUntil(self, v, visited):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUntil(i,visited)
		
		
	

	def fillOrder(self,v,visited,stack) :
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.fillOrder(i,visited,stack)
		stack = stack.append(v)



	def Transpose(self):
		gr = Graph(self.V,self.Virtices)
		for i in self.graph:
			for j in self.graph[i]:
				gr.addEdges(j,i)
		return gr
	

	def SCCs(self) :
		sum = 0
		stack = []
		visited = [False]*(self.V)
		for i in self.Virtices:
			if visited[i] ==False:
				self.fillOrder(i,visited,stack)
		
		g = self.Transpose()

		visited = [False]*(self.V)

		while stack:
			i = stack.pop()
			if visited[i] == False:
				g.DFSUntil(i,visited)
				sum += 1
		print(sum)
		# Size.sort(reverse= True)
		# for i in range(5):
		# 	print(Size[i])




Virtices = []

with open("SCC.txt") as f:
	read_list = f.readlines()
	
	
V = len(read_list)
for i in range(V):
		read_list[i] = read_list[i].split()
for i in range(V):
	Virtices.append(int(read_list[i][0]))
	Virtices.append(int(read_list[i][1]))

g = Graph(len(set(Virtices)),set(Virtices))
for i in range(V):
	x = int(read_list[i][0])
	y = int(read_list[i][1])
	g.addEdges(x,y)
g.SCCs()



