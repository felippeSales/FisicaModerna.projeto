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
	pode_passar = False
	esta_atraz = False
	
	def __init__(self):
		
		self.surface = pygame.image.load("Imagens/portaAutomatica/square.png").convert()
		self.rect = pygame.image.load("Imagens/portaAutomatica/square.png").get_rect()
		self.surface.set_colorkey((0,255,0))
		
		#posicao do puto
		self.rect.x = 170
		self.rect.y = 500
	
	def verifica_pode_subir(self):
		if self.pode_passar:
			if self.rect.y - self.move_speed >= 350:
				return True
		
		return False

	def verifia_esta_atras(self):
		if self.rect.y == 360:
			self.esta_atraz = True
	
		else:
			self.esta_atraz = False
			
	def reset(self):
		self.rect.x = 170
		self.rect.y = 500
		self.set_surface("Imagens/portaAutomatica/square.png")
	
	def key_pressed(self, key):
		
		if key == K_DOWN:
			if (self.rect.y + self.move_speed <= 500) and self.rect.y != 360:
				self.rect.y += self.move_speed
								
		if key == K_UP:
			if (self.rect.y - self.move_speed) >= 400:
				self.rect.y -= self.move_speed
			elif self.verifica_pode_subir():
				self.rect.y -= self.move_speed
			
			self.set_surface("Imagens/portaAutomatica/square.png")
		
		if key == K_LEFT:
			if (self.rect.x - self.move_speed) >= 0:
				self.rect.x -= self.move_speed
				self.set_surface("Imagens/portaAutomatica/square_left.png")
				
		if key == K_RIGHT:
			if (self.rect.x + self.move_speed) <= 600:
				self.rect.x += self.move_speed
				self.set_surface("Imagens/portaAutomatica/square_right.png")
		if key == K_r:
			self.reset()
			
		self.verifia_esta_atras()
		print "Y:" , self.rect.y , " X: " , self.rect.x
		
	# Poe uma imagem no objeto: 
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
		
	def draw(self, surface):
		surface.blit(self.surface, self.rect)
		
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
	
	desenha = True
	
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/ondaVertical.png").convert()
		
		self.surface.set_colorkey((0,0,0))
		
		
		self.rect = self.surface.get_rect()
		
		#posicao do puto
		self.rect.x = 570
		self.rect.y = 150
		

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		self.rect = surface.get_rect()
		
	def draw(self, surface):
		if self.desenha:
			self.rect.y += 2
			
			surface.blit(self.surface, self.rect)
			
			if self.rect.y >= 440:
				 self.rect.y = 150

class RaioInvertido(object):
	
	desenha = False
	
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/ondaVerticalInvertida.png").convert()
		
		self.surface.set_colorkey((0,0,0))
		
		self.rect = self.surface.get_rect()
		
		#posicao do puto
		self.rect.x = 570
		self.rect.y = 150
		

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		self.rect = surface.get_rect()
		
	def draw(self, surface):
		print "oi"
		if self.desenha:
			self.rect.y -= 2
			
			surface.blit(self.surface, self.rect)
			print "oi"
			if self.rect.y <= 130:
				self.desenha = False
	
class Luz(object):
	def __init__(self):
		self.surface = pygame.image.load("Imagens/portaAutomatica/areaLuz.png").convert()
		self.rect = self.surface.get_rect()
		
		self.surface.set_colorkey((0,0,0))
		
		#posicao do puto
		self.rect.x = 515
		self.rect.y = 430

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		self.rect = surface.get_rect()
		self.rect.x = 515
		self.rect.y = 450
		
	def draw(self, surface):
		surface.blit(self.surface, self.rect)
			
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
		if self.x >= 408:
			self.x -= 1
			
	def fecha_porta(self):
		if self.x <= 515:
			self.x += 1
	
	def draw(self, surface):
		if self.has_to_open:
			self.abre_porta()
		else:
			self.fecha_porta()
			
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
		if self.x <= 730:
			self.x += 1
			
	def fecha_porta(self):
		if self.x >= 623:
			self.x -= 1

	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
		
	def draw(self, surface):
		if self.has_to_open:
			self.abre_porta()
		else:
			self.fecha_porta()
		
		surface.blit(self.surface, (self.x, self.y))
		
def colisao_luz_personagem():
	if personagem.rect.colliderect(luz.rect) == True:
		portaDireita.has_to_open = True
		portaEsquerda.has_to_open = True
		personagem.pode_passar = True
	else:
		portaDireita.has_to_open = False
		portaEsquerda.has_to_open = False
		personagem.pode_passar = False

def escolhe_Animacao():
	if raio.desenha:
		raio.desenha = False
	else:
		raio.desenha = True
	
def atualiza_tela():				
	
	if personagem.esta_atraz == False:	
		luz.draw(screen)
		ceu.draw(screen)
		solo.draw(screen)
		parede.draw(screen)
		sensor.draw(screen)
	
		portaEsquerda.draw(screen)
		portaDireita.draw(screen)
	
		personagem.draw(screen)
			
		if not raioInvertido.desenha and not raio.desenha:
			raioInvertido.rect.y = personagem.rect.y
			raioInvertido.rect.x = personagem.rect.x
			raioInvertido.desenha = True
			
		raioInvertido.draw(screen)
		raio.draw(screen)
		
	else:
		ceu.draw(screen)
		luz.draw(screen)
		solo.draw(screen)
		personagem.draw(screen)
		parede.draw(screen)
		sensor.draw(screen)

		portaEsquerda.draw(screen)
		portaDireita.draw(screen)
		
		
		raioInvertido.draw(screen)
		raio.draw(screen)
		
	pygame.display.flip()


ceu = Ceu()
solo = Solo()
parede = Parede()
sensor = Sensor()
personagem = Personagem()
raio = Raio()
raioInvertido = RaioInvertido()

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
			if event.key == K_m:
				escolhe_Animacao()
			else:
				personagem.key_pressed(event.key)
	
	colisao_luz_personagem()
	
	atualiza_tela()

run()
