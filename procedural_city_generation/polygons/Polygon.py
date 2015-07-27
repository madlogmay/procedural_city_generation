from __future__ import division
import numpy as np

def is_convex(self):
	for (edge1, edge2) in zip(self.edges, self.edges[1:] + [self.edges[0]]):
		v = edge2.dir_vector - edge1.dir_vector
		angle = np.arctan2(v[1],v[0])
		if angle >= np.pi or (angle < 0 and angle + 2*np.pi >= np.pi):
			return False
	return True
	
def area(self):
	"""Return area of polygon"""
	return 0.5 * abs(sum(edge[0][0]*edge[1][1] - edge[1][0]*edge[0][1]
			for edge in self.edges))
	
class Edge(object):
	
	def __init__(self, vertex1, vertex2, bordering_road = True):
		"""Input vertices are numpy-arrays"""
		self.bordering_road = bordering_road
		self.vertices = (vertex1, vertex2)
		self.dir_vector = vertex2 - vertex1
		self.length = np.linalg.norm(self.dir_vector)
		v = self.dir_vector/self.length
		self.n = np.array((v[1],-v[0]))
		
	def __getitem__(self, i):
		return self.vertices[i]
		
	def __repr__(self):
		return str([round(x, 2) for x in self[0]]) + ", " + str([round(x, 2) for x in self[1]])	
		
class Polygon(object):
	
	def __init__(self, in_list, poly_type="vacant"):
		"""Input may be numpy-arrays or Edge-objects"""

		if isinstance(in_list[0], Edge):
			self.edges = in_list
			self.vertices = [edge[0] for edge in self.edges]
		else:
			self.vertices = in_list
			self.edges = [Edge(v1,v2) for v1,v2 in 
							zip(in_list, in_list[1:]+[in_list[0]])]
		self.is_convex = is_convex(self)
		self.area = area(self)
		self.poly_type = poly_type
				
	def __repr__(self):
		s = "Polygon: \n"
		for vertex in self.vertices:
			s += str([round(x, 2) for x in vertex]) + "\t"
		s += "\n"
		return s
		
	
			


if __name__=="__main__":
	import poly_plot as pp
	p = [np.array(x) for x in [[0,0],[0,1],[1,0.8],[1,0]]]
	poly = Polygon(p)
	p1,p2 = poly.split()
	p1.selfplot(); p2.selfplot()
	plt.show()
