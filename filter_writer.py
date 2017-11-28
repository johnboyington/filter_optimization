'''
This code will be great.
'''

import numpy as np
import os
import time
import filter_functions as fil
from itertools import product

initial_time = time.time()

#create list of every filter permutation possible
names = []
for item in product(['1', '2', '3'], repeat=10):
    names.append(''.join(item))
for item in range(87):
    names.append('1111111111')
names = np.array(names).reshape(-1, 256)



def runBatch(name_list):
    init_bat_time = time.time()
    for name in name_list:
        fil.createInputs(name)
    for name in name_list:
        os.system('qsub {}n.qsub'.format(name))
        os.system('qsub {}p.qsub'.format(name))
    time.sleep(75)
    for name in name_list:
        n_tally = fil.readNeutron(name)
        g_tally =  fil.readGamma(name)
        if len(n_tally) + len(g_tally) == 6:
            with open('filter_data.txt', 'a') as F:
                    F.write('{}  {:11.9f}  {:11.9f}  {:11.9f}\n'.format(name, n_tally[0] / n_tally[1], (n_tally[1]) / (n_tally[3] + g_tally[1]), n_tally[0]))
        else:
            print 'Problem with file {}'.format(name)
            with open('filter_data.txt', 'a') as F:
                F.write('{} trouble'.format(name))
    fil.remove()
    print 'Batch finished in {} seconds.'.format(time.time() - init_bat_time)


for i in range(16, len(names)):
    print 'Starting Batch {} of {}'.format(i, len(names))
    runBatch(names[i])


print 'Script finished in {} seconds.'.format(time.time() - initial_time)