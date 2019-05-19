# Track simulator v0.1

This simulator will allow users to input their track and cross-country running statistics, and simulate a
real-time race against other runners. Users can choose to enter tournaments in which they compete against runners in a range of difficulties. 

# Running Track Simulator 

The track simulator can be run on iPython or with the following terminal command: 

`python race_simulation.py -n [name] -d [distance] -t [time] -p [runners] -i [interval]`

Here is a brief breakdown of the parameters:\
  `[name]` - The name of your runner.\
  `[distance]` - The length of the race your player will run (in meters).\
  `[time]` - The average recorded time of your player for the corresponding distance (in seconds).\
  `[runners]` (Optional. Default = 10 runners) - The total number of runners your player will be racing against.\
  `[interval]` (Optional. Default = 1 millisecond) - The time gap between frames (in milliseconds). For real-time race duration,      enter 1000 milliseconds. 
