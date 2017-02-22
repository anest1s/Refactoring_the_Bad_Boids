import yaml
import numpy as np


class Initialize(object):
    def __init__(self):
        self.config = yaml.load(open('config.yaml'))

        self.birds_num = (self.config['birds_number'])

    def initial_conditions(self, lower_limits, upper_limits):
        lower_limits, upper_limits = [np.array(lower_limits), np.array(upper_limits)]
        width = upper_limits - lower_limits
        condition = lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*width[:, np.newaxis]
        return condition

    def initial_position(self):
        position = self.initial_conditions(self.config['position_lower_limits'], self.config['position_upper_limits'])
        return position

    def initial_velocity(self):
        velocity = self.initial_conditions(self.config['velocity_lower_limits'], self.config['velocity_upper_limits'])
        return velocity

'''
z = Initialize()
a = z.initial_position()
print(a)
'''