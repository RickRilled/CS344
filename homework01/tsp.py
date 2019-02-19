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

    def actions(self, state):
        return [state + 1]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        #return the path it takes


if __name__ == '__main__':

    cities = []
    distances = []
    numCities = 5


    """
    This was the best way I found to create a bunch of random distance values that was guaranteed to have
    enough values for each city
    """
    CD0 = 1

    for city in range(numCities):
        for paths in range(numCities - CD0):
            value = randrange(25, 100)
            distances.append(value)
        CD0 += 1

    CD1 = 1

    for city in range(numCities):
        for x in range(numCities - CD1):
            cities.append(str(city) + " " + str(distances[randrange(0, len(distances))]))
        CD1 += 1

    p = TSP(numCities)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          )

    # print(distances, cities)




