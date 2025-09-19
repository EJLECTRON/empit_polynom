class Polynom(list):
    def __init__(self, coeffs):
        super().__init__(coeffs)


    def __repr__(self):
        return "Polynom({})".format(super().__repr__())


    def __add__(self, other):
        if not isinstance(other, Polynom):
            raise Exception("Value error while adding polynom with entity other than polynom")

        len_self, len_other = len(self), len(other)
        max_len, sum_coeffs = max(len_self, len_other), []

        for i in range(max_len):
            sum_coeffs.append(
            (self[i] if i < len_self else 0) +
            (other[i] if i < len_other else 0)
            )

        return Polynom(sum_coeffs)


    def __sub__(self, other):
        if not isinstance(other, Polynom):
            raise Exception("Value error while subtracting polynom with entity other than polynom")

        len_self, len_other = len(self), len(other)
        max_len, diff_coeffs = max(len_self, len_other), []

        for i in range(max_len):
            diff_coeffs.append(
                (self[i] if i < len_self else 0) -
                (other[i] if i < len_other else 0)
            )

        return Polynom(diff_coeffs)


    def __mul__(self, other):
        if not isinstance(other, Polynom):
            raise Exception("Value error while multiplying polynom with entity other than polynom")

        len_self, len_other = len(self), len(other)
        product_coeffs = [0] * (len_self + len_other - 1)
        
        for pow_self, coef_self in enumerate(self):
            for pow_other, coef_other in enumerate(other):
                product_coeffs[pow_self + pow_other] += coef_self*coef_other
        
        return Polynom(product_coeffs)


    def __call__(self, x):
        result = 0
        for i in range(len(self)):
            result += self[i] * x**i
        return result


    def __str__(self):
        terms = []
        for i, coeff in enumerate(self):
            if coeff == 0:
                continue
            term = str(abs(round(coeff, 3)))
            if i > 0:
                term += "*x"
            if i > 1:
                term += "^{}".format(i)
            if coeff < 0:
                term = "-" + term
            elif terms:
                term = "+" + term
            terms.append(term)
        if not terms:
            return "0"
        return "".join((terms))


    def integrate(self, interval: tuple[float, float], solver: "IntegralSolver"):
        return solver.integrate(self, interval)


class IntegralSolver:
    def integrate(self, polynom: Polynom, interval: tuple[float, float]):
        raise NotImplementedError
