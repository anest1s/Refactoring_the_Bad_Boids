from Generate_Boids import Initialize
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Boids(Initialize):
    def __init__(self):
        Initialize.__init__(self)
        super(Boids, self).__init__()

    def align(self):

        # Fly towards the middle line

        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle*self.alignment_const

    def square_distances(self):

        # This function calculates the squared difference distance between birds
        # Returns the squared dif distance

        separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        self.separations_if_close = np.copy(separations)
        square_dist = np.sum(squared_displacements, 0)
        return square_dist

    def separate(self):

        # Fly away from nearby boids

        far_away = self.square_distances() > self.separation_limit
        self.separations_if_close[0, :, :][far_away] = 0
        self.separations_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(self.separations_if_close, 1)

    def cohere(self):

        # Try to match speed with nearby birds

        velocities_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        velocities_differences_if_close = np.copy(velocities_differences)
        far_away = self.square_distances() > self.cohesion_limit
        velocities_differences_if_close[0, :, :][far_away] = 0
        velocities_differences_if_close[1, :, :][far_away] = 0
        self.velocities -= np.mean(velocities_differences_if_close, 1)*self.cohesion_const

    def positions_velocities(self):

        # Move according to velocities

        self.positions += self.velocities

    def update(self):

        # Update Boids combining all methods

        self.align()
        self.separate()
        self.cohere()
        self.positions_velocities()


z = Boids()
print(z.birds_num)

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(z.positions[0], z.positions[1])


def animate(frame):
    z.update()
    scatter.set_offsets(z.positions.transpose())

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
