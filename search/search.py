# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import manhattanDistance

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	dfsStack = util.Stack()
	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	dfsStack.push((problem.getStartState(),[],[]))
	while not dfsStack.isEmpty():
	 	node, actions, visited = dfsStack.pop()
	 	for coord ,directions,steps in problem.getSuccessors(node):
	 		if not coord in visited :
	 			if problem.isGoalState(coord):
	 				return actions +[directions]
	 			dfsStack.push((coord, actions + [directions], visited + [node] ))
	return []
def breadthFirstSearch(problem):
	bfsQueue = util.Queue()
	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())
	bfsQueue.push((problem.getStartState(),[]))
	marked = []
	while not bfsQueue.isEmpty():
		node, actions = bfsQueue.pop()
		for coord, directions, steps in problem.getSuccessors(node):
			if not coord in marked :
				if problem.isGoalState(coord):
					return actions+[directions]
				bfsQueue.push((coord,actions+[directions]))
				marked.append(coord)
	return []
   

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return manhattanDistance(state,problem)

def aStarSearch(problem, heuristic=nullHeuristic):
	#memory= 40
	visited = []
	fringe = util.PriorityQueue()
	start = problem.getStartState()
	fringe.push( (start, []), heuristic(start, problem))
	while not fringe.isEmpty():
		node, actions = fringe.pop()
		if problem.isGoalState(node):
			return actions
		visited.append(node)
		for coord, directions, cost in problem.getSuccessors(node):
			if not coord in visited:
				new_actions = actions + [directions]
				score = problem.getCostOfActions(new_actions) + heuristic(coord,problem)
				fringe.push( (coord, new_actions), score)
	return []
def smAStarSearch(problem, heuristic=nullHeuristic, memory=40):
	visited = []
	fringe = util.PriorityDeque()
	start = problem.getStartState()
	fringe.push( (start, []), heuristic(start, problem))
	while not fringe.isEmpty():
		node, actions = fringe.pop()
		if problem.isGoalState(node):
			return actions
		visited.append(node)
		for coord, directions, cost in problem.getSuccessors(node):
			if not coord in visited:
				new_actions = actions + [directions]
				score = problem.getCostOfActions(new_actions) + heuristic(coord,problem)
				fringe.push( (coord, new_actions), score)
				if fringe.count > memory:
					fringe.popleft()
	return []

def GreedyBestFirstSearch(problem, heuristic=nullHeuristic):
	visited = []
	fringe = util.PriorityQueue()
	start = problem.getStartState()
	fringe.push( (start, []), heuristic(start, problem))
	while not fringe.isEmpty():
		node, actions = fringe.pop()
		if problem.isGoalState(node):
			return actions
		visited.append(node)
		for coord, directions, cost in problem.getSuccessors(node):
			if not coord in visited:
				new_actions = actions + [directions]
				score = heuristic(coord,problem)
				fringe.push( (coord, new_actions), score)
	return []

# Abbreviations
gbfs = GreedyBestFirstSearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
smastar = smAStarSearch
ucs = uniformCostSearch
