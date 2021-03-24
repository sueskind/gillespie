import gillespie
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 500  # whole population
    beta = 2  # transmission rate
    gamma = 0.5  # recovery rate
    t = 15  # duration

    I0 = 3
    initials = [N - I0, I0, 0]  # S, I, R

    propensities = [lambda s, i, r: beta * s * i / N,  # S -> I, Propensity: b * S(t) * I(t) / N
                    lambda s, i, r: gamma * i]  # I -> R Propensity: g * I(t)

    stoichiometry = [[-1, 1, 0],  # S -> I, Population change: S-1, I+1, R+0
                     [0, -1, 1]]  # I -> R Population change: S+0, I-1, R+1

    t, SIR = gillespie.simulate(initials, propensities, stoichiometry, t)
    S, I, R = zip(*SIR)

    plt.plot(t, S, label="susceptible")
    plt.plot(t, I, label="infected")
    plt.plot(t, R, label="recovered")

    plt.title("SIR epidemic model")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()

    plt.savefig("plots/SIR.png")
