from tictactoe import TicTacToe, filters
from state import GameState
from tree import Tree

game = TicTacToe()
game.setupTree()
#game.checkChildScores()

print("Depth of root: " + str(game.tree.root.data.depth))
node = game.tree.findNode([0,1,0,1,2,0])
print("Depth of this node " + str(node.data.depth))

game.xplayer = True #Human is X
game.oplayer = True #Human is O

while not game.gameover:
    print("")
    print(game.template)
    print("=======")
    print(game.tree.root.data)
    if game.xturn:
        if game.xplayer:
            game.humanTurn('X')
            #game.checkChildScores()
        else:
            pass
    else:
        if game.oplayer:
            game.humanTurn('O')
            #game.checkChildScores()
        else:
            pass

    if game.checkEndGame():
        game.gameover = True
    game.xturn = not game.xturn
    #game.gameover = True #testing

print(game.tree.root.data)
print("GAME OVER MAN!")
    
"""
print("Testing")
num = game.tree.walk(0, game.tree.root)
print(num)
node = game.tree.findNode([0,1,0,1,0,1])
if node is not None:
    print(node.data)
    print(node.data.state)

#print(node.data.isEndState(filters()))


print("Checking finding node by state")
state = ['X', 'O', -2, 'X', -2, -2, 'O', 'X', -2]
#state = ['X', -2, -2, -2, -2, -2, 'O', -2, -2]
data = GameState(state)
print(data.state)
node = game.tree.find(data)
if node is not None:
    print(node.data)
    print(node.id)

    node = game.tree.findNode(node.id)
    if node is not None:
        print(node.data)
        print(node.id)
"""
#Test a fake simple tree
#tree = Tree()
#tree.addNode(tree.root, 1)
#tree.addNode(tree.root, 4)
#tree.addNode(tree.root, 5)
#tree.addNode(tree.root.children[0], 2)
#tree.addNode(tree.root.children[0], 8)
#tree.addNode(tree.root.children[2], 78)
#tree.addNode(tree.root.children[2], 99)

#num = tree.walk(0, tree.root)
#print(num)
#node = tree.find(8)
#if node is not None:
#    print(node.id)
#    print(node.data)
