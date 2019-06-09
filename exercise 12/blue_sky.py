import sys
import pygame

from settings import Settings
from character import Character
import game_functions as gf

def run_game():
	"""Initializes the game and screen objects."""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Blue Sky")
	
	# Make a character.
	character = Character(screen)
	
	# Start the main loop of the game.
	while True:
		
		gf.check_events()
		gf.update_screen(ai_settings, screen, character)
		
run_game()
		
