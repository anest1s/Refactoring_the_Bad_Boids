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

    def calc_initial_conditions(self, lower_limits, upper_limits):
        self.width = upper_limits - lower_limits
        self.condition = lower_limits[:, np.newaxis] + np.random.rand(2, self.birds_num)*self.width[:, np.newaxis]
        return self.condition

    def initial_position(self):
        self.position = self.calc_initial_conditions(self.position_lower_limits, self.position_upper_limits)
        return self.position

    def initial_velocity(self):
        self.velocity = self.calc_initial_conditions(self.velocity_lower_limits, self.velocity_upper_limits)
        return self.velocity


z = Initialize()
a = z.initial_position()
print(a)