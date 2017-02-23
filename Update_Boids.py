from Generate_Boids import Initializer
import numpy as np


class Boids(Initializer):
    def __init__(self, configuration_file):
        super(Boids, self).__init__(configuration_file)

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