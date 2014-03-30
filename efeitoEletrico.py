# coding: utf- 8

import pygame
import random
import time
import sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Efeito Foto Eletrico")

class EfeitoVoltaico():
	circuito = (pygame.image.load("Imagens/PlacasDeNP.png"),(100,100))
	eletron  = (pygame.image.load("Imagens/eletron.png"),(600,0))
	lampada = 	(pygame.image.load("Imagens/lampadaDesligada.png"),(552,300))
	back  = (pygame.image.load("Imagens/background.png"),(0,0))
	
	surface = pygame.image.load("Imagens/radiacao.png").convert()
	surface.set_colorkey((0,0,0))
	raio = (surface,(10,10))
	sol = (pygame.image.load("Imagens/InkSun.png"),(0,0))
	ceu = (pygame.image.load("Imagens/radiacao.png"),(50,50))
	raio_pos = (50,50)
	
	circuito[0].set_colorkey((255,255,255))
	eletron[0].set_colorkey((255,255,255))
	lampada[0].set_colorkey((255,255,255))
	
	sol[0].set_colorkey((255,255,255))
	
	def set_background(self, imagem):
		self.background = pygame.image.load(imagem)
		
	
	def atualiza_tela(self):
		# Atualiza a tela:
		screen.blit(self.back[0],self.back[1])
		screen.blit(self.circuito[0],self.circuito[1])
		screen.blit(self.eletron[0],self.eletron[1])
		screen.blit(self.lampada[0],self.lampada[1])
		screen.blit(self.sol[0],self.sol[1])
		screen.blit(self.raio[0], self.raio_pos)
		
		self.raio_pos = (self.raio_pos[0] + 1, self.raio_pos[1] + 1)
		
		if(self.raio_pos[1] == 170):
			self.raio_pos = (50,50)
			
		pygame.display.flip()
		
	def run(self):     
		
		while True:
			for event in pygame.event.get():
				# Fecha o jogo
				if event.type == QUIT:
					sys.exit()
				
			self.atualiza_tela()
		
exp = EfeitoVoltaico()
exp.run()	
	