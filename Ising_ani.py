import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

dim = 10
frames = 10

grid = np.zeros((dim, dim))

def animate(i):
    grid[:] = np.random.choice([0, 1], size = (dim, dim))
    im = ax.imshow(grid, cmap = "bwr")

    return [im]

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

ani = FuncAnimation(fig, animate, frames = frames, interval = 200, blit = True)
ani.save("l_Ising.gif", writer = "pillow", fps = 5)
