# coding: utf- 08

import pygame
import random
import time
import sys

from pygame.locals import *

class Interface_do_Experimento:
	
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800,600),0,32)
		pygame.display.set_caption("Efeito Foto Elétrico")

	def set_background(self, imagem):
		self.background = pygame.image.load(imagem)
		
	def atualiza_tela(self):
		# Atualiza a tela:
		
		self.background = pygame.image.load("background.png")
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()
	
	def run(self):     
		
		while True:
			for event in pygame.event.get():
				# Fecha o jogo
				if event.type == QUIT:
					sys.exit()
				if event.type == KEYDOWN:
					self.key_pressed(event.key)
			
			self.atualiza_tela()
			
experimento = Interface_do_Experimento()
experimento.run()
