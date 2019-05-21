import argparse
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def trackSim(name, distance, time, nplayers=10, interval=1):
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
    plt.style.use('seaborn-pastel')

    class Ball(object):

        def __init__(self, input_name, x, y, v):
            """
            :param x y: Initial position.
            :param v: Initial velocity.
            """
            self.v = float(v)
            self.x = float(x)
            self.y = float(y)
            self.name = input_name

            self.scatter, = ax.plot([], [], 'o', markersize=20)

            #self.text, = ax.annotate(str(self.name), xy=([], []))

        def update(self):
            self.x += self.v
            self.scatter.set_data(self.x, self.y)
            #self.text.set_text(self.x, self.y)

            if self.x >= distance:
                self.scatter.set_data(distance, self.y)
                if self.name not in rankings:
                    final_time = np.round((1/self.v)*distance, 2)
                    print(self.name, ' with a final time of '\
                                     +str(final_time)\
                                     +' seconds')
                    rankings.append(self.name)

        def start(self):
            self.scatter.set_data(self.x, self.y)

    def init():
        return []

    def animate(t):

        if t==0.0:
            print('starting!!')
            for ball in balls:
                ball.start()
        else:
            for ball in balls:
                ball.update()

                if len(rankings)==len(balls):
                    ani.event_source.stop()
                    #print(rankings)

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

def parse_args():
    """ Parses command line arguments.

    Returns
    -------
    args : obj
        An ``argparse`` object containing all of the added arguments.
    """

    # Create help strings
    name_help = 'Your name (or whichever name you want your player to have).'
    distance_help = 'The length you want your player to run for (meters).'
    time_help = 'Your average time for the selected distance (seconds).'
    nplayers_help = 'The amount of runners you want to compete against. Default = 10 runners.'
    interval_help = 'The time (in milliseconds) in between frames. Default = 1 millisecond.'


    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
        dest='name',
        action='store',
        type=str,
        required=True,
        help=name_help)
    parser.add_argument('-d',
        dest='distance',
        action='store',
        type=int,
        required=True,
        help=distance_help)
    parser.add_argument('-t',
        dest='time',
        type=int,
        action='store',
        required=True,
        help=time_help)
    parser.add_argument('-p',
        dest='nplayers',
        action='store',
        type=int,
        required=False,
        default=10,
        help=nplayers_help)
    parser.add_argument('-i --interval',
        dest='interval',
        action='store',
        type=int,
        required=False,
        help=interval_help,
        default=1)

    # Set defaults
    parser.set_defaults(nplayers=10, interval=1)

    # Parse args
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()

    trackSim(args.name, args.distance, args.time, args.nplayers, args.interval)
