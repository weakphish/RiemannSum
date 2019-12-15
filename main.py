import math
import numpy

# define functions used for calculations


def func(x):
    return ((x * x) / (math.log(x)))


def deltax(a, b, n):
    return ((b - a) / (n))


def calc_points(a, b, dx):
    points = []
    for i in numpy.arange(a, b, dx):
        points.append(i)
    return points


def approximate(dx, function, points):
    operated_points = []

    for i in points:
        f = function(i)
        operated_points.append(f)

    approx = dx * (sum(operated_points))

    return approx


# perform calculations and gather user input

print("Function = (x^2)/(ln(x))\n")

a = int(input("Starting point: "))
b = int(input("End point: "))
n = int(input("How many intervals? "))

dx = deltax(a, b, n)

points = calc_points(a, b, dx)

print("Points:")
for i in points:
    print(i)

approx_area = approximate(dx, func, points)
print("Approximate area under curve between points %s,%s: %s" % (a, b, approx_area))
