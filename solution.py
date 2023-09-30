# import
import itertools as it
import numpy as np
import matplotlib.pyplot as plt

# define constants:
from math import sin, cos, pi, sqrt

k: float = 100
g: float = 9.81
m: float = 0.2
t: float = 0.5
fs: float = 0.1
fk: float = 0.05

# helper function for returning the solutions to a quadratic
def quadratic_formula(a: float, b: float, c: float) -> tuple[float, float]:
    discriminant = sqrt(b * b - 4 * a * c)
    mid = -b / (2 * a)
    return (
        mid - discriminant / (2 * a),
        mid + discriminant / (2 * a)
    )

# defining the range for where the block will stop
# note that |upper| < |lower|
# this is because x is the distance below the spring

def lower_bound() -> float:
    return (m * g / k) * (sin(t) + fs * cos(t))

def upper_bound() -> float:
    return (m * g / k) * (sin(t) - fs * cos(t))

def stops(x: float, upper: float, lower: float) -> bool:
    return upper <= x <= lower

# determining the new x given the starting x
# precondition: stops(x) is false

def iter_up(x: float) -> float:
    a = 0.5 * k
    b = -fk * m * g * cos(t) - m * g * sin(t)
    c = -0.5 * k * x * x + fk * m * g * cos(t) * x + m * g * sin(t) * x
    return quadratic_formula(a, b, c)[0]

def iter_down(x: float) -> float:
    a = 0.5 * k
    b = fk * m * g * cos(t) - m * g * sin(t)
    c = -0.5 * k * x * x - fk * m * g * cos(t) * x + m * g * sin(t) * x
    return quadratic_formula(a, b, c)[1]

def iterate(x: float) -> float:
    history = [x]
    lower = lower_bound()
    upper = upper_bound()

    # base case: x is stop
    if stops(x, upper, lower):
        return x

    # determine which order
    functions = it.cycle([iter_up, iter_down])
    if x < upper:
        next(functions)

    # loop until
    max_iter = 2
    while not stops(x, upper, lower):
        x = next(functions)(x)
        history.append(x)

        max_iter = max_iter - 1
        if max_iter < 0:
            break

    print(history)
    return x

def test():
    x = iterate(0.033)
    print(upper_bound(), lower_bound())
    print(x)

def main():
    print(upper_bound(), lower_bound())
    # create graph
    x = np.arange(0, 0.025, 0.001)
    y = [iterate(a) for a in x]
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    test()
    # main()
