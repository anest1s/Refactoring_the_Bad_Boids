from matplotlib import animation
from matplotlib import pyplot as plt
from Update_Boids import Boids


class Animator(object):
    def __init__(self):
        self.boids = Boids()

    def animate(self, scatter):
        self.boids.update()
        scatter.set_offsets(self.boids.positions.transpose())

    def figure(self):

        figure = plt.figure()
        axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
        positions = self.boids.positions
        scatter = axes.scatter(positions[0, :], positions[1, :])

        # Function handle for animate
        animate = lambda x: self.animate(scatter)
        anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)
        plt.show()

z = Animator()
z.figure()
