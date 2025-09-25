from .polynom import Polynom, IntegralSolver

import numpy as np

# TODO: create your solver classes here using the IntegralSolver as a base class


class AnalyticalSolver(IntegralSolver):
    @staticmethod
    def __prima(polynom: Polynom, x: float):
        # value of primitive function of given polynom in the given point
        return sum(polynom[i] / (i + 1) * x**(i + 1) for i in range(len(polynom)))


    def integrate(self, polynom: Polynom, interval: tuple[float, float]):
        if interval[0] > interval[1]:
            raise Exception("Invalid interval, try again")

        result = self.__prima(polynom, interval[1]) - self.__prima(polynom, interval[0])
        return round(result, 3)


class NumericIntegralEstimation(IntegralSolver):
    def integrate(self, polynom: Polynom, interval: tuple[float, float]):
        if interval[0] > interval[1]:
            raise Exception("Invalid interval, try again")

        n_points = np.random.randint(500_000, 1_000_000)

        x, dx = np.linspace(interval[0], interval[1], n_points, endpoint=False), (interval[1] - interval[0]) / n_points
        y = np.array([polynom(el) for el in x], dtype=float)

        integral_estimate = np.sum(y * dx)
        return round(integral_estimate, 3)


class MonteCarloIntegralEstimation(IntegralSolver):
    def integrate(self, polynom: Polynom, interval: tuple[float, float]):
        if interval[0] > interval[1]:
            raise Exception("Invalid interval, try again")
        
        rng, n_samples = np.random.default_rng(), np.random.randint(500_000, 1_000_000)
        x_samples = rng.uniform(interval[0], interval[1], size=n_samples)
        y_samples = np.array([polynom(el) for el in x_samples], dtype=float)

        integral_estimate = (interval[1] - interval[0]) * np.mean(y_samples)
        return round(integral_estimate, 3)
