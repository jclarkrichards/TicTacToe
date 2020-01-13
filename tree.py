"""This is a representation of a tree.  A tree has a root node, and each node can have numerous children.  Children have parents except for the root node.  A child can only have 1 parent."""
class TreeNode(object):
    def __init__(self):
        self.id = [] #each Node object is unique
        self.parent = None
        self.children = []
        self.data = None #GameState object
        self.visited = False
        self.score = 0
        self.depth = 0
        
    def __repr__(self):
        return "Node: " + str(self.id)

    
class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.root.id = [0]

    def findNode(self, id):
        '''Find the node in the tree with the given id.  The id shows the path the tree must take to reach the desired node.'''
        node = self.root
        #print(id)
        vals = id[len(self.root.id):]
        for val in vals:
            #print(val)
            try:
                node = node.children[val]
            except IndexError:
                return None
        return node

    def find(self, data):
        '''If you have the data instead of the id.  Return TreeNode object.'''
        def recurse(node):
            #print(str(data) + ", " + str(node.data))
            if data == node.data:
                return node
            for n in node.children:
                anode = recurse(n)
                if anode is not None: return anode
            return None
        return recurse(self.root)
    
    def addNode(self, parent, data=None):
        '''Add a node to the tree.  This node should be a child of the given parent node'''
        node = TreeNode()
        node.data = data
        for val in parent.id:
            node.id.append(val)
        node.parent = parent
        numchildren = len(parent.children)
        node.id.append(numchildren)
        node.depth = len(node.id)-1
        parent.children.append(node)
        return node
    
    def walk(self, num, node):
        '''Walk through the tree and print out all of the nodes, print leaves first'''
        if len(node.children) == 0:
            num += 1
            print("L: " + str(node) + " depth: " + str(node.depth) + " score: " + str(node.score))
            print(node.data)
        else:
            for n in node.children:
                num = self.walk(num, n)
            print("N: " + str(node) + " depth: " + str(node.depth) + " score: " + str(node.score))
            print(node.data)

        return num

    

    
    #This will most likely be deleted.  Just for testing...
    def scoreTest(self, filters):
        d = {'X':0, 'O':0, 'TIE':0}
        scores = {'X':{}, 'O':{}}
        #print(d)
        def recurse(d, scores, node):
            #print(d)
            if len(node.children) == 0: #leaf node (end state)
                if node.data.winnerX(filters) and not node.data.winnerO(filters):
                    depth = len(node.id) - len(self.root.id)
                    if len(scores['X']) == 0:
                        scores['X'][depth] = 1
                    else:
                        if depth in scores['X']:
                            scores['X'][depth] += 1
                        else:
                            if depth < scores['X'].keys()[0]:
                                scores['X'].pop(scores['X'].keys()[0])
                                scores['X'][depth] = 1
                                        
                    
                    d['X'] += 1
                    
                elif node.data.winnerO(filters) and not node.data.winnerX(filters):
                    depth = len(node.id) - len(self.root.id)
                    if len(scores['O']) == 0:
                        scores['O'][depth] = 1
                    else:
                        if depth in scores['O']:
                            scores['O'][depth] += 1
                        else:
                            if depth < scores['O'].keys()[0]:
                                scores['O'].pop(scores['O'].keys()[0])
                                scores['O'][depth] = 1
                                        

                    d['O'] += 1

            else:
                for n in node.children:
                    #scores[n.id] = {}
                    recurse(d, scores, n)
                    
                    if node is self.root:
                        print("")
                        print("Results for " + str(n.id))
                        #print(d)
                        #print(str(d['X'] - d['O']))
                        d = {'X':0, 'O':0, 'TIE':0}
                        print(scores)
                        #print(str(scores['X'] - scores['O']))
                        scores = {'X':{}, 'O':{}}
        #print(d)
        recurse(d, scores, self.root)
        
        #return recurse(self.root)
    
    def isLeaf(self, id):
        '''Check if the node with the given id is a leaf or not'''
        node = self.findNode(id)
        if len(node.children) == 0:
            return True
        return False

    def prune(self, node, filters):
        '''Prune the tree so that nodes with a 3-in-a-row have no children'''
        if node.data.isEndState(filters):
            node.children = []  #empty the children
            node.data.setWinner(filters)
        else:
            for n in node.children:
                self.prune(n, filters)
    
    def setRoot(self, id):
        '''Given an id, set that node as the root.  This removes portions of the tree'''
        node = self.findNode(id)
        if node is not None:
            self.root = node
            self.root.parent = None
            self.decreaseDepth()
            
    def decreaseDepth(self):
        '''Go through tree and set the depth of all nodes to 1 less than previous'''
        def recurse(node):
            node.depth -= 1
            for childNode in node.children:
                recurse(childNode)
        recurse(self.root)
        

    #set root with data as well instead of id
    def checkWinners(self, node, wins, symbol):
        if len(node.children) == 0:
            if node.data.winner == symbol:
                wins[node.depth] += 1
        else:
            for n in node.children:
                wins= self.checkWinners(n, wins, symbol)

        return wins
        
"""
#Testing the tree
print("Tree testing")
tree = Tree()
print("root: " + str(tree.root))
#print(tree.root.parent)
#print(tree.root.children)
#print(tree.root.id)
tree.addNode(tree.root)
tree.addNode(tree.root)
tree.addNode(tree.root)
for child in tree.root.children:
    print(child)
    print(child.parent)

node = tree.findNode([0,1])
print("# " + str(node))
tree.addNode(node)
tree.addNode(node)

for child in node.children:
    print(child)
    print(child.parent)

node = tree.findNode([0,1,1])
print(node)
if node is None:
    print("Node is not in the tree")

node = tree.findNode([0,0])
tree.addNode(node)
tree.addNode(node)
tree.addNode(node)
for child in node.children:
    print(child)
    print(child.parent)

node = tree.findNode([0,1,1])
tree.addNode(node)
tree.addNode(node)

node = tree.findNode([0,0])
tree.addNode(node)
tree.addNode(node)

print("Walk through the tree")
tree.walk(tree.root)


print("IS it a leaf?")
print(tree.isLeaf([0]))
print(tree.isLeaf([0,1]))
print(tree.isLeaf([0,1,1,0]))
print(tree.isLeaf([0,2]))

print("Set new root")
tree.setRoot([0,1])
tree.walk(tree.root)

print(tree.root.id)
node = tree.findNode([0,1,1,1])
print(node)
tree.addNode(node)
tree.addNode(node)
tree.addNode(node)

node = tree.findNode([0,0,1])
print(node)
tree.walk(tree.root)
"""
