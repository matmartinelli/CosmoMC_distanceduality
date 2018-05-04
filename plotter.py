import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here,'../python/')))
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib.backend_bases import register_backend
register_backend('pdf', FigureCanvasPgf) 
import planckStyle as s
from pylab import *

#g = s.getSinglePlotter(plot_data='plot_data/')


import GetDistPlots






import planckStyle



g = planckStyle.getSinglePlotter(chain_dir = './chains', ratio=.7)

roots = ['BAO_ddt','union_ddt','BAO+union_ddt']
g.settings.solid_contour_palefactor = 0.8
g.plot_2d(roots, 'omegam', 'sigma8', filled=[True,True,False], colors=['#FFB300','#8E001C','black'])#, lims=[0.25, 0.45, 0.6, 1.1])#0.6, 0.9])
labels = [r'BAO','SN','BAO+SN']


g.add_legend(labels, legend_loc='upper left',fontsize='small');#, colored_text=True);

#plt.show()
g.export('results_plots/ddt.pdf')
