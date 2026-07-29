from Graph import Graph, Vertex

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdsize):
    if 0 <= x < bdsize:
        return True
    else:
        return False

def knightGraph(bdSize):
    ktGragh = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPosition = genLegalMoves(row, col, bdSize)
            for e in newPosition:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGragh.addEdge(nodeId, nid)
    return ktGragh

def posToNodeId(row, col, bdsize):
    return row * bdsize + col

# 深度优先搜索算法
def knightTour(n, path, u: Vertex, limit):
    """
    :param n:层次
    :param path:路径
    :param u:当前顶点
    :param limit:搜索总深度
    """
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i += 1
        if not done:    # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

# 算法改进
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

def knightTourBetter(n, path, u: Vertex, limit):  # use order by available function
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

kg = knightGraph(5)  # five by five solution
thepath = []
start = kg.getVertex(4)
knightTourBetter(0, thepath, start, 24)
for v in thepath:
    print(v.getId())