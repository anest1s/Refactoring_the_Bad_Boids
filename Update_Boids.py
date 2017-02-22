from Generate_Boids import Initialize
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
        self.separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        self.squared_displacements = self.separations * self.separations
        self.velocities = self.initial.initial_velocity()
        self.a = self.positions.shape
        self.b = self.separations.shape

    def sum_squared_dif(self):

        # This function calculates the squared difference distance between birds
        # Returns the squared dif distance

        ssd = np.sum(self.squared_displacements, 0)

        return ssd

    def align(self):

        # Fly towards the middle line
        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle*self.alignment_const

    def separate(self):

        # Fly away from nearby boids

        separations_if_close = np.copy(self.separations)
        separations_if_close[0, :, :][self.sum_squared_dif() > self.separation_limit] = 0
        separations_if_close[1, :, :][self.sum_squared_dif() > self.separation_limit] = 0
        self.velocities += np.sum(separations_if_close, 1)
        return self.velocities


    '''
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
        self.separate()
        '''
        self.cohere()
        '''
        self.positions_velocities()

z = Boids()
print(z.a)
print(z.b)


figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(z.x, z.y)


def animate(frame):
    z.update()
    scatter.set_offsets(z.positions.transpose())

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
