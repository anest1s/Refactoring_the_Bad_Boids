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

        self.positions = self.initial.initial_position()
        self.velocities = self.initial.initial_velocity()

    def sum_squared_dif(self):

        # This function calculates the squared difference distance between birds
        # Returns the squared dif distance
        separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        self.separations_if_close = np.copy(separations)
        ssd = np.sum(squared_displacements, 0)
        return ssd

    def align(self):

        # Fly towards the middle line
        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle*self.alignment_const

    def separate(self):

        # Fly away from nearby boids

        far_away = self.sum_squared_dif() > self.separation_limit
        self.separations_if_close[0, :, :][far_away] = 0
        self.separations_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(self.separations_if_close, 1)

    def cohere(self):

        # Try to match speed with nearby birds

        velocities_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        velocities_differences_if_close = np.copy(velocities_differences)
        velocities_differences_if_close[0, :, :][self.sum_squared_dif() > self.cohesion_limit] = 0
        velocities_differences_if_close[1, :, :][self.sum_squared_dif() > self.cohesion_limit] = 0
        self.velocities -= np.mean(velocities_differences_if_close, 1)*self.cohesion_const

    def positions_velocities(self):

        # Move according to velocities

        self.positions += self.velocities

    def update(self):

        # Update Boids method

        self.align()
        self.separate()
        self.cohere()
        self.positions_velocities()


z = Boids()

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(z.positions[0], z.positions[1])


def animate(frame):
    z.update()
    scatter.set_offsets(z.positions.transpose())

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
