# coding: utf- 8

import pygame
import random
import time
import sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Efeito Foto Eletrico")

class Raio():
	def __init__(self):
		self.surface = pygame.image.load("Imagens/radiacao2.png").convert()
		self.surface.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 10
		self.y = 10
	
	def mudaCorDoRaio(self, cor):
		if(cor == 1):
			self.surface = pygame.image.load("Imagens/radiacao5.png").convert()
			self.surface.set_colorkey((0,0,0))
			#posicao do puto
			self.x = 10
			self.y = 10
		elif(cor == 2):
			self.surface = pygame.image.load("Imagens/radiacao4.png").convert()
			self.surface.set_colorkey((0,0,0))
			#posicao do puto
			self.x = 10
			self.y = 10
		elif(cor == 3):
			self.surface = pygame.image.load("Imagens/radiacao3.png").convert()
			self.surface.set_colorkey((0,0,0))
			#posicao do puto
			self.x = 10
			self.y = 10
		elif(cor == 4):
			self.surface = pygame.image.load("Imagens/radiacao2.png").convert()
			self.surface.set_colorkey((0,0,0))
			#posicao do puto
			self.x = 10
			self.y = 10
		elif(cor == 5):
			self.surface = pygame.image.load("Imagens/radiacao1.png").convert()
			self.surface.set_colorkey((0,0,0))
			#posicao do puto
			self.x = 10
			self.y = 10
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.x += 1
		self.y += 1
		if(self.x == 170):
			self.x = 50
			self.y = 50
		


class Sol():
	def __init__(self):
		self.surface = pygame.image.load("Imagens/nuvem.png").convert()
		self.surface.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 0
		self.y = 0
		
	def atualizaSol(self ,pos):
		if pos > 0 and pos < 6:
			self.surface = pygame.image.load("Imagens/sol.png").convert()
			self.surface.set_colorkey((0,0,0))
		elif pos >= 6:
			self.surface = pygame.image.load("Imagens/InkSun.png").convert()
			self.surface.set_colorkey((0,0,0))
		else:
			self.surface = pygame.image.load("Imagens/nuvem.png").convert()
			self.surface.set_colorkey((0,0,0))
		
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface, pos):
		surface.blit(self.surface, (self.x, self.y))
		for i in range(0,8):
			raios[i].mudaCorDoRaio(indicadorh.getpos())
			raios[i].draw(screen)

class Indicador():
	move_speed = 25
	
	
	def __init__(self):
		self.sol = Sol()
		self.pos=0
		self.surface = pygame.image.load("Imagens/indicador.png").convert()
		self.surface.set_colorkey((0,0,0))

		self.lampada = 	(pygame.image.load("Imagens/lampadaDesligada.png"),(552,300))
		self.lampada_on = 	(pygame.image.load("Imagens/lampadaLigada.png"),(552,300))
		#posicao do puto
		self.x = 527
		self.y = 37
		
	def key_pressed(self, key):
		if key == K_LEFT:
			if self.pos > 0:
				self.pos -= 1
				self.x -= self.move_speed
				self.sol.atualizaSol(self.pos)
				screen.blit(self.lampada_on[0],self.lampada_on[1])
			
			else:
				screen.blit(self.lampada[0],self.lampada[1])
		if key == K_RIGHT:
			if self.pos < 8:
				self.pos += 1
				self.x += self.move_speed
				self.sol.atualizaSol(self.pos)
			
				
		
			
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.sol.draw(screen, self.pos)
		if self.pos > 0:
			screen.blit(self.lampada_on[0],self.lampada_on[1])
		else:
			screen.blit(self.lampada[0],self.lampada[1])

class IndicadorH():
	move_speed = 25
	
	
	def __init__(self):
		self.sol = Sol()
		self.pos=2
		self.surface = pygame.image.load("Imagens/indicadorh.png").convert()
		self.surface.set_colorkey((0,0,0))

		#posicao do puto
		self.x = 686
		self.y = 195
		
	def key_pressed(self, key):
		if key == K_UP:
			if self.pos > 0:
				self.pos -= 1
				self.y -= self.move_speed
				
		if key == K_DOWN:
			if self.pos < 4:
				self.pos += 1
				self.y += self.move_speed
				
				
				
	def getpos(self):
		return self.pos
			
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		




class EfeitoVoltaico():
	circuito = (pygame.image.load("Imagens/PlacasDeNP.png"),(100,100))
	eletron  = (pygame.image.load("Imagens/eletron.png"),(600,400))
	back  = (pygame.image.load("Imagens/background.png"),(0,0))
	
	surface = pygame.image.load("Imagens/radiacao2.png").convert()
	surface.set_colorkey((0,0,0))
	raio = (surface,(10,10))
	intensidade_bar = (pygame.image.load("Imagens/barra_intensidade.png"),(500,0))
	frequencia_bar = (pygame.image.load("Imagens/frequencia.png"),(630,100))
	raio_pos = (50,50)
	cursor_pos =(527, 37)
	
	intensidade_bar[0].set_colorkey((255,255,255))
	frequencia_bar[0].set_colorkey((255,255,255))
	circuito[0].set_colorkey((255,255,255))
	eletron[0].set_colorkey((255,255,255))
	
	
	def set_background(self, imagem):
		self.background = pygame.image.load(imagem)
		
	def atualiza_tela(self):
		# Atualiza a tela:
		
		screen.blit(self.back[0],self.back[1])
		screen.blit(self.intensidade_bar[0], self.intensidade_bar[1])
		screen.blit(self.frequencia_bar[0], self.frequencia_bar[1])
		screen.blit(self.circuito[0],self.circuito[1])
		screen.blit(self.eletron[0],self.eletron[1])
		
		indicador.draw(screen)
		indicadorh.draw(screen)
		
		pygame.display.flip()
		
	def run(self):     
		
		while True:
			for event in pygame.event.get():
				# Fecha o jogo
				if event.type == QUIT:
					sys.exit()
				if event.type == KEYDOWN:
					indicador.key_pressed(event.key)
					indicadorh.key_pressed(event.key)
				
			self.atualiza_tela()


raios = []
for i in range(0,8):
	raios.append(Raio())
indicador = Indicador()			
indicadorh = IndicadorH()
exp = EfeitoVoltaico()
exp.run()	
