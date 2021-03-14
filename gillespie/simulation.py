import math
import random


def run(initials, propensities, stoichiometry, duration):
    """
    

    :param initials:
    :param propensities:
    :param stoichiometry:
    :param duration:
    :return:
    """

    # initial values
    times = [0.0]
    counts = [initials]

    # while finish time has not been reached
    while times[-1] < duration:
        # get current state
        state = counts[-1]

        # calculate weights with respective propensities
        weights = [prop(*state) for prop in propensities]

        # stop loop if no transitions available
        if all(w == 0 for w in weights):
            break

        # randomly draw one transition
        transition = random.choices(stoichiometry, weights=weights)[0]
        next_state = [a + b for a, b in zip(state, transition)]

        # draw next time increment from random exponential distribution
        # dt = math.log(1.0 / random.random()) / sum(weights)
        dt = -math.log(random.random()) / sum(weights)

        # append new values
        times.append(times[-1] + dt)
        counts.append(next_state)

    return t, counts


if __name__ == '__main__':
    N = 50  # whole population
    beta = 2  # transmission rate
    gamma = 0.5  # recovery rate
    t = 15  # duration

    initials = [47, 3, 0]  # S, I, R

    propensities = [lambda s, i, r: beta * s * i / N,  # S -> I, Propensity: b * S(t) * I(t) / N
                    lambda s, i, r: gamma * i]  # I -> R Propensity: g * I(t)

    stoichiometry = [[-1, 1, 0],  # S -> I, Population change: S-1, I+1, R+0
                     [0, -1, 1]]  # I -> R Population change: S+0, I-1, R+1

    run(initials, propensities, stoichiometry, t)
