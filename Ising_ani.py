import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import numpy as np

grid = np.zeros([10, 10, 10])

dim = len(grid)

for t in range(dim):
    for i in range(dim):
        for j in range(dim):
            r = np.random.rand()
            if r < 0.5:
                grid[t, i, j] = 0
            else:
                grid[t, i, j] = 1

def animate(i):
    ax.clear()
    ax.imshow(grid[i])
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    return fig

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames = 10)
ani.save("l_Ising.gif", writer = "pillow", fps = 5)
