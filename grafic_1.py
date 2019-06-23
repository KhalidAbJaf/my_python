import math
import pylab
from matplotlib import mlab

def func(x):
    """
    sin(x)
    """
    return math.sin()

xmin = -10.0
xmax = 10.0

dx = 0.01

xlist = mlab.frange(xmin, xmax, dx)
ylist = [func(x) for x in xlist]

pylab.plot(xlist, ylist)

pylab.show()