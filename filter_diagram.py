import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Arrow


class Diagram(object):

    def __init__(self):
        self.draw()

    def draw(self):
        fig = plt.figure(0)
        ax = fig.add_subplot(111)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xlim(-10, 25)
        ax.set_ylim(-10, 10)

        slabs = [0, 2, 4, 6, 8, 10, 12, 20]
        mats = [1, 2, 1, 2, 4, 1, 2, 2, 2, 2]
        ecolors = ['k', 'darkgreen', 'darkblue', 'maroon', 'darkgoldenrod']
        fcolors = ['k', 'forestgreen', 'blue', 'red', 'goldenrod']
        hatches = ['//', '\\', '//', '\\', '//']

        # add the filter slabs
        for i in range(len(slabs) - 1):
            ax.add_patch(Polygon([[slabs[i], -5], [slabs[i+1], -5], [slabs[i+1], 5], [slabs[i], 5]], closed=True,
                                 fill=True, hatch=hatches[mats[i]], edgecolor=ecolors[mats[i]], facecolor=fcolors[mats[i]],
                                 linewidth=0.8))

        # add the beamport
        ax.add_patch(Ellipse((0, 0), 0.5, 2.54, fill=False))
        ax.add_patch(Arrow(0, 0, 3, 0, width=2.5, color='black'))
        ax.add_patch(Polygon([[slabs[-1], -0.5], [slabs[-1]+1, -0.5], [slabs[-1]+1, 0.5], [slabs[-1], 0.5]], closed=True,
                                 fill=True, edgecolor='black', facecolor='black',
                                 linewidth=0.8))
        ax.plot([-5, 0], [1.27, 1.27], 'k', linewidth=0.8)
        ax.plot([-5, 0], [-1.27, -1.27], 'k', linewidth=0.8)
        # text
        ax.text(21, 2, 'Detector')
        ax.text(-5, 2, 'Source')
        
        ax.axes.get_yaxis().set_visible(False)

        fig.savefig('filter.png', dpi=300)
        

Diagram()