from math import e, exp, ceil
import sympy as sp
from sympy import cos, lambdify, log


def bisection_method(polynom, start, end):
    f = lambdify(x, polynom)
    max_iterations = log(eps/(end-start), exp(1))
    max_iterations /= -log(2, exp(1))
    max_iterations = ceil(max_iterations)
    x_l = start
    x_r = end
    counter = 0
    x_c = (x_l + x_r) / 2
    while abs(x_r - x_l) > eps:
        counter += 1
        x_c = (x_l + x_r) / 2
        if(f(x_c) * f(x_r)) < 0:
            x_l = x_c
        elif(f(x_c) * f(x_r)) > 0:
            x_r = x_c
        if counter > max_iterations:
            print("cannot resolve")
            return None
    return [x_c, counter]


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
            print("%.5f" % i[0], end=", ")
            print(f"found in {i[1]} attempts")


x = sp.symbols('x')
polynomial = (x**2*e**((-x)**2+5*x-3))*(3*x-5)
start = 0
end = 3
eps = 10**-10
print("Newton Raphson method")
main(newton_raphson)
print("Secant method")
main(secant_method)
