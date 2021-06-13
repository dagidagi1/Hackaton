import sympy as sp
from sympy import cos
from math import e
from main import suffix
def rumb(poly, start, end, eps):
    index = 0
    def simpson(polynomial, start, end, n):
        h = (end - start) / n
        f = sp.lambdify(x, polynomial)
        result = f(start)
        start += h
        counter = 4
        while start < end:
            if counter == 4:
                result += 4 * f(start)
                counter = 2
            else:
                result += 2 * f(start)
                counter = 4
            start += h
        result += f(end)
        result *= (h / 3)
        return result

    t_h = []
    n = 1
    t_h.append([simpson(poly,start,end,n)])
    flag = True
    i = 1
    while flag:
        n *= 2
        tmp = []
        for j in range(i + 1):
            if j == 0:
                tmp.append(simpson(poly,start,end,n))
            else:
                tmp.append(tmp[j - 1] + 1 / ((4 ** j) - 1) * (tmp[j - 1] - t_h[i - 1][j - 1]))
        t_h.append(tmp)
        if abs(t_h[-1][-1] - t_h[-2][-1]) < eps:
            flag = False
        i += 1
    for _ in t_h:
        print(_)
    return t_h[-1][-1], len(t_h)
x = sp.symbols('x')
pol = cos(2*e ** (-2*x))/ (2*x**3 + 5*x**2 - 6)
start = -0.5
end = 0.5
res, num = rumb(pol,start,end,0.000001)
print("Romberg-Simpson solved in {0} extrapulations, result = {1}".format(num,suffix(res,131931)))