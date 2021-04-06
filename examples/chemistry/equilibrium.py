import matplotlib.pyplot as plt

import src as gillespie

if __name__ == '__main__':
    forward = 2  # forward reaction rate
    backward = 0.5  # backward reaction rate
    t = 15  # duration

    initials = [100, 150, 0]  # X, Y, XY

    propensities = [lambda x, y, xy: forward * x * y,  # X + Y -> XY, Propensity: forward * X * Y
                    lambda x, y, xy: backward * xy]  # XY -> X + Y, Propensity: backward * XY

    stoichiometry = [[-1, -1, 1],  # X + Y -> XY, Population change: X - 1, Y - 1, XY + 1
                     [1, 1, -1]]  # XY -> X + Y, Population change: X + 1, Y + 1, XY - 1

    t, XYXY = gillespie.simulate(initials, propensities, stoichiometry, t)
    X, Y, XY = zip(*XYXY)

    plt.plot(t, X, label="X")
    plt.plot(t, Y, label="Y")
    plt.plot(t, XY, label="XY")

    plt.title("Simple equilibrium reaction X + Y -> XY")
    plt.xlabel("Time")
    plt.ylabel("Number of molecules")
    plt.legend()

    plt.savefig("plots/equilibrium.png")
