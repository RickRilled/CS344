"""
This file solves the TSP problem using Hill Climbing and SA.
It can be configured with random distances and number of cities

Written by Royce Lloyd for CS 344 at Calvin College
2/22/2019
"""

from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class TSP(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, numCities):
        self.numCities = numCities
        self.citiesDistances = []
        self.distances = []
        self.distancesMatrix = []

        self.initial = []

        for x in range(0, numCities):
            self.initial.append(x)

        """
        This was the best way I found to create a bunch of random distance values that was guaranteed to have
        enough values for each city
        """

        decrement = 1
        for city in range(numCities):
            for paths in range(numCities - decrement):
                value = randrange(25, 100)
                self.distances.append(value)
            decrement += 1


        for city in range(0, numCities):
            cityArray = []
            for x in range(0, numCities ):
                cityArray.append(self.distances[randrange(0, len(self.distances))])
            self.distancesMatrix.append(cityArray)



        for x in range(0, numCities):
            for city in range(0, numCities):
                self.distancesMatrix[x][city] = self.distancesMatrix[city][x]

    def actions(self, state):
        idea_list = []

        for x in range(0, self.numCities):
            for y in range(0, self.numCities):
                if(x != y):
                    idea = [x, y]
                    idea_list.append(idea)
        return idea_list

    def result(self, state, action):
        state_copy = state[:]
        temp_state = state_copy[action[0]]
        state_copy[action[0]] = state_copy[action[1]]
        state_copy[action[1]] = temp_state
        return state_copy


    def value(self, state):
        sum = 0

        for x in range(0, len(state)):
            cityA = state[x]
            cityB = state[(x + 1) % len(state)]
            sum += self.distancesMatrix[cityA][cityB]
        maxDistance = 100 * numCities
        sum = maxDistance - sum
        return sum


if __name__ == '__main__':

    numCities = 25

    p = TSP(numCities)

    #Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    print(str(hill_solution))
    print(p.value(hill_solution))

    #Solve the problem with SA
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    print(str(annealing_solution))
    print(p.value(annealing_solution))






