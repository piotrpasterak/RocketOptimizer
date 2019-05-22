from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

y_1 = 1.11 * 10**(-9)
y_2 = 1.48 * 10**9
y_3 = 4.88 * 10**21


def goal_f(r):
    return y_1 * r[0]**2 * r[1]**3 * (y_2 + np.sqrt(y_2**2 - (y_3 / r[0]**2 * r[1]**3)))


def print_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(1, 100000, 1)
    Y = np.arange(1, 8, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = goal_f([X,Y])

    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)

    plt.show()


if __name__ == '__main__':
    """Main script loop.
    """

    fopt = optimize.minimize(goal_f, [100000, 10], method="Nelder-Mead")
    print(fopt)

    print_plot()



