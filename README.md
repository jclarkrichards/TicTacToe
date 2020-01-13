# TicTacToe
If you play against the computer, then you will never win.  The computer is a perfect player and will not make a mistake.  The best you can do is tie with the computer.

You run the game with 'python main.py'.

You can choose what type of players X and O are (human or computer).

When choosing to place an X or an O you use the keypad (0-8) to indicate where to place the symbol.  The following diagram will be shown before each turn:

0 | 1 | 2
- + - + -
3 | 4 | 5
- + - + -
6 | 7 | 8

We use the minimax algorithm for the AI.

Trees:
A tree starts with a root node.  Each node is of type TreeNode and has the following properties:

TreeNode:
id: unique identifier and is of type list.  The root node id is [0].  The root node's second child would be [0,1].  The id basically gives you the direct path to the node from the root node.
parent:  Each node only has 1 parent except for the root node which has no parent.
children:  A node is a leaf node if it has no children.  Leaf nodes are end states for the game.
data:  In this case the data is of type GameState
score:  The score gets calculated during the minimax.
depth: How far down the tree is this node?  Directly related to the id.  The depth is just the length of id - 1.

Minimax:
The minimax algorithm needs a tree as input.  The algorithm works by traversing the tree (in order) until a leaf is reached.  When a leaf is reached a score is calculated depending on the state of the game that node represents and whose turn it is.  The score is just the inverse of the depth so that leafs closer to the root node will have higher scores.  If the players turn is X and if the leaf node represents a win for X then the score is positive.  If the leaf node represents a win for O, then the score is negative.  If neither X nor O win, then the score is 0.  When all of the children of a node have been visited, then that node gets assigned the highest or lowest score from the children.  If the depth is even then the largest value is stored.  If the depth is odd, then the lowest value is stored.  After reaching the root again after all children have been visited, then the algorithm returns the index of roots children that corresponds to the best path.

