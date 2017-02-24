#  ==============================================================================================================
#  @brief: This script generates the initial conditions (positions/velocities) of a flock
#  @details: This work has been done for the MPHYG001 module of my MRes studies
#  @author: Anestis Mamplekos-Alexiou (anestis.mamplekos-alexiou.16@ucl.ac.uk)
#  @date: 24/2/2017

import yaml
import numpy as np


class Initializer(object):
    def __init__(self, configuration_file):

        '''
        :param configuration_file: includes all necessary constants for the simulation
        :return: initial positions and velocities for each bird of the flock
        '''

        self.config = yaml.load(open(configuration_file))

        self.birds_num = (self.config['birds_number'])
        self.alignment_const = (self.config['alignment_const'])
        self.separation_limit = (self.config['separation_limit'])
        self.cohesion_limit = (self.config['cohesion_limit'])
        self.cohesion_const = (self.config['cohesion_const'])

        self.positions = self.initial_conditions(self.config['position_lower_limits'],
                                                 self.config['position_upper_limits'])

        self.velocities = self.initial_conditions(self.config['velocity_lower_limits'],
                                                  self.config['velocity_upper_limits'])

    def initial_conditions(self, lower_limits, upper_limits):

        '''
        :param lower_limits: position or velocity lower limits
        :param upper_limits: position or velocity upper limits
        This function calculates the condition (position or velocity) of the birds based on the input data (config_file)
        '''

        lower_limits, upper_limits = [np.array(lower_limits), np.array(upper_limits)]
        width = upper_limits - lower_limits
        condition = lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*width[:, np.newaxis]
        return condition
