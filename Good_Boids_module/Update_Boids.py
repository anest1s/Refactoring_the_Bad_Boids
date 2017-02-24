#  ==============================================================================================================
#  @brief: This script updates the position of each bird of the flock based on a distributed behavioral model
#  @details: This work has been done for the MPHYG001 module of my MRes studies
#  @author: Anestis Mamplekos-Alexiou (anestis.mamplekos-alexiou.16@ucl.ac.uk)
#  @date: 24/2/2017

from Good_Boids_module.Generate_Boids import Initializer
import numpy as np


class Boids(Initializer):
    def __init__(self, configuration_file):

        '''
        This class contains three steering behaviors which describe
        how an individual boid maneuvers based on the positions and velocities its nearby flockmates
        '''

        super(Boids, self).__init__(configuration_file)

    def align(self):

        '''
        Alignment behavior: Steer towards the average heading of local flockmates
        :return: velocities
        '''

        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:, np.newaxis]
        self.velocities -= direction_to_middle*self.alignment_const

    def square_distances(self):

        '''
        This function calculates the squared difference distance between birds
        :return: Returns the squared dif distance
        '''

        separations = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        self.separations_if_close = np.copy(separations)
        square_dist = np.sum(squared_displacements, 0)
        return square_dist

    def separate(self):

        '''
        Separation behavior: steer to avoid crowding local flockmates
        :return: velocities
        '''

        far_away = self.square_distances() > self.separation_limit
        self.separations_if_close[0, :, :][far_away] = 0
        self.separations_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(self.separations_if_close, 1)

    def cohere(self):

        '''
        Cohesion behavior: steer to move toward the average position of local flockmates
        :return: velocities
        '''

        velocities_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        velocities_differences_if_close = np.copy(velocities_differences)
        far_away = self.square_distances() > self.cohesion_limit
        velocities_differences_if_close[0, :, :][far_away] = 0
        velocities_differences_if_close[1, :, :][far_away] = 0
        self.velocities -= np.mean(velocities_differences_if_close, 1)*self.cohesion_const

    def positions_velocities(self):

        '''
        This method calculates the position according to velocity
        :return: positions
        '''

        self.positions += self.velocities

    def update(self):

        '''
        Updates the boids according to all previous behaviors (methods)
        :return: final positions
        '''

        self.align()
        self.separate()
        self.cohere()
        self.positions_velocities()
