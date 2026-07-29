from Graph import Graph, Vertex
# 下面的Queue类可替换为from collections import deque（入队和出队都是O(1)）
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile, 'r') as wfile:
        # create buckets of words that differ by one letter
        for line in wfile:
            word = line[:-1]    # 去除换行符（假设每一行都以换行符结尾，即最后一行是空行）
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    # 上面的三层循环可替换为以下
    """
    from itertools import combinations
    for bucket_words in d.values():
        for word1, word2 in combinations(bucket_words, 2):
            g.addEdge(word1, word2)
    """
    return g

def bfs(g, start: Vertex):
    """广度优先搜索Breadth First Search"""
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert: Vertex = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y: Vertex):
    """反向打印出完整的单词变换路径"""
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

wordgraph = buildGraph("fourletterwords.txt")
bfs(wordgraph, wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))
# traverse(wordgraph.getVertex('COOL'))
