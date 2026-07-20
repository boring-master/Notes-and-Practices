# 完整版
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        """
        判断当前节点是否为叶子节点
        """
        return not (self.rightChild or self.leftChild)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def inorder(self):
        """
        中序遍历（左 -> 根 -> 右）
        """
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        """
        后序遍历（左 -> 右 -> 根）
        """
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def preorder(self):
        """
        前序遍历（根 -> 左 -> 右）
        """
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def printexp(self):
        """
        以带括号的格式打印表达式树
        """
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

    def postordereval(self):
        """
        计算表达式树的最终结果
        """
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        res1 = None
        res2 = None
        if self.leftChild:
            res1 = self.leftChild.postordereval()
        if self.rightChild:
            res2 = self.rightChild.postordereval()
        if res1 and res2:
            return opers[self.key](res1, res2)
        else:
            return self.key

def inorder(tree):
    """
    外部实现的中序遍历
    """
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def preorder(tree):
    """
    外部实现的前序遍历
    """
    if tree is not None:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    """
    外部实现的后序遍历
    """
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def printexp(tree):
    """
    外部实现的带括号表达式打印
    """
    if tree.leftChild:
        print('(', end=' ')
        printexp(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.rightChild:
        printexp(tree.getRightChild())
        print(')', end=' ')

def printexp(tree):
    """
    外部实现的带括号表达式构建
    """
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        sVal += printexp(tree.getRightChild()) + ')'
    return sVal

def postordereval(tree):
    """
    外部实现的表达式树求值
    """
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

def height(tree):
    """
    计算二叉树的高度
    """
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))

if __name__ == '__main__':
    t = BinaryTree(7)
    t.insertLeft(3)
    t.insertRight(9)
    inorder(t)
    import operator # 替代传统的运算符表达式（如加法、乘法、比较等）并提升性能

    x = BinaryTree('*')
    x.insertLeft('+')
    l = x.getLeftChild()
    l.insertLeft(4)
    l.insertRight(5)
    x.insertRight(7)
    print(printexp(x))
    print(postordereval(x))
    print(height(x))