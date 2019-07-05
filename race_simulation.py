import argparse
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_players():
    """ Creates a dictionary containing racer info based on user input
    that can be passed to trackSim().

    Returns
    -------
    A dictionary containing the inputted racer info.
    """

    number_of_players = int(input('How many players? '))
    names = []
    velocity = []
    for i in np.arange(number_of_players):
        names.append(input('Name of player {}? '.format(i+1)))
        velocity.append(float(input('Speed of player {} (mph)? '.\
        	            format(i+1))) / 2.237)  # convert mph to meters/s
    d = dict({})
    d['name'] = names
    d['velocity'] = velocity
    return d

def simulate(distance):
    """Simulates a race without plotting.

    Parameters
    ----------
    distance : int
        The length you want your player to run for (meters).

    Returns
    -------
    rankings : list
        The results of the race.
    """
    
    # Create racers from user input
    player_info = create_players()
    nplayers = len(player_info['name'])
    
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

        def update(self):
            self.x += self.v
            if self.x >= distance:
                if self.name not in rankings:
                    final_time = np.round((1/self.v)*distance, 2)
                    print(self.name, ' with a final time of '
                                     + str(final_time)
                                     + ' seconds')
                    rankings.append(self.name)

    # create the balls
    balls = []
    for n in np.arange(0, nplayers):
        runner_pos = n+1
        ball = Ball(player_info['name'][n], 0, runner_pos,
                    player_info['velocity'][n])
        balls.append(ball)
    
    # run the race
    rankings = []
    while len(rankings) != nplayers:
        for ball in balls:
            ball.update()
            if len(rankings) == nplayers:
                print(rankings)
                return rankings

def trackSim(distance, interval=1):
    """ Runs the track simulator!

    Parameters
    ----------
    distance : int
        The length you want your player to run for (meters).
    interval : int (default = 1)
        The time (in milliseconds) in between frames. Essentially, this
        parameter adjusts how long you want the race simulation to run.
        The lower this number, the shorter the duration. To run the simulation
        in real-time, the input value should be 1000.
    plot : boob (default = True)
        Set to True to watch the race

    Returns
    -------
    A matplotlib animation with the race simulation.
    """

    # Create racers from user input
    player_info = create_players()

   	# ~~~~~~Bounds of the racetrack~~~~~~
    xlim = (0, distance+(0.5*distance))
    nplayers = len(player_info['name'])
    ylim = (0, nplayers+1.0)

    # ~~~~~~Figure Aesthetics~~~~~~
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

        def update(self):
            self.x += self.v
            self.scatter.set_data(self.x, self.y)
            if self.x >= distance:
                self.scatter.set_data(distance, self.y)
                if self.name not in rankings:
                    final_time = np.round((1/self.v)*distance, 2)
                    print(self.name, ' with a final time of '
                                     + str(final_time)
                                     + ' seconds')
                    rankings.append(self.name)

        def start(self):
            self.scatter.set_data(self.x, self.y)

    def init():
        return []

    def animate(t):
        if t == 0.0:
            print('starting!!')
            for ball in balls:
                ball.start()
        else:
            for ball in balls:
                ball.update()
                if len(rankings) == len(balls):
                    ani.event_source.stop()

        # have to return an iterable
        return [ball.scatter for ball in balls]

    frames = np.arange(0, distance, .001)

    # create the balls
    balls = []
    for n in np.arange(0, nplayers):
        runner_pos = n+1
        ball = Ball(player_info['name'][n], 0, runner_pos,
                    player_info['velocity'][n])
        balls.append(ball)

    # run the simulation
    rankings = []
    ani = animation.FuncAnimation(fig, animate, frames, init_func=init,
                                  interval=interval, blit=True, repeat=False)
    plt.show()
    print(rankings)

    return

def parse_args():
    """ Parses command line arguments.

    Returns
    -------
    args : obj
        An ``argparse`` object containing all of the added arguments.
    """

    # Create help strings
    distance_help = 'The length you want your player to run for (meters).'
    interval_help = ('The time (in milliseconds) in between frames. '
    	             'Default = 1 millisecond.')

    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        dest='distance',
                        action='store',
                        type=int,
                        required=True,
                        help=distance_help)
    parser.add_argument('-i --interval',
                        dest='interval',
                        action='store',
                        type=int,
                        required=False,
                        help=interval_help,
                        default=1)

    # Set defaults
    parser.set_defaults(distance=800, interval=1)

    # Parse args
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()

    trackSim(args.distance, args.interval)
