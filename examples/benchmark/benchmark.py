import random
import timeit

import src as gillespie

if __name__ == '__main__':
    # SIR epidemic model for benchmarking

    random.seed(12345)

    N = 10000000  # whole population
    beta = 2  # transmission rate
    gamma = 0.5  # recovery rate
    t = 15  # duration

    initials = [47, 3, 0]  # S, I, R

    propensities = [lambda s, i, r: beta * s * i / N,  # S -> I, Propensity: b * S(t) * I(t) / N
                    lambda s, i, r: gamma * i]  # I -> R Propensity: g * I(t)

    stoichiometry = [[-1, 1, 0],  # S -> I, Population change: S-1, I+1, R+0
                     [0, -1, 1]]  # I -> R Population change: S+0, I-1, R+1

    print(timeit.timeit(lambda: gillespie.simulate(initials, propensities, stoichiometry, t), number=1000))
