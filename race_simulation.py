import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(10,10))
fig.set_dpi(100)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 1.0, fc='y')

finish_line = 5
rankings = []

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = i
    y = 5
    
    patch.center = (x, y)
    if x >= finish_line: 
        rankings.append(patch)
        plt.close()
    else:
        patch.center = (x, y)
    
    return patch,


anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=10,
                               interval=500,
                               blit=True,
                               repeat=False)

plt.show()
print(rankings)
