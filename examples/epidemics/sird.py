import gillespie
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 500  # whole population
    beta = 2  # transmission rate
    gamma = 0.5  # recovery rate
    mu = 0.05  # mortality rate
    t = 15  # duration

    I0 = 3
    initials = [N - I0, I0, 0, 0]  # S, I, R, D

    propensities = [lambda s, i, r, d: beta * s * i / N,  # S -> I, Propensity: b * S(t) * I(t) / N
                    lambda s, i, r, d: gamma * i,  # I -> R Propensity: g * I(t)
                    lambda s, i, r, d: mu * i]  # I -> D Propensity: m * I(t)

    stoichiometry = [[-1, 1, 0, 0],  # S -> I, Population change: S-1, I+1, R+0, D+0
                     [0, -1, 1, 0],  # I -> R Population change: S+0, I-1, R+1, D+0
                     [0, -1, 0, 1]]  # I -> D Population change: S+0, I-1, R+0, D+1

    t, SIRD = gillespie.simulate(initials, propensities, stoichiometry, t)
    S, I, R, D = zip(*SIRD)

    plt.plot(t, S, label="susceptible")
    plt.plot(t, I, label="infected")
    plt.plot(t, R, label="recovered")
    plt.plot(t, D, label="deceased")

    plt.title("SIRD epidemic model")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()

    plt.savefig("plots/SIRD.png")
