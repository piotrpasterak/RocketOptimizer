from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

y_1 = 1.11 * 10**(-9)
y_2 = 1.48 * 10**9
y_3 = 4.88 * 10**21


def goal_f(r):
    return y_1 * r[0]**2 * r[1]**3 * (y_2 + np.sqrt(y_2**2 - (y_3 / (r[0]**2 * r[1]**3))))


def restrict_f(r):
    return np.sqrt(y_2**2 - (y_3 / (r[0]**2 * r[1]**3)))


def print_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(10, 40000, 100)
    Y = np.arange(3, 40, 1)
    X, Y = np.meshgrid(X, Y)
    plt.title('Funkcja celu')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    Z = goal_f([X, Y])

    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)

    #ax.plot_surface(X, Y, restrict_f([X, Y]), linewidth=0, antialiased=True)

    plt.show()

if __name__ == '__main__':
    """Main script loop.
    """
    bnds = ((0.1, 0.001), (1000, 100))

    cons = [{'type': 'ineq', 'fun': lambda x: y_2**2 - (y_3 / (x[0]**2 * x[1]**3))},
            {'type': 'ineq', 'fun': lambda x: x[0]},
            {'type': 'ineq', 'fun': lambda x: x[1]}]

    fopt = optimize.minimize(goal_f, [100, 10],method="trust-constr", constraints=cons, hess=None)
    print(fopt)

    print("----------------------------------------")

    fopt2 = optimize.minimize(goal_f, [100, 10],method="COBYLA", constraints=cons)
    print(fopt2)

    print_plot()
