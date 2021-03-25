import matplotlib.pyplot as plt

import src as gillespie

if __name__ == '__main__':
    N = 500  # whole population
    beta = 3  # transmission rate
    gamma = 0.5  # recovery rate
    a = 0.5  # incubation rate
    t = 15  # duration

    I0 = 3
    initials = [N - I0, 0, I0, 0]  # S, E, I, R

    propensities = [lambda s, e, i, r: beta * s * i / N,  # S -> E, Propensity: b * S(t) * I(t) / N
                    lambda s, e, i, r: a * e,  # E -> I, Propensity: a * E(t)
                    lambda s, e, i, r: gamma * i]  # I -> R, Propensity: g * I(t)

    stoichiometry = [[-1, 1, 0, 0],  # S -> E, Population change: S-1, E+1, I+0, R+0
                     [0, -1, 1, 0],  # E -> I, Population change: S+0, E-1, I+1, R+0
                     [0, 0, -1, 1]]  # I -> R, Population change: S+0, E+0, I-1, R+1

    t, SEIR = gillespie.simulate(initials, propensities, stoichiometry, t)
    S, E, I, R = zip(*SEIR)

    plt.plot(t, S, label="susceptible")
    plt.plot(t, E, label="exposed")
    plt.plot(t, I, label="infected")
    plt.plot(t, R, label="recovered")

    plt.title("SEIR epidemic model")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()

    plt.savefig("plots/SEIR.png")
