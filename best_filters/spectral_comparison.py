from spectrum import Spectrum
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from nebp_spectrum import FluxNEBP


# nice plots
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})

# load bin structure
bins = np.loadtxt('scale56.txt')

# load nebp neutron spectrum
nebp_spectrum = FluxNEBP(250)


# calculate neutron scaling factor
tally_area = tally_area = np.pi * (1.27 ** 2)
cn = 2.54 / (200 * 1.60218e-13 * tally_area)
cn *= 7.53942E-8
cn *= 250  # normalize to 250 W(th)

# load filtered neutron data
n_fil = np.loadtxt('n_fil.txt')
n_fil = n_fil.T[1][1:] * cn
n_fil = Spectrum(bins, n_fil)

# calculate gamma scaling factor
tally_area = tally_area = np.pi * (1.27 ** 2)
cg = 8.32 / (200 * 1.60218e-13 * tally_area)
cg *= 250  # normalize to 250 W(th)

# load nebp gamma data
g_spectrum = np.loadtxt('gdata_total.txt')
g_spectrum = g_spectrum.T[1][1:] * cg
g_spectrum = Spectrum(bins, g_spectrum)

# load filtered gamma data
g_fil = np.loadtxt('g_fil.txt')
g_fil = g_fil.T[1][1:] * cg * 6.90356E-8
g_fil = Spectrum(bins, g_fil)


def plot():
    # create neutron plot
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Energy $MeV$')
    ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
    ax.set_xlim(1E-9, 20)
    ax.set_ylim(1E0, 1E13)

    # plot original
    style = {'color': 'indigo', 'linewidth': 0.7, 'linestyle': '-', 'label': 'Unfiltered Neutron'}
    ax.plot(nebp_spectrum.step_x, nebp_spectrum.step_y, **style)

    style = {'color': 'red',  'linewidth': 0.7, 'linestyle': '-', 'label': 'Unfiltered Gamma'}
    ax.plot(g_spectrum.step_x, g_spectrum.step_y, **style)

    # plot filtered
    style = {'color': 'blue',  'linewidth': 0.7, 'linestyle': '-', 'label': 'Filtered Neutron'}
    ax.plot(n_fil.step_x, n_fil.step_y, **style)

    style = {'color': 'green',  'linewidth': 0.7, 'linestyle': '-', 'label': 'Filtered Gamma'}
    ax.plot(g_fil.step_x, g_fil.step_y, **style)

    ax.legend()
    fig.savefig('filtered_spectra.png', dpi=300)

    plt.close(fig)

plot()
