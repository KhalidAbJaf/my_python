from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from numpy import (linspace, meshgrid, pi, sin, sqrt)

u = linspace(-4*pi, 4*pi, 50); x,y = meshgrid(u,u); r = sqrt(x**2 + y**2); z = sin(r)/r; fig = figure();
ax = Axes3D(fig); ax.plot_surface(x,y,z,rstride=1, cstride=1)

show()