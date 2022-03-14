import pygame
import numpy
import math

#settings
res = width, height = 800, 450
offset = numpy.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

#texture
texture = pygame.image.load('Textures/texture.jpg')
texture_size = min(texture.get_size()) - 1
texture_array = pygame.surfarray.array3d(texture)


class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = numpy.full(
            (width, height, 3), [0, 0, 0], dtype=numpy.uint8)

    def render(self):
        for x in range(width):
            for y in range(height):
                c = (x - offset[0]) * zoom + 1j * (y - offset[1]) * zoom
                z = 0
                num_iter = 0
                for _ in range(max_iter):
                    z = z ** 2 + c
                    if abs(z) > 2:
                        break
                    num_iter += 1
                col = int(texture_size * num_iter / max_iter)
                self.screen_array[x, y] = texture_array[col, col]

    def update(self):
        self.render()

    def draw(self):
        pygame.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(res, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pygame.display.flip()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            self.clock.tick()
            pygame.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')


if __name__ == '__main__':
    app = App()
    app.run()
