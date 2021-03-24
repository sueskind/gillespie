import matplotlib.pyplot as plt

import src as gillespie

if __name__ == '__main__':
    N = 500  # whole population
    beta = 2  # transmission rate
    gamma = 0.5  # recovery rate
    t = 15  # duration

    I0 = 3
    initials = [N - I0, I0]  # S, I

    propensities = [lambda s, i: beta * s * i / N,  # S -> I, Propensity: b * S(t) * I(t) / N
                    lambda s, i: gamma * i]  # I -> S, Propensity: g * I(t)

    stoichiometry = [[-1, 1],  # S -> I, Population change: S-1, I+1
                     [1, -1]]  # I -> S, Population change: S+1, I-1

    t, SI = gillespie.simulate(initials, propensities, stoichiometry, t)
    S, I = zip(*SI)

    plt.plot(t, S, label="susceptible")
    plt.plot(t, I, label="infected")

    plt.title("SIS epidemic model")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()

    plt.savefig("plots/SIS.png")
