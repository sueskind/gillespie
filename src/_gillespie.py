import math
import random


def simulate(initials, propensities, stoichiometry, duration):
    """
    Run a simulation with given model.

    :param initials: List of initial population counts.
    :param propensities: List of functions that take population counts and give transition rates.
    :param stoichiometry: List of integers, how the population counts change per transition.
    :param duration: Maximum simulation time.
    :return: Two lists: The time points and population counts per time point.
    """

    # initial values
    times = [0.0]
    counts = [initials]

    # while finish time has not been reached
    while times[-1] < duration:
        # get current state
        state = counts[-1]

        # calculate rates with respective propensities
        rates = [prop(*state) for prop in propensities]

        # stop loop if no transitions available
        if all(r == 0 for r in rates):
            break

        # randomly draw one transition
        transition = random.choices(stoichiometry, weights=rates)[0]
        next_state = [a + b for a, b in zip(state, transition)]

        # draw next time increment from random exponential distribution
        # dt = math.log(1.0 / random.random()) / sum(weights)
        dt = -math.log(random.random()) / sum(rates)

        # append new values
        times.append(times[-1] + dt)
        counts.append(next_state)

    return times, counts
