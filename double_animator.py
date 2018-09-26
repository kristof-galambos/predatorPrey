"""
runs the simulation and outputs both the animated matplotlib plots of the populations and the movements of the animals
but it's running really slowly, because matplotlib can't animate that many rectangles so fast
"""

from universe import Universe

import matplotlib.pyplot as plt
import matplotlib.animation as animation


#input parameters
GRID_SIZE = 30
INITIAL_PREDATORS = 50
INITIAL_PREYS = 50

#initialise universe
u = Universe(GRID_SIZE, INITIAL_PREDATORS, INITIAL_PREYS)

#initialise graphics
fig = plt.figure('predator prey model', figsize=(10,10))
ax1 = fig.add_subplot(2 ,1, 1)
ax2 = fig.add_subplot(2, 1, 2)
plot1_x = []
plot1_y1 = []
plot1_y2 = []

def animate(i):
    u.move_animals()
    u.prepare_next_round()
    
    #plot 1 comes
    plot1_x.append(i)
    plot1_y1.append(len(u.predators))
    plot1_y2.append(len(u.preys))
    
    ax1.clear()
    ax1.plot(plot1_x, plot1_y1, 'r', label='predators')
    ax1.plot(plot1_x, plot1_y2, 'g', label='preys')
    ax1.legend()
    
    #plot 2 comes
    ax2.clear()
    ax2.axis([0, GRID_SIZE, 0, GRID_SIZE])
    for pred in u.predators:
        ax2.add_artist(plt.Rectangle((pred.cell.x, pred.cell.y), 1, 1, fc='r'))
    for prey in u.preys:
        ax2.add_artist(plt.Rectangle((prey.cell.x, prey.cell.y), 1, 1, fc='g'))
    
#run graphics 
ani = animation.FuncAnimation(fig, animate, interval=1)

