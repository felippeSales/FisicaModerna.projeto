# coding: utf- 08

import pygame
import random
import time
import sys

from pygame.locals import *

class Interface_do_Experimento:
	
	ceu = (pygame.image.load("Imagens/portaAutomatica/ceu.png"),(0,0))
	solo = (pygame.image.load("Imagens/portaAutomatica/chao.png"),(0,400))
	
	parede = (pygame.image.load("Imagens/portaAutomatica/wall.png"),(0,400))
	
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800,600),0,32)
		pygame.display.set_caption("Efeito Foto Elétrico")

	def set_background(self, imagem):
		self.background = pygame.image.load(imagem)
		
	def atualiza_tela(self):
		# Atualiza a tela:
		
		self.screen.blit(self.ceu[0],self.ceu[1])
		self.screen.blit(self.solo[0],self.solo[1])
		self.screen.blit(self.parede[0],self.parede[1])
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
