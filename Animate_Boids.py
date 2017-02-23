from matplotlib import animation
from matplotlib import pyplot as plt
from Generate_Boids import Initializer
from Update_Boids import Boids


class Animator(Initializer):
    def __init__(self):
        super(Animator, self).__init__()

        self.boids = Boids()

    def animate(self, scatter):
        self.boids.update()
        scatter.set_offsets(self.boids.positions.transpose())

    def figure(self):

        figure = plt.figure()
        axes = plt.axes(xlim=self.config['x_coordinates'], ylim=self.config['y_coordinates'])
        positions = self.boids.positions
        scatter = axes.scatter(positions[0, :], positions[1, :])

        # Function handle for animate
        animate = lambda x: self.animate(scatter)
        anim = animation.FuncAnimation(figure, animate, frames=self.config['frames'], interval=self.config['interval'])
        plt.show()


z = Animator()
z.figure()

