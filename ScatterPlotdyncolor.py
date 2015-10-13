__author__ = 'nico'

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])             #create the graphing application
w = gl.GLViewWidget()                    #create widget
w.opts['distance'] = 100                  #start distance from where one looks at the plot
w.show()                                 #show widget
w.setWindowTitle('pyqtgraph example(with mild changes): GLScatter Plot Item')

##
##  Second example shows a volume of points with rapidly updating color
##  and pxMode=True
##

pos = np.random.random(size=(100000,3))
pos *= [10,-10,10]
pos[0] = (0,0,0)

color = np.ones((pos.shape[0], 4))
d2 = (pos**2).sum(axis=1)**0.5
size = np.random.random(size=pos.shape[0])*10
sp2 = gl.GLScatterPlotItem(pos=pos, color=(1,1,1,1), size=size)
sp2.translate(0,20,0)
phase = 0.

w.addItem(sp2)

def update():
    ## update volume colors
    global phase, sp2, d2
    s = -np.cos(d2*2+phase)
    color = np.empty((len(d2),4), dtype=np.float32)
    color[:,3] = np.clip(s * 0.1, 0, 1)
    color[:,0] = np.clip(s * 3.0, 0, 1)
    color[:,1] = np.clip(s * 1.0, 0, 1)
    color[:,2] = np.clip(s ** 3, 0, 1)
    sp2.setData(color=color)
    phase -= 0.1


t = QtCore.QTimer()
t.timeout.connect(update)
t.start(50)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()