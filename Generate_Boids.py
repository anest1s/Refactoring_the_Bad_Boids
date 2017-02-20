import random
import yaml


class Initialize(object):

    def __init__(self):
        self.configuration = yaml.load(open('config.yaml'))
        self.birds_num = (self.configuration['birds_number'])

        self.x_coord_low = (self.configuration['horizontal_position_bounds'][0])
        self.x_coord_high = (self.configuration['horizontal_position_bounds'][1])

        self.y_coord_low = (self.configuration['vertical_position_bounds'][0])
        self.y_coord_high = (self.configuration['vertical_position_bounds'][1])

        self.x_vel_low = (self.configuration['horizontal_velocity_bounds'][0])
        self.x_vel_high = (self.configuration['horizontal_velocity_bounds'][1])

        self.y_vel_low = (self.configuration['vertical_velocity_bounds'][0])
        self.y_vel_high = (self.configuration['vertical_velocity_bounds'][1])

    def initial_position(self):
        self.boids_x_scat = [random.uniform(self.x_coord_low, self.x_coord_high) for bird in range(self.birds_num)]
        self.boids_y_scat = [random.uniform(self.y_coord_low, self.y_coord_high) for bird in range(self.birds_num)]
        return [self.boids_x_scat, self.boids_y_scat]

    def initial_velocity(self):
        self.boids_x_vel_scat = [random.uniform(self.x_vel_low, self.x_vel_high) for bird in range(self.birds_num)]
        self.boids_y_vel_scat = [random.uniform(self.y_vel_low, self.y_vel_high) for bird in range(self.birds_num)]
        return [self.boids_x_vel_scat, self.boids_y_vel_scat]


'''
z = Initialize()
a = z.initial_positions()
b = z.initial_velocity()
print(b[0])

print(b[1])
'''