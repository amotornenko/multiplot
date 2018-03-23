# Anton Motornenko, 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import AutoMinorLocator, LogLocator, MultipleLocator, FixedLocator, LinearLocator, FormatStrFormatter
from matplotlib import gridspec

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


#font parameters
params = {'axes.labelsize': 22,'axes.titlesize':22, 'text.fontsize': 22, 'legend.fontsize': 22, 'xtick.labelsize': 22, 'ytick.labelsize': 22}

rows = 5
columns = 5
#number of plots
plotN = rows*columns
#ticks label positioning (if needed)
x_ticks = [5,9,13,17]
y_labels = y_ticks = [0.0,0.2,0.4,0.6,0.8,1.0]

#sample of symbols to generate random labels
sample = list('1234567890qwertyuiopasdfghjklzxcvbnm')

#initialize array for labels
labels = [[],[]]

fig = plt.figure(figsize=(10.5,8))

# set height ratios for sublots
gs = gridspec.GridSpec(rows, columns, height_ratios=np.ones(rows))

ax = []

for i in range(plotN):
    column = i%columns
    row = i//columns
    
    if(row == 0):
        ax.append(plt.subplot(gs[i]))
    else:
        ax.append(plt.subplot(gs[i], sharex = ax[i-1]))
        
    if(column == 0):
        ax[-1].set_ylabel(r'row %d' %(i//rows))
    else:
        plt.setp(ax[-1].get_yticklabels(), visible=False)
        
    if(row+1 == rows):
        ax[-1].set_xlabel(r'column %d' %(column))
    else:
        plt.setp(ax[-1].get_xticklabels(), visible=False)
        
    ax[-1].text(.5,.85,r'text (%d, %d)' %(column, row),
        horizontalalignment='center',
        transform=ax[-1].transAxes)
    name = ''.join(np.random.choice(sample, 5))
    
    #plot with random data and label
    l, = ax[-1].plot(np.linspace(5,17,20),np.random.random_sample(20),
                     c=cm.hsv(i/plotN), label = name)
    labels[0].append(l)
    labels[1].append(name)
    
    #playaround with ticks
    ax[-1].yaxis.set_ticks_position('both')
    
    #Set custom ticks positions
    ax[-1].set_xticks(x_ticks)
    ax[-1].set_yticks(y_ticks)
                  
    ax[-1].get_xaxis().set_minor_locator(AutoMinorLocator())
    ax[-1].get_yaxis().set_minor_locator(AutoMinorLocator())
                  
    ax[-1].tick_params(which = 'major', direction='in', bottom ='on', top ='on', right ='on', left ='on', length=4)
    ax[-1].tick_params(which = 'minor', direction='in', bottom ='on', top ='on', right ='on', left ='on', length=2)
    
    #remove label from last vertical tick
    # if(column==0):
    #     yticks = ax[-1].yaxis.get_major_ticks()
    #     yticks[0].label1.set_visible(False)
    
    #set axss limits
    ax[-1].axis([3, 19, -0.1, 1.1]) 

legend = ax[0].legend(labels[0], labels[1], bbox_to_anchor=(0., 1.02, columns, 0.102), loc=3,
       ncol=columns, mode="expand", borderaxespad=-.0, handletextpad = 0.5, 
       numpoints = 1, framealpha=1.0, fancybox = False)
legend.get_frame().set_edgecolor('black')


# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0,wspace=.0)
#plot title
#plt.title(r'${\bf Header}$', y=5, x=-1.5)
#export plot to pdf
plt.savefig('multiplot.pdf', format='PDF', bbox_inches='tight')
plt.savefig('multiplot.png', format='PNG', bbox_inches='tight')

plt.show()
