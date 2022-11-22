
# Python implementation of Kosaraju's algorithm to print all SCCs
from sys import argv

import sys
sys.setrecursionlimit(300000)
from collections import defaultdict


class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)


	def addEdges(self,u,v):
		self.graph[u].append(v)


	def DFSUntil(self, v, visited,size):
		size +=1
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				return self.DFSUntil(i,visited,size)
		return size
		
	

	def fillOrder(self,v,visited,stack) :
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.fillOrder(i,visited,stack)
		stack = stack.append(v)



	def Transpose(self):
		gr = Graph(self.V)
		for i in self.graph:
			for j in self.graph[i]:
				gr.addEdges(j,i)
		return gr
	

	def SCCs(self) :
		stack = []
		Size = []
		visited = [False]*(self.V)
		for i in range(self.V):
			if visited[i] ==False:
				self.fillOrder(i,visited,stack)
		
		g = self.Transpose()

		visited = [False]*(self.V)

		while stack:
			i = stack.pop()
			if visited[i] == False:
				size = 0
				temp =g.DFSUntil(i,visited,size)
				Size.append(temp)

		Size.sort(reverse= True)
		for i in range(5):
			print(Size[i])

		print(Size)







with open("SCC.txt") as f:
	read_list = f.readlines()
	
	
V = len(read_list)
for i in range(V):
		read_list[i] = read_list[i].split()

g = Graph(V)
for i in range(V):
	x = int (read_list[i][0])
	y = int (read_list[i][1])
	g.addEdges(x,y)

g.SCCs()


