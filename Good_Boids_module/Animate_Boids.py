#  ==============================================================================================================
#  @brief: This script animates the boids flocking
#  @details: This work has been done for the MPHYG001 module of my MRes studies
#  @author: Anestis Mamplekos-Alexiou (anestis.mamplekos-alexiou.16@ucl.ac.uk)
#  @date: 24/2/2017

from matplotlib import animation
from matplotlib import pyplot as plt
from Good_Boids_module.Update_Boids import Boids


class Animator(Boids):
    def __init__(self, configuration_file):
        super(Animator, self).__init__(configuration_file)

    def animate(self, scatter):
        self.update()
        scatter.set_offsets(self.positions.transpose())

    def figure(self):

        figure = plt.figure()
        axes = plt.axes(xlim=self.config['x_coordinates'], ylim=self.config['y_coordinates'])
        plt.xlabel('x position')
        plt.ylabel('y position')
        plt.title('The Boids!')

        positions = self.positions
        scatter = axes.scatter(positions[0, :], positions[1, :])

        animate = lambda x: self.animate(scatter)
        anim = animation.FuncAnimation(figure, animate, frames=self.config['frames'], interval=self.config['interval'])
        plt.show()
