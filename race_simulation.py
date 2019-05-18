import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def trackSim(name, distance, time, nplayers, interval=1):
    """ Runs the track simulator!

    Parameters
    ----------
    name : str
        Your name (or whichever name you want your player to have).
    distance : int
        The length you want your player to run for (meters).
    time : int
        Your average time for the selected distance (seconds).
    nplayers : int
        The amount of runners you want to compete against.
    interval : int (default = 1)
        The time (in milliseconds) in between frames. Essentially, this
        parameter adjusts how long you want the race simulation to run.
        The lower this number, the shorter the duration. To run the simulation
        in real-time, the input value should be 1000.

    Returns
    -------
    A matplotlib animation with the race simulation.
    """
    #~~~~~~Bounds of the racetrack~~~~~~
    xlim = (0,distance+(0.5*distance))
    ylim = (0,nplayers+1)
    player_pos = nplayers/2 # starting position of the player

    #~~~~~~Figure Aesthetics~~~~~~
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
    plt.axvline(distance, color='k')
    plt.text(distance+(2), nplayers/1.5, 'Finish!', fontsize=20, rotation=90)

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

    frames = np.arange(0, distance, .001)

    limit = 0.2*time

    balls = []
    for n in np.arange(0, nplayers+1, 1):
        runner_pos = 0+n

        if runner_pos != player_pos:
            runner_time = random.randint(time-limit,time+limit)
            ball = Ball('runner '+str(n), 0, runner_pos, distance/runner_time)
            balls.append(ball)

    player_name = Ball(name, 0, player_pos, distance/time)

    balls.append(player_name)

    rankings = []
    ani = animation.FuncAnimation(fig, animate, frames, init_func=init,
                                  interval=interval, blit=True, repeat=False)
    plt.show()
