from Generate_Boids import Initialize
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Boids(object):
    def __init__(self):

        self.initial = Initialize()  # Create object from Initialize class
        self.configuration = self.initial.configuration  # Get configuration data

        # Get configuration constants
        self.birds_num = self.initial.birds_num
        self.alignment_const = (self.configuration['alignment_const'])
        self.separation_limit = (self.configuration['separation_limit'])
        self.cohesion_limit = (self.configuration['cohesion_limit'])
        self.cohesion_const = (self.configuration['cohesion_const'])

        # Get initial cartesian positions and velocities

        self.x = self.initial.initial_position()[0]
        self.x_vel = self.initial.initial_velocity()[0]
        self.y = self.initial.initial_position()[1]
        self.y_vel = self.initial.initial_velocity()[1]

        self.positions = self.initial.initial_position()
        self.velocities = self.initial.initial_velocity()

    def squared_dif(self, bird_i, bird_j):

        # This function calculates the squared difference distance between birds
        # Returns the squared dif distance

        self.distance = (self.x[bird_i]-self.x[bird_j])**2 + (self.y[bird_i]-self.y[bird_j])**2
        return self.distance

    def align(self):

        # Fly towards the middle line
        self.middle = np.mean(self.positions, 1)
        self.direction_to_middle = self.positions - self.middle[:, np.newaxis]
        self.velocities = self.velocities - self.direction_to_middle*self.alignment_const

    '''
    def separate(self):

        # Fly away from nearby boids

        for [bird_i, bird_j] in itertools.product(range(self.birds_num), repeat=2):
            if self.squared_dif(bird_i, bird_j) < self.separation_limit:
                self.x_vel[bird_i] += (self.x[bird_i] - self.x[bird_j])
                self.y_vel[bird_i] += (self.y[bird_i] - self.y[bird_j])

    def cohere(self):

        # Try to match speed with nearby birds
        for [bird_i, bird_j] in itertools.product(range(self.birds_num), repeat=2):
            if self.squared_dif(bird_i, bird_j) < self.cohesion_limit:
                self.x_vel[bird_i] += (self.x_vel[bird_j]-self.x_vel[bird_i])*self.cohesion_const/self.birds_num
                self.y_vel[bird_i] += (self.y_vel[bird_j]-self.y_vel[bird_i])*self.cohesion_const/self.birds_num
    '''

    def positions_velocities(self):

        # Move according to velocities

        self.positions += self.velocities

    def update(self):

        # Update Boids method

        self.align()
        '''
        self.separate()
        self.cohere()
        '''
        self.positions_velocities()

z = Boids()

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(z.x, z.y)


def animate(frame):
    z.update()
    scatter.set_offsets(z.positions.transpose())

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
