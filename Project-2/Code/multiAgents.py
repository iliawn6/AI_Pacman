# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood().asList()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        pacmanPositionition = currentGameState.getPacmanPosition()

        if successorGameState.isWin():
            return 90000

        for ghost_state in newGhostStates:
            if ghost_state.getPosition() == pacmanPositionition and ghost_state.scaredTimer == 0:
                return -90000

        score = 0

        if action == 'Stop':
            score -= 100
        
        foodDist = [util.manhattanDistance(newPos, food) \
        for food in newFood]
        nearestFood = min(foodDist)
        score += float(1/nearestFood)
        score -= len(newFood)

        currentGhostDist = [util.manhattanDistance(newPos, ghost.getPosition()) \
        for ghost in currentGameState.getGhostStates()]
        nearestCurrentGhost = min(currentGhostDist)
    
        newGhostDist = [util.manhattanDistance(newPos, ghost.getPosition()) \
        for ghost in newGhostStates]
        nearestNewGhost = min(newGhostDist)

        sumScaredTimes = sum(newScaredTimes)
        if sumScaredTimes > 0 :
            if nearestNewGhost < nearestCurrentGhost:
                score += 200
            else:
                score -= 100
        else:
            if nearestNewGhost < nearestCurrentGhost:
                score -= 100
            else:
                score += 200

        return successorGameState.getScore() + score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def minValue(state, agentIndex, depth):

            agentCount = gameState.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)

            if not legalActions:
                return self.evaluationFunction(state)

            if agentIndex == agentCount - 1:
                minimumValue =  min(maxValue(state.generateSuccessor(agentIndex, action), \
                agentIndex,  depth) for action in legalActions)
            else:
                minimumValue = min(minValue(state.generateSuccessor(agentIndex, action), \
                agentIndex + 1, depth) for action in legalActions)

            return minimumValue

        def maxValue(state, agentIndex, depth):
        
            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)

            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            maximumValue =  max(minValue(state.generateSuccessor(agentIndex, action), \
            agentIndex + 1, depth + 1) for action in legalActions)

            return maximumValue

        actions = gameState.getLegalActions(0)
        
        allActions = {}
        for action in actions:
            allActions[action] = minValue(gameState.generateSuccessor(0, action), 1, 1)

        return max(allActions, key=allActions.get)

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        def minValue(state, agentIndex, depth, alpha, beta):
            
            agentCount = gameState.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)

            if not legalActions:
                return self.evaluationFunction(state)

            minimumValue = 99999
            currentBeta = beta
           
            if agentIndex == agentCount - 1:
                for action in legalActions:
                    minimumValue =  min(minimumValue, maxValue(state.generateSuccessor(agentIndex, action), \
                    agentIndex,  depth, alpha, currentBeta))
                    if minimumValue < alpha:
                        return minimumValue
                    currentBeta = min(currentBeta, minimumValue)

            else:
                for action in legalActions:
                    minimumValue =  min(minimumValue,minValue(state.generateSuccessor(agentIndex, action), \
                    agentIndex + 1, depth, alpha, currentBeta))
                    if minimumValue < alpha:
                        return minimumValue
                    currentBeta = min(currentBeta, minimumValue)

            return minimumValue

        def maxValue(state, agentIndex, depth, alpha, beta):

            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)

            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            maximumValue = -99999
            currentAlpha = alpha

            for action in legalActions:
                maximumValue = max(maximumValue, minValue(state.generateSuccessor(agentIndex, action), \
                agentIndex + 1, depth + 1, currentAlpha, beta) )
                if maximumValue > beta:
                    return maximumValue
                currentAlpha = max(currentAlpha, maximumValue)
            return maximumValue

        actions = gameState.getLegalActions(0)
        alpha = -99999
        beta = 99999
       
        allActions = {}
        for action in actions:
            value = minValue(gameState.generateSuccessor(0, action), 1, 1, alpha, beta)
            allActions[action] = value

            if value > beta:
                return action
            alpha = max(value, alpha)

        return max(allActions, key=allActions.get)   
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expValue(state, agentIndex, depth):
            agentCount = gameState.getNumAgents()
            legalActions = state.getLegalActions(agentIndex)
            if not legalActions:
                return self.evaluationFunction(state)

            expectedValue = 0
            probabilty = 1.0 / len(legalActions) 
            for action in legalActions:
                if agentIndex == agentCount - 1:
                    currentExpValue =  maxValue(state.generateSuccessor(agentIndex, action), \
                    agentIndex,  depth)
                else:
                    currentExpValue = expValue(state.generateSuccessor(agentIndex, action), \
                    agentIndex + 1, depth)
                expectedValue += currentExpValue * probabilty

            return expectedValue


        def maxValue(state, agentIndex, depth):
           
            agentIndex = 0
            legalActions = state.getLegalActions(agentIndex)

            if not legalActions  or depth == self.depth:
                return self.evaluationFunction(state)

            maximumValue =  max(expValue(state.generateSuccessor(agentIndex, action), \
            agentIndex + 1, depth + 1) for action in legalActions)

            return maximumValue
        actions = gameState.getLegalActions(0)
        allActions = {}
        for action in actions:
            allActions[action] = expValue(gameState.generateSuccessor(0, action), 1, 1)
        return max(allActions, key=allActions.get)
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    Don't forget to use pacmanPosition, foods, scaredTimers, ghostPositions!
    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPosition = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()
    scaredTimers = [ghostState.scaredTimer for ghostState in ghostStates]
    ghostPositions = currentGameState.getGhostPositions()
    #ghostPosition = ghost.getPosition

    currentCapsule = currentGameState.getCapsules()
    if currentGameState.isWin():
        return 90000

    for state in ghostStates:
        if state.getPosition() == pacmanPosition and state.scaredTimer == 1:
            return -90000

    score = 0

    foodDistance = [util.manhattanDistance(pacmanPosition, food) \
    for food in foods]
    nearestFood = min(foodDistance)
    score += float(1/nearestFood)
    score -= len(foods)

    if currentCapsule:
        capsuleDistance = [util.manhattanDistance(pacmanPosition, capsule) \
        for capsule in currentCapsule]
        nearestCapsule = min(capsuleDistance)
        score += float(1/nearestCapsule)

    currentGhostDistances = [util.manhattanDistance(pacmanPosition, ghost.getPosition()) \
    for ghost in currentGameState.getGhostStates()]
    nearestCurrentGhost = min(currentGhostDistances)
    scaredTime = sum(scaredTimers)
    if nearestCurrentGhost >= 1:
        if scaredTime < 0:
            score -= 1/nearestCurrentGhost
        else:
            score += 1/nearestCurrentGhost

    return currentGameState.getScore() + score

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
