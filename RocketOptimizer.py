from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

y_1 = 1.11 * 10**(-9)
y_2 = 1.48 * 10**9
y_3 = 1.49 * 10**5
y_4 = 4.88 * 10**21


def goal_f(r):
    return y_1 * r[0]**2 * r[1]**3 * (y_2 - y_3 * (r[1]**2/r[0]**2) + np.sqrt((y_3 * (r[1]**2/r[0]**2) - y_2)**2 - (y_4 / (r[0]**2 * r[1]**3))))


def restrict_f(x):
    return (y_3 * (x[1]**2/x[0]**2) - y_2)**2 - (y_4 / (x[0]**2 * x[1]**3))


def print_plot(solution):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(5, 40000, 100)
    Y = np.arange(0.1, 40, 0.1)
    X, Y = np.meshgrid(X, Y)
    plt.title('Funkcja celu rakiety Saturn V')
    ax.set_xlabel("R")
    ax.set_ylabel("r")
    ax.set_zlabel("V")
    Z = goal_f([X, Y])

    pointx = [solution[0][0], solution[1][0]]
    pointy= [solution[0][1], solution[1][1]]
    pointz = [solution[0][2], solution[1][2]]
    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)
    ax.scatter(pointx, pointy, pointz, c="r")
    plt.show()


if __name__ == '__main__':
    """Main script loop.
    Zadanie optymalizacyjne:
    Promień dyszy silnika, oznaczany małą literą r,
    Promień zewnętrzny stopnia rakiety, oznaczany dużą literą R.
    """

    cons = [{'type': 'ineq', 'fun': restrict_f},
            {'type': 'ineq', 'fun': lambda x: x[0]},
            {'type': 'ineq', 'fun': lambda x: x[0] - 8},
            {'type': 'ineq', 'fun': lambda x: 2.5 - x[1]},
            {'type': 'ineq', 'fun': lambda x: x[1] - 20},
            {'type': 'ineq', 'fun': lambda x: x[0] - x[1]}
            ]

    print(
        """
        Method COBYLA uses the Constrained Optimization BY Linear Approximation (COBYLA) method. 
        The algorithm is based on linear approximations to the objective function and each constraint. 
        The method wraps a FORTRAN implementation of the algorithm. 
        The constraints functions ‘fun’ may return either a single number or an array or list of numbers.
        """
    )

    result_cobyla = optimize.minimize(goal_f, [5, 10], method="COBYLA", constraints=cons)
    print(result_cobyla)

    print(
        """
        Method trust - constr is a trust - region algorithm for constrained optimization.
        It swiches between two implementations depending on the problem definition.
        It is the most versatile constrained minimization algorithm implemented in SciPy and the most appropriate for large-scale problems.
        This interior point algorithm, in turn, solves inequality constraints by introducing slack variables and solving a sequence of equality-constrained barrier problems for progressively smaller values of the barrier parameter.
        The previously described equality constrained SQP method is used to solve the subproblems with increasing levels of accuracy as the iterate gets closer to a solution.
        """)

    result_trust = optimize.minimize(goal_f, [5, 10], method="trust-constr", constraints=cons)
    print(result_trust)

    print_plot([[result_cobyla.x[0], result_cobyla.x[1], result_cobyla.fun], [result_trust.x[0], result_trust.x[1], result_trust.fun]])
