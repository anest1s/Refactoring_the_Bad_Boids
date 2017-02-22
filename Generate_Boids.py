import yaml
import numpy as np


class Initialize(object):

    def __init__(self):
        self.configuration = yaml.load(open('config.yaml'))
        self.birds_num = (self.configuration['birds_number'])

        self.position_lower_limits = np.array(self.configuration['position_lower_limits'])
        self.position_upper_limits = np.array(self.configuration['position_upper_limits'])

        self.velocity_lower_limits = np.array(self.configuration['velocity_lower_limits'])
        self.velocity_upper_limits = np.array(self.configuration['velocity_upper_limits'])

    def initial_position(self):
        self.width = self.position_upper_limits - self.position_lower_limits
        self.position = self.position_lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*self.width[:, np.newaxis]
        return self.position

    def initial_velocity(self):
        self.width = self.velocity_upper_limits - self.velocity_lower_limits
        self.velocity = self.velocity_lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*self.width[:, np.newaxis]
        return self.velocity


z = Initialize()
a = z.initial_position()
print(a)