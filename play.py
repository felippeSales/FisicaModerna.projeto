# coding: utf- 08

import pygame
import random
import time
import sys
import os

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Efeito Foto Elétrico")

class Personagem(object):
	
	move_speed = 20
	
	def __init__(self):
		#self.image = pygame.image.load("Imagens/square.png")
		self.surface = pygame.image.load("Imagens/square.png").convert()
		self.surface.set_colorkey((0,255,0))
		
		#posicao do puto
		self.x = 0
		self.y = 500
	
	def key_pressed(self, key):
		
		if key == K_DOWN:
			if (self.y + self.move_speed) <= 500:
				self.y += self.move_speed
								
		if key == K_UP:
			if (self.y - self.move_speed) >= 400:
				self.y -= self.move_speed
		
		if key == K_LEFT:
			if (self.x - self.move_speed) >= 0:
				self.x -= self.move_speed
				
		if key == K_RIGHT:
			if (self.x + self.move_speed) <= 600:
				self.x += self.move_speed

		
	# Poe uma imagem no objeto: 
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))

class Ceu(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/ceu.png").convert()
		self.surface.set_colorkey((255,255,255))
		
		#posicao do puto
		self.x = 0
		self.y = 0

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((255,255,255))
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))

class Solo(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/chao.png").convert()
		self.surface.set_colorkey((255,255,255))		
		
		#posicao do puto
		self.x = 0
		self.y = 400

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((255,255,255))
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))

class Parede(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/wall.png").convert()
		self.surface.set_colorkey((255,255,255))
		
		#posicao do puto
		self.x = 0
		self.y = 20

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((255,255,255))
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))

class Sensor(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/sensor.png").convert()
		self.surface.set_colorkey((255,255,255))
		
		#posicao do puto
		self.x = 570
		self.y = 150

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((255,255,255))
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
			
def atualiza_tela():
		
	ceu.draw(screen)
	solo.draw(screen)
	parede.draw(screen)
	sensor.draw(screen)
	personagem.draw(screen)
	pygame.display.flip()
	

ceu = Ceu()
solo = Solo()
parede = Parede()
sensor = Sensor()
personagem = Personagem()

clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		# Fecha o jogo
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			personagem.key_pressed(event.key)
	
	atualiza_tela()

run()
