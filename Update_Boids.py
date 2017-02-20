from Generate_Boids import Initialize
import itertools


class Boids(object):
    def __init__(self):

        self.initial = Initialize()  # Create object from Initialize class
        self.configuration = self.initial.configuration  # Get configuration data

        # Get configuration constants
        self.birds_num = self.initial.birds_num
        self.alignment_const = (self.configuration['alignment_const'])
        self.separation_limit = (self.configuration['separation_limit'])

        # Get initial cartesian positions and velocities
        self.x = self.initial.initial_position()[0]
        self.x_vel = self.initial.initial_velocity()[0]
        self.y = self.initial.initial_position()[1]
        self.y_vel = self.initial.initial_velocity()[1]

        print(self.x_vel)

    def align(self):

        # This function ascertains that the birds fly towards the middle line

        for [bird_i, bird_j] in itertools.product(range(self.birds_num), repeat=2):
            self.x_vel[bird_i] = self.x_vel[bird_i] + (self.x[bird_j]-self.x[bird_i])*self.alignment_const/self.birds_num
            self.y_vel[bird_i] = self.y_vel[bird_i] + (self.y[bird_j]-self.y[bird_i])*self.alignment_const/self.birds_num

        print(self.x_vel)







z = Boids()
z.align()



