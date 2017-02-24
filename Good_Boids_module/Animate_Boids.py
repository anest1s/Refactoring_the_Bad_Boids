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
        positions = self.positions
        scatter = axes.scatter(positions[0, :], positions[1, :])

        # Function handle for animate
        animate = lambda x: self.animate(scatter)
        anim = animation.FuncAnimation(figure, animate, frames=self.config['frames'], interval=self.config['interval'])
        plt.show()