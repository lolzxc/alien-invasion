import pygame

class Character():
	
	def __init__(self, screen):
		"""Initializes the character and set its starting point."""
		self.screen = screen
		
		# Load the character image and get its rect(rectangle).
		self.image = pygame.image.load('images/character.png')
		self.image = pygame.transform.scale(self.image, (140, 80))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start new character at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		"""Draw the character at its location."""
		self.screen.blit(self.image, self.rect)
		
