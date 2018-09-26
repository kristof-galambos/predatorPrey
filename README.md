This is a Lotka Volterra predator prey model written in Python.

Predators eat the preys, when there are a lot of preys, they have a lot of food, so their population grows. When the predator population has grown, they eat all the preys, the prey population drops, so the predators run out of food. The predators die of hunger so their population starts to drop. When the predator population dropped, preys can proliferated easily, so their population grows, there will be enough food for the predators again, and the cycle starts from the beginning.
The result is a nice cyclic fluctuation of the population sizes, which can appears to match theoretical predictions quite well.

There are 2 different types of output: 1. plot of the population sizes of predators and preys and 2. animation of movement of the animals, predators are read, preys are green.

There is a separate launcher file for all different kinds of output. Input parameters are mostly hardcoded into these launcher files.

List of files:

Implementation: universe.py, animals.py, cell.py

Launchers:animator.py, animated_plotter.py, double_animator.py, plotter.py, gui.py
