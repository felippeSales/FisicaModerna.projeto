# coding: utf- 8

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
		
		self.surface = pygame.image.load("Imagens/square.png").convert()
		self.rect = pygame.image.load("Imagens/square.png").get_rect()
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

		self.rect.x = self.x
		self.rect.y = self.y

		print "Y:" , self.y , " X: " , self.x
		
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
			
class Raio(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/raioVertical.png").convert()
		
		self.surface.set_colorkey((0,0,0))
		
		#posicao do puto
		self.x = 570
		self.y = 150
		
		self.rect = self.surface.get_rect()

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		self.rect = surface.get_rect()
		
	def draw(self, surface):
		self.y += 1
		surface.blit(self.surface, (self.x, self.y))
		
		if self.y >= 440:
			 self.y = 150
			 
		self.rect.x = self.x
		self.rect.y = self.y

class Luz(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/areaLuz.png").convert()
		self.rect = self.surface.get_rect()
		
		self.surface.set_colorkey((0,0,0))
		
		#posicao do puto
		self.x = 515
		self.y = 450
		
		self.rect = self.surface.get_rect()

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		self.rect = surface.get_rect()
		
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
			
class Porta_Esquerda(object):
	
	has_to_open = False
	
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/porta.png").convert()
		self.surface.set_colorkey((0,0,0))
		
		#posicao do puto
		self.x = 515
		self.y = 204

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
	
	def abre_porta(self):
		self.x -= 1
		if self.x == 408:
			self.x = 515
	def fecha_porta(self):
		while(self.x != 515):
			self.x += 2
	
	def draw(self, surface):
		if self.has_to_open:
			self.abre_porta()
	
		surface.blit(self.surface, (self.x, self.y))

class Porta_Direita(object):
	
	has_to_open = False
	
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/porta.png").convert()
		self.surface.set_colorkey((0,0,0))
		
		#posicao do puto
		self.x = 623
		self.y = 204

	def abre_porta(self):
		self.x += 1
		if self.x == 730:
			self.x = 623

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		
	def draw(self, surface):
		if self.has_to_open:
			self.abre_porta()
		
		surface.blit(self.surface, (self.x, self.y))



def colisao_luz_personagem():
	
	if personagem.rect.colliderect(luz.rect) == True:
		print "algo"
		portaDireita.has_to_open = True
		portaEsquerda.has_to_open = True
	#else:
#		print pesq.fecha_porta()

def atualiza_tela():				
		
	ceu.draw(screen)
	solo.draw(screen)
	parede.draw(screen)
	sensor.draw(screen)
	luz.draw(screen)
	
	portaEsquerda.draw(screen)
	portaDireita.draw(screen)
	
	personagem.draw(screen)
	
#	raio.draw(screen)
	
		
	pygame.display.flip()



ceu = Ceu()
solo = Solo()
parede = Parede()
sensor = Sensor()
personagem = Personagem()

portaEsquerda = Porta_Esquerda()
portaDireita = Porta_Direita()
luz = Luz()
clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		# Fecha o jogo
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			personagem.key_pressed(event.key)
	
	colisao_luz_personagem()
	
	atualiza_tela()

run()
