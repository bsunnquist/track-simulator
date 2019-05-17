import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#~~~~~~Future Input Parameters~~~~~~
distance = 400 # meters
time     = 60  # seconds
nplayers = 20  # players

#~~~~~~Bounds of the racetrack~~~~~~
xlim = (0,distance+(0.5*distance))
ylim = (0,nplayers)

#~~~~~~Figure Aesthetics~~~~~~
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
plt.axvline(distance, color='k')
plt.text(distance+1, 12, 'Finish!', fontsize=20, rotation=90)

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
        if self.x >= distance:
            if self.name not in rankings:
                print(self.name)
                rankings.append(self.name)
            self.scatter.set_data(distance, self.y)

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

# calculating v
v = distance/time
#                           this # tells you by how much X is going to increase every frame
#                           example: .3 means X is going up by .3 every 1000ms (which is the interval)
#
balls = [Ball('bob', 0, 2, .3),
         Ball('jenny', 0, 4, v),
         Ball('ben', 0, 6, .5)]

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
rankings = []
ani = animation.FuncAnimation(fig, animate, np.arange(0, distance, .01), init_func=init, interval=1, blit=True, repeat=False)
plt.show()
