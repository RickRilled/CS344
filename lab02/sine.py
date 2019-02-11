"""
This module implements the sine objective function

Author: Royce Lloyd
Based on abs.py by Prof. VanderLinden
12/10/2019 for CS 344 at Calvin College
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time
import statistics


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)

    p = SineVariant(initial, maximum, delta=5.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    then0 = time.time()
    hill_solution0 = hill_climbing(p)
    print('Hill-climbing solution 0       x: ' + str(hill_solution0)
          + '\tvalue: ' + str(p.value(hill_solution0))
          )
    hill_solution1 = hill_climbing(p)
    print('Hill-climbing solution 1       x: ' + str(hill_solution1)
          + '\tvalue: ' + str(p.value(hill_solution1))
          )
    hill_solution2 = hill_climbing(p)
    print('Hill-climbing solution 2       x: ' + str(hill_solution2)
          + '\tvalue: ' + str(p.value(hill_solution2))
          )
    hill_climbing_data = [p.value(hill_solution0), p.value(hill_solution1), p.value(hill_solution2)]
    print('Average hill climbing solution time:', statistics.mean(hill_climbing_data))
    now0 = time.time()
    print("Time for hill climbing:", now0 - then0, "\n")

    # Solve the problem using simulated annealing.
    then1 = time.time()
    annealing_solution0 = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    print('Simulated annealing solution 0 x: ' + str(annealing_solution0)
          + '\tvalue: ' + str(p.value(annealing_solution0))
          )
    annealing_solution1 = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    print('Simulated annealing solution 1 x: ' + str(annealing_solution1)
          + '\tvalue: ' + str(p.value(annealing_solution1))
          )
    annealing_solution2 = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    print('Simulated annealing solution 2 x: ' + str(annealing_solution2)
          + '\tvalue: ' + str(p.value(annealing_solution2))
          )
    sa_data = [p.value(annealing_solution0), p.value(annealing_solution1), p.value(annealing_solution2)]
    print("Average SA solution time:", statistics.mean(sa_data))
    now1 = time.time()
    print("Time for SA:", now1 - then1)
