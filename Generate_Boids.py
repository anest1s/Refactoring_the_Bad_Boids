import yaml
import numpy as np


class Initialize(object):
    def __init__(self):
        self.configuration = yaml.load(open('config.yaml'))

        self.birds_num = (self.configuration['birds_number'])
        
    def calc_initial_conditions(self, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        condition = lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*width[:, np.newaxis]
        return condition

    def initial_position(self):
        position_lower_limits = np.array(self.configuration['position_lower_limits'])
        position_upper_limits = np.array(self.configuration['position_upper_limits'])
        position = self.calc_initial_conditions(position_lower_limits, position_upper_limits)
        return position

    def initial_velocity(self):
        velocity_lower_limits = np.array(self.configuration['velocity_lower_limits'])
        velocity_upper_limits = np.array(self.configuration['velocity_upper_limits'])
        velocity = self.calc_initial_conditions(velocity_lower_limits, velocity_upper_limits)
        return velocity

'''
z = Initialize()
a = z.initial_position()
print(a)
'''