import pygame, sys
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, ino, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ino.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    space_ino_x = 700 - 2 * ino_width
    number_ino_x = int(space_ino_x / ino_width)
    space_ino_y = 800 - 200 - 2 * ino_height
    number_ino_y = int(space_ino_y / (ino_height))

    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def update_inos(inos):
    """обновляет позиции пришельцев"""
    inos.update()