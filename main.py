import pygame
import os
import sys

vec = pygame.math.Vector2

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect(x, y, 20, 20)
        self.vy = 4

    def update(self, *args):
        self.rect = self.rect.move(0, self.vy)
        if pygame.sprite.spritecollideany(self, platforms):
            self.vy = 0
            self.rect.bottom = pygame.sprite.spritecollideany(self, platforms).rect.top
        else:
            self.vy = 4
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.left -= 3
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.left += 3
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.vy = -4

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__(all_sprites)
        self.add(platforms)
        self.image = pygame.Surface([w, h])
        self.image.fill((125, 125, 125))
        self.rect = pygame.Rect(x, y, w, h)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    running = True
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    fps = 60
    clock = pygame.time.Clock()
    Hero(0, height - 30)
    Platform(0, height - 10, width, 20)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
