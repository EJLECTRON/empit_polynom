import unittest
import numpy as np

from empit_polynom.polynom import Polynom
from empit_polynom.solvers import AnalyticalSolver, NumericIntegralEstimation, MonteCarloIntegralEstimation

N_TESTS = 1
ACCEPTED_ERROR = 0.25


def generate_random_polynomial(max_degree=5):
    """
    Support function to generate random polynomial for test

    Args:
        max_degree (int, optional): Defaults to 5.

    Returns:
        Polynom: Polynom with random coefficients and length
    """
    coeffs = np.random.uniform(-100, 100, size=np.random.randint(2, max_degree+2))
    coeffs = np.round(coeffs, 6)
    return Polynom(coeffs.tolist())


def generate_random_interval():
    a, b = np.random.uniform(-100, 100, size=2)

    return (a, b)


def expected_integral(polynom: Polynom, interval: tuple[float, float]):
    """
    Calculates value of integral using numpy.

    Returns:
        float: This value is considered as correct value, which will be used for comparation
    """
    coeffs = np.array(polynom[::-1])

    reverted_polynom = np.poly1d(coeffs)
    antipolynom = np.polyint(reverted_polynom)

    return np.polyval(antipolynom, interval[1]) - np.polyval(antipolynom, interval[0])


class TestIntegralSolvers(unittest.TestCase):

    def test_random_polynomials(self):
        analytic_solver = AnalyticalSolver()
        numeric_solver = NumericIntegralEstimation()
        mc_solver = MonteCarloIntegralEstimation()

        for _ in range(N_TESTS):
            p = generate_random_polynomial()
            interval = generate_random_interval()
            expected = expected_integral(p, interval)

            try:
                # Analytical solver
                result_analytic = analytic_solver.integrate(p, interval)
                rel_error_analytic = abs(result_analytic - expected) / abs(expected) * 100
                print(f"Analytic rel error: {rel_error_analytic:.6f}%")
                self.assertLess(rel_error_analytic, ACCEPTED_ERROR)

                # Numeric solver
                result_numeric = numeric_solver.integrate(p, interval)
                rel_error_numeric = abs(result_numeric - expected) / abs(expected) * 100
                print(f"Numeric rel error: {rel_error_numeric:.6f}%")
                self.assertLess(rel_error_numeric, ACCEPTED_ERROR)

                # Monte Carlo solver
                result_mc = mc_solver.integrate(p, interval)
                rel_error_mc = abs(result_mc - expected) / abs(expected) * 100
                print(f"Monte Carlo rel error: {rel_error_mc:.6f}%")
                self.assertLess(rel_error_mc, ACCEPTED_ERROR)

            except Exception as e:
                print(e)
                self.assertTrue(str(e) == "Invalid interval, try again")

if __name__ == "__main__":
    unittest.main()
