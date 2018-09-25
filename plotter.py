

from universe import Universe

import matplotlib.pyplot as plt

times = list(range(300))
predators = []
preys = []

u = Universe(50, 50, 50)
for time in times:
    print(('\nNEW ROUND:', time))
#    print 'predators:', u.predators
#    print
    u.move_animals()
    u.prepare_next_round()
    
#    print 'predators:', len(u.predators)
#    print 'preys:', len(u.preys)
    predators.append(len(u.predators))
    preys.append(len(u.preys))
    
plt.figure(1)
plt.plot(times, predators, 'r', lw=2, label='predators')
plt.plot(times, preys, 'g', lw=2, label='preys')
plt.xlabel('number of passed rounds')
plt.ylabel('number of living animals')
plt.legend()


