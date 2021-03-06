__author__ = 'nico'

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])             #create the graphing application
w = gl.GLViewWidget()                    #create widget
w.opts['distance'] = 20                  #start distance from where one looks at the plot
w.show()                                 #show widget
w.setWindowTitle('pyqtgraph example(with mild changes): GLScatter Plot Item')

# g = gl.GLGridItem()                    #creates a grid item
# w.addItem(g)                           #adds the grid item (if w.addItem is called again the item is overwritten. Somehow this only holds for the grid item...)

##
##  First example is a set of points with pxMode=False
##  These demonstrate the ability to have points with real size down to a very small scale
##
pos = np.empty((53, 3))
size = np.empty((53))
color = np.empty((53, 4))
pos[0] = (1,0,0); size[0] = 0.5;   color[0] = (1.0, 0.0, 0.0, 0.5)
pos[1] = (0,1,0); size[1] = 0.2;   color[1] = (0.0, 0.0, 1.0, 0.5)
pos[2] = (0,0,1); size[2] = 2./3.; color[2] = (0.0, 1.0, 0.0, 0.5)

z = 0.5
d = 6.0
for i in range(3,53):
    pos[i] = (0,0,z)
    size[i] = 2./d
    color[i] = (0.0, 1.0, 0.0, 0.5)
    z *= 0.5
    d *= 2.0

sp1 = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)     #creates a scatter plot item
#If pxMode=True, spots are always the same size regardless of scaling, and size is given in px.
#Otherwise, size is in scene coordinates and the spots scale with the view. Default is True
#For more information see: http://www.pyqtgraph.org/documentation/graphicsItems/scatterplotitem.html

# sp1.translate(5,0,0)                      #puts item at different position in widget
w.addItem(sp1)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()