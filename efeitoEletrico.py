# coding: utf- 8

import pygame
import random
import time
import sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Efeito Foto Eletrico")



class Eletron():
	movespeed = 1
	def __init__(self):
		self.surface = pygame.image.load("Imagens/eletron.png")
		self.surface.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 227
		self.y = 470
	
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def move(self):
		if(self.x == 227 and self.y >= 470 and self.y < 540):
			self.y += self.movespeed
		elif(self.y ==540 and self.x >= 227 and self.x < 532):
			self.x += self.movespeed
		elif(self.x ==532 and self.y <= 540 and self.y > 100):
			self.y -= self.movespeed
		elif(self.y == 100 and self.x <= 532 and self.x > 227):
			self.x -= self.movespeed
		elif(self.x == 227 and self.y >= 100 and self.y < 222):
			self.y += self.movespeed
		else:
			self.x = 227
			self.y = 470
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.move()

class Raio():
	def __init__(self):
		self.surface = pygame.image.load("Imagens/radiacao.png").convert()
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
		if pos > 0 and pos < 5:
			self.surface = pygame.image.load("Imagens/sol.png").convert()
			self.surface.set_colorkey((0,0,0))
		elif pos >= 5:
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
		for i in range(0,pos):
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
				
				
	def getPos(self):
		return self.pos	
			
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.sol.draw(screen, self.pos)
		if self.pos > 0:
			screen.blit(self.lampada_on[0],self.lampada_on[1])
			for i in range(0, self.pos*3):
				eletrons[i].draw(screen)

		else:
			screen.blit(self.lampada[0],self.lampada[1])
			
			

class IndicadorH():
	move_speed = 25
	
	
	def __init__(self):
		self.sol = Sol()
		self.pos=4
		self.surface = pygame.image.load("Imagens/indicadorh.png").convert()
		self.surface.set_colorkey((0,0,0))

		#posicao do puto
		self.x = 687
		self.y = 230
		
	def key_pressed(self, key):
		if key == K_UP:
			if self.pos > 0:
				self.pos -= 1
				self.y -= self.move_speed
				self.sol.atualizaSol(self.pos)
		if key == K_DOWN:
			if self.pos < 8:
				self.pos += 1
				self.y += self.move_speed
				self.sol.atualizaSol(self.pos)
				
				
		
			
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.sol.draw(screen, self.pos)




class EfeitoVoltaico():
	circuito = (pygame.image.load("Imagens/PlacasDeNP.png"),(100,100))
	back  = (pygame.image.load("Imagens/background.png"),(0,0))
	surface = pygame.image.load("Imagens/radiacao.png").convert()
	surface.set_colorkey((0,0,0))
	raio = (surface,(10,10))
	intensidade_bar = (pygame.image.load("Imagens/barra_intensidade.png"),(500,0))
	frequencia_bar = (pygame.image.load("Imagens/frequencia.png"),(550,80))
	raio_pos = (50,50)
	cursor_pos =(527, 37)
	intensidade_bar[0].set_colorkey((255,255,255))
	frequencia_bar[0].set_colorkey((255,255,255))
	circuito[0].set_colorkey((255,255,255))
	
	
	
	def set_background(self, imagem):
		self.background = pygame.image.load(imagem)
		
	def atualiza_tela(self):
		# Atualiza a tela:
		
		screen.blit(self.back[0],self.back[1])
		screen.blit(self.intensidade_bar[0], self.intensidade_bar[1])
		screen.blit(self.frequencia_bar[0], self.frequencia_bar[1])
		screen.blit(self.circuito[0],self.circuito[1])
		
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
eletrons = []
for i in range(0, 100):
	eletrons.append(Eletron())
for i in range(0,8):
	raios.append(Raio())
indicador = Indicador()			
indicadorh = IndicadorH()
exp = EfeitoVoltaico()
exp.run()	
	
