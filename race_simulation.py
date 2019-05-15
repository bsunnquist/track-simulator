import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# bounds of the room
xlim = (0,30)
ylim = (0,20)

finish_line = 20

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()

class Ball(object):
    
    def __init__(self, name, x, y, v):
        """
        :param x y: Initial position.
        :param v: Initial velocity.
        """
        self.v = float(v)
        self.x = float(x)
        self.y = float(y)
        self.name = name

        self.scatter, = ax.plot([], [], 'o', markersize=20)
        
    def update(self):
        self.x += self.v
        self.scatter.set_data(self.x, self.y)
        if self.x >= finish_line:
            if self.name not in rankings:
                print(self.name)
                rankings.append(self.name)
            self.scatter.set_data(finish_line, self.y)

    def start(self):
        self.scatter.set_data(self.x, self.y)

def init():
    return []

def animate(t): 

    if t==0.0:
        print('starting')
        for ball in balls:
            ball.start()
    else:
        for ball in balls:
            ball.update()
            if len(rankings)==len(balls):
                ani.event_source.stop()
                print(rankings)
    
    # have to return an iterable
    return [ball.scatter for ball in balls]

balls = [Ball('bob', 0, 2, .3), 
         Ball('jenny', 0, 4, .4), 
         Ball('ben', 0, 6, .5)]

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
rankings = []
ani = animation.FuncAnimation(fig, animate, np.arange(0,finish_line,0.001), init_func=init, interval=100, blit=True, repeat=False)
plt.show()
