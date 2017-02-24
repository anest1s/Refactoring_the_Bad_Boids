The Boids  
=========  
This project simulates the bird-oids (Boids) Flocking.
The updated code is the outcome of refactoring the bad boids implementation.

**Start with Installation!!!:**
```
cmd: Refactoring_the_Bad_Boids> python setup.py install

sudo pip install git+https://github.com/anest1s/Refactoring_the_Bad_Boids

```

**Usage:**
```
usage: command_line.py [-h] [--file CONFIGURATION_FILE]

Simulation of boids' flocking

optional arguments:
    -h, --help            show this help message and exit
    --file CONFIGURATION_FILE
                          Choose your configuration file
```

**Command line entry:**
```
cmd: Refactoring_the_Bad_Boids\Good_Boids_module python command_line.py --file 'YOUR_CONFIGURATION_FILE'.py
```

**Configuration file:**
```
In order to simulate the Boids you need a configuration file as an input. This file has to have the format provided below.
For different simulation parameters you might change the values but not the general structure of the file.

Example of configuration file

config.yaml
# Code constants configuration file

birds_number: 50

# motion constants
alignment_const: 0.01
separation_limit: 100
cohesion_limit: 10000
cohesion_const: 0.125

# initial conditions
# x, y axes of motion respectively
position_lower_limits: [-450.0, 300.0]
position_upper_limits: [50.0, 600.0]
velocity_lower_limits: [0.0, -20.0]
velocity_upper_limits: [10.0, 20.0]

# plot settings
x_coordinates: [-500, 1500]
y_coordinates: [-500, 1500]

# animation settings
frames: 50
interval: 50

```

For more information, contact me (Anestis Mamplekos-Alexiou) at: mamplekos@gmail.com