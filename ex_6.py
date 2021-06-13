from math import e
import sympy as sp
from sympy import cos, lambdify
from romberg import *


def newton_raphson(polynom, start, end):
    f = lambdify(x, polynom)
    f_dif = sp.diff(polynom, x)
    f_dif = lambdify(x, f_dif)
    counter = 0
    x_next = (start + end) / 2
    print("#\txr\t\t\t\tf(x)\t\t\t\tf'(x)")
    while abs(f(x_next)) > eps and x_next < end:
        counter += 1
        x_current = x_next
        print(f"{counter}\t{x_current}\t{f(x_current)}\t{f_dif(x_current)}")
        x_next = x_current - f(x_current)/f_dif(x_current)
    return [x_next, counter]


def secant_method(polynom, start, end):
    f = lambdify(x, polynom)
    x_current = start
    x_prev = end
    x_next = (start + end)/2
    counter = 0
    print("#\txr\t\t\t\txr+1\t\t\t\tf(xr)")
    while abs(x_current - x_prev) > eps and x_next < end:
        counter += 1
        x_next = (x_prev*f(x_current) - x_current*f(x_prev)) / (f(x_current) - f(x_prev))
        print(f"{counter}\t{x_current}\t{x_next}\t{f(x_current)}")
        x_prev = x_current
        x_current = x_next
    return [x_current, counter]


def main(method):
    global polynomial, start, end, x
    x_l = start
    func = sp.lambdify(x, polynomial)
    p_dif = sp.diff(polynomial, x)
    f_dif = sp.lambdify(x, p_dif)
    solution = []
    while x_l < end:
        if abs(func(x_l)) < eps:
            solution.append([x_l, 1])
        elif func(x_l)*func(x_l + 0.1) < 0:
            temp = method(polynomial, x_l, (x_l + 0.1))
            if temp is not None:
                if abs(func(temp[0])) < eps:
                    solution.append(temp)
        elif f_dif(x_l)*f_dif(x_l+0.1) < 0:
            temp = method(p_dif, x_l, (x_l + 0.1))
            if temp is not None:
                if abs(func(temp[0])) < eps:
                    solution.append(temp)
        x_l += 0.1
    if abs(func(end)) < eps:
        solution.append([end, 1])
    for i in solution:
        if i is not None:
            print(suffix(i[0]), end=", ")
            print(f"found in {i[1]} attempts")


x = sp.symbols('x')
polynomial = cos(2 * e ** (-2 * x)) / (2 * x ** 3 + 5 * x ** 2 - 6)
start = -1.1
end = 2
eps = 10**-5
print("Newton Raphson method")
main(newton_raphson)
print("Secant method")
main(secant_method)
start = -0.4
end = 0.4
print("Romberg-Simpson:")
res,num = rumb(polynomial,start,end,eps)
print("Romberg-Simpson solved in {0} extrapulations, result = {1}".format(num,suffix(res)))
