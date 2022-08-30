import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import Game_Stats
from button import Button
from score_board import Scoreboard

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = Game_Stats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    aliens = Group()

    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
