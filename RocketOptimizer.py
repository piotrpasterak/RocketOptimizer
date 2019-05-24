from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

y_1 = 1.11 * 10**(-9)
y_2 = 1.48 * 10**9
y_3 = 4.88 * 10**21


def goal_f(r):
    return y_1 * r[0]**2 * r[1]**3 * (y_2 + np.sqrt(y_2**2 - (y_3 / (r[0]**2 * r[1]**3))))


def restrict_f(x):
    return y_2**2 - (y_3 / (x[0]**2 * x[1]**3))


def print_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(10, 40000, 100)
    Y = np.arange(3, 40, 1)
    X, Y = np.meshgrid(X, Y)
    plt.title('Funkcja celu rakiety Saturn V')
    ax.set_xlabel("R")
    ax.set_ylabel("r")
    ax.set_zlabel("V")
    Z = goal_f([X, Y])

    ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)
    plt.show()


if __name__ == '__main__':
    """Main script loop.
    Zadanie optymalizacyjne:
    Promień dyszy silnika, oznaczany małą literą r,
    Promień zewnętrzny stopnia rakiety, oznaczany dużą literą R.
    """

    cons = [{'type': 'ineq', 'fun': restrict_f},
            {'type': 'ineq', 'fun': lambda x: x[0]},
            {'type': 'ineq', 'fun': lambda x: x[1]}]

    print(
        """
        Method COBYLA uses the Constrained Optimization BY Linear Approximation (COBYLA) method. 
        The algorithm is based on linear approximations to the objective function and each constraint. 
        The method wraps a FORTRAN implementation of the algorithm. 
        The constraints functions ‘fun’ may return either a single number or an array or list of numbers.
        """
    )

    result_cobyla = optimize.minimize(goal_f, [100, 10],method="COBYLA", constraints=cons)
    print(result_cobyla)

    print(
        """
        Method trust - constr is a trust - region algorithm for constrained optimization.
        It swiches between two implementations depending on the problem definition.
        It is the most versatile constrained minimization algorithm implemented in SciPy and the most appropriate for large-scale problems.
        This interior point algorithm, in turn, solves inequality constraints by introducing slack variables and solving a sequence of equality-constrained barrier problems for progressively smaller values of the barrier parameter.
        The previously described equality constrained SQP method is used to solve the subproblems with increasing levels of accuracy as the iterate gets closer to a solution.
    
        Function plot suggesting that function is close to be linear, at least close to this in significant number of regions.
        That could means that 'trust-constr' method is not best choice for this case (bases on gradient and is time consuming here.).
        
        It takes long time, please be waiting.
        """)

    result_trust = optimize.minimize(goal_f, [100, 10], jac='2-point', method="trust-constr", constraints=cons,
                             options={'maxiter': 100000})
    print(result_trust)

    print_plot()
