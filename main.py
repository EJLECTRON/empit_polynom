import time

from .polynom import Polynom
from .solvers import AnalyticalSolver, NumericIntegralEstimation, MonteCarloIntegralEstimation
from .tests.test_integration import expected_integral

def main():
    coeffs_str = input("Enter polynomial coefficients (space-separated, lowest degree first): ")
    coeffs = [float(c.strip()) for c in coeffs_str.strip().split(" ")]
    polynom = Polynom(coeffs)

    a = float(input("Enter interval start (a): "))
    b = float(input("Enter interval end (b): "))
    interval = (a, b)

    print("\nSolving integral of", polynom, "over interval", interval, "\n")

    expected = expected_integral(polynom, interval)
    print("Numpy solution: ", expected)

    # Analytical solver
    start = time.time()
    result_analytic = AnalyticalSolver().integrate(polynom, interval)
    print("Analytical:", result_analytic, "Time:", time.time() - start)

    # Numeric solver
    start = time.time()
    result_numeric = NumericIntegralEstimation().integrate(polynom, interval)
    print("Numeric:", result_numeric, "Time:", time.time() - start)

    # Monte Carlo solver
    start = time.time()
    result_mc = MonteCarloIntegralEstimation().integrate(polynom, interval)
    print("Monte Carlo:", result_mc, "Time:", time.time() - start)

    # Compare differences
    print("\nDifferences:")
    print("Analytic: ", abs(result_analytic - expected) / abs(expected) * 100)
    print("Numeric - Analytic:", abs(result_numeric - expected) / abs(expected) * 100)
    print("Monte Carlo - Analytic:", abs(result_mc - expected) / abs(expected) * 100)


if __name__ == "__main__":
    main()
