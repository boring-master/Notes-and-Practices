import sys
from typing import Dict
class Vertex:
    """顶点"""
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None    # 前驱结点
        self.disc = 0
        self.fin = 0
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def setColor(self,color):
        self.color = color
    def setDistance(self,d):
        self.dist = d
    def setPred(self,p):
        self.pred = p
    def setDiscovery(self, dtime):
        self.disc = dtime
    def setFinish(self, ftime):
        self.fin = ftime
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def __repr__(self):
        return self.__str__()
    def getFinish(self):
        return self.fin
    def getDiscovery(self):
        return self.disc
    def getPred(self):
        return self.pred
    def getDistance(self):
        return self.dist
    def getColor(self):
        return self.color
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList: Dict[int|str|tuple, Vertex] = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList
    def addEdge(self, f, t, cost=0):
        """
        :param f:一个顶点
        :param t:另一个顶点
        :param cost:边的权重，默认为0
        """
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
"""
当打印包含对象的容器（如字典、列表）时，如print(g.vertList)，
Python在构建这个容器的字符串表示时，不会去调用容器内部元素的 __str__ 方法，
而是去调用它们的 __repr__ 方法。若Vertex类中没有定义 __repr__ 方法，
Python就会回退（fallback）到默认的object.__repr__，
从而打印出类似 <__main__.Vertex object at 0x...> 的内存地址
"""
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))