import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Arrow


class Diagram(object):

    def __init__(self, m, name, ft, ng):
        self.draw(m, name, ft, ng)

    def draw(self, m, name, ft, ng):
        fig = plt.figure(0)
        ax = fig.add_subplot(111)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xlim(-10, 25)
        ax.set_ylim(-10, 10)

        slabs = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        mats = m
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

        # add ratio info
        ax.text(-5, -8, 'FT Ratio: {}'.format(ft))
        ax.text(11, -8, 'NG Ratio: {}'.format(ng))

        ax.axes.get_yaxis().set_visible(False)

        fig.savefig('{}.png'.format(name), dpi=300)
        plt.close(fig)


if __name__ == '__main__':
    m = [1, 2, 1, 2, 4, 1, 2, 2, 2, 2]
    Diagram(m, 'filter', 0.9, 1.5)
