import matplotlib.pyplot as plt

import src as gillespie

if __name__ == '__main__':
    alpha = 1  # reproduction rate of prey
    beta = 0.01  # prey consumption rate (and reproduction of predator)
    gamma = 2  # death rate of predators
    t = 15  # duration

    initials = [50, 50]  # prey, predators

    propensities = [lambda prey, pred: alpha * prey,  # prey birth
                    lambda prey, pred: beta * prey * pred,  # prey death / predator birth
                    lambda prey, pred: gamma * pred]  # predator death

    stoichiometry = [[1, 0],  # prey birth
                     [-1, 1],  # prey death / predator birth
                     [0, -1]]  # predator death

    t, PP = gillespie.simulate(initials, propensities, stoichiometry, t)
    Prey, Pred = zip(*PP)

    plt.plot(t, Prey, label="prey")
    plt.plot(t, Pred, label="predators")

    plt.title("Lotka–Volterra population model")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()

    plt.savefig("plots/predator-prey.png")
