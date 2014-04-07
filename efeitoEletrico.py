# coding: utf- 8

import pygame
import random
import time
import sys

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Efeito Foto Eletrico")

class FuncoesFisicas():
	
	def __init__(self):
		self.surface = pygame.image.load("ampindi.png").convert()
		self.surface.set_colorkey((0,0,0))
		self.x = 14	
		self.y = 547
		self.lampada = 	(pygame.image.load("lampadaDesligada.png"),(552,300))
		self.lampada_on = 	(pygame.image.load("lampadaLigada.png"),(552,300))
		# frequencia = n x 10 ^ 12
		self.violeta = 789.0
		self.azul = 668.0
		self.verde = 606.0
		self.amarelo = 526.0
		self.vermelho = 484.0
		
		# Um metro
		self.comprimento = 1.0

		self.cargaEletron = 1.6 * (10**(-19))
		self.massaEletron = 9.11 * (10**(-31))
		# -34 + 12 da frequencia
		self.planck = 6.63 * (10 ** (-34 + 12))

		# Potassio
		self.funcaoTrabalhoPotassio = 2.3 * self.cargaEletron
		self.max = self.calcula_corrente(self.violeta, self.funcaoTrabalhoPotassio, 8)
	
	def energia_cinetica(self, frequencia , funcaoTrabalho):
		energia = self.planck*frequencia - funcaoTrabalho
	
		#Se a energia for negativa ele nao arranca eletrons 
		if energia < 0:
			energia = 0
		return energia

	def velocidade(self, frequencia, funcaoTrabalho):
		# 0.5 representa a raiz quadrada
		return (2 * self.energia_cinetica(frequencia, funcaoTrabalho) / self.massaEletron) ** (0.5)

	def tempo(self, frequencia, funcaoTrabalho):
		v = self.velocidade(frequencia, funcaoTrabalho)
		if v == 0:
			return 0.0
		v = self.velocidade(frequencia, funcaoTrabalho)
		return self.comprimento / v
	
	def calcula_corrente(self, frequencia, funcaoTrabalho, numeroEletrons):
		t = self.tempo(frequencia, funcaoTrabalho)
		
		if t == 0:
			return 0.0
		return 	(numeroEletrons * self.cargaEletron) / t 
	def pegacor(self, pos):
		if(pos == 0):
			return self.violeta
		elif(pos == 1):
			return self.azul
		elif(pos == 2):
			return self.verde
		elif(pos == 3):
			return self.amarelo
		elif(pos == 4):
			return self.vermelho
	def draw(self, surface, intensidade, frequencia):
		amp = self.calcula_corrente(self.pegacor(frequencia), self.funcaoTrabalhoPotassio, intensidade)	/ self.max	
		variacao =  int(round(amp * 100))
		
		for i in range(0, variacao+1):
			surface.blit(self.surface, (self.x, self.y - (i*4)))
			if i > 0:
				eletrons[i].draw(screen)
			
		
		if variacao > 0:
			screen.blit(self.lampada_on[0],self.lampada_on[1])
		else:
			screen.blit(self.lampada[0],self.lampada[1])
		
	

	
	


class Eletron():
	movespeed = 1
	def __init__(self):
		self.surface = pygame.image.load("eletron.png").convert()
		self.surface.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 227
		self.y = 470
	def getY(self):
		return self.y
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,0,0))
	def move(self, vel):
		if(self.x == 227 and self.y >= 470 and self.y < 540):
			self.y += self.movespeed*(3-vel)	
		elif(self.y >=540  and self.x >= 227 and self.x < 532):
			self.y = 540
			self.x += self.movespeed*(3-vel)
		elif(self.x >=532 and self.y <= 540 and self.y > 100):
			self.x = 532
			self.y -= self.movespeed*(3-vel)
		elif(self.y <= 100 and self.x <= 532 and self.x > 227):
			self.y = 100
			self.x -= self.movespeed*(3-vel)
		elif(self.x <= 227 and self.y >= 100 and self.y < 222):
			self.x = 227
			self.y += self.movespeed*(3-vel)
		else:
			self.x = 227
			self.y = 470
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.move(indicadorh.getpos())

class Raio():
	movespeed = 1
	def __init__(self):
		self.surface = pygame.image.load("radiacao2.png").convert()
		self.surface.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 50
		self.y = 50
	
	def mudaCorDoRaio(self, cor):
		if(cor == 0):
			self.surface = pygame.image.load("radiacao5.png").convert()
			self.surface.set_colorkey((0,0,0))
			
		elif(cor == 1):
			self.surface = pygame.image.load("radiacao4.png").convert()
			self.surface.set_colorkey((0,0,0))
			
		elif(cor == 2):
			self.surface = pygame.image.load("radiacao3.png").convert()
			self.surface.set_colorkey((0,0,0))
			
		elif(cor == 3):
			self.surface = pygame.image.load("radiacao2.png").convert()
			self.surface.set_colorkey((0,0,0))
			
		elif(cor == 4):
			self.surface = pygame.image.load("radiacao1.png").convert()
			self.surface.set_colorkey((0,0,0))
			
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def move(self, vel):
		if vel > 2:
			vel = 2
		self.x += (self.movespeed*vel)
		self.y += (self.movespeed*vel)
		if(self.x >= 170):
			self.x = 50
			self.y = 50
	def draw(self, surface):
		surface.blit(self.surface, (self.x, self.y))
		self.move(indicador.getPos())


class Sol():
	def __init__(self):
		self.surface = pygame.image.load("lua.png").convert()
		self.surface.set_colorkey((0,0,0))
		self.nuvem = pygame.image.load("nuvem.png").convert()
		self.nuvem.set_colorkey((0,0,0))
		#posicao do puto
		self.x = 0
		self.y = 0
		self.x2 = 40
		self.y2 = 0
		
	def atualizaSol(self ,pos):
		if pos > 0 and pos <= 7:
			self.surface = pygame.image.load("sol.png").convert()
			self.surface.set_colorkey((0,0,0))
		elif pos > 7:
			self.surface = pygame.image.load("InkSun.png").convert()
			self.surface.set_colorkey((0,0,0))
		else:
			self.surface = pygame.image.load("lua.png").convert()
			self.surface.set_colorkey((0,0,0))
		
	def set_surface(self, imagem):
		self.surface = pygame.image.load(imagem).convert()
		self.surface.set_colorkey((0,255,0))
	def draw(self, surface, pos):
		surface.blit(self.surface, (self.x, self.y))
		if pos > 0:
			if pos < 8:
				surface.blit(self.nuvem, (self.x2 + ((pos-1)*10), self.y2))
			for j in range(0,indicador.getPos(), 1):
				raios[j].mudaCorDoRaio(indicadorh.getpos())
				raios[j].draw(screen)

class Indicador():
	move_speed = 25
	
	
	def __init__(self):
		self.sol = Sol()
		self.pos=0
		self.surface = pygame.image.load("indicador.png").convert()
		self.surface.set_colorkey((0,0,0))

		
		#posicao do puto
		self.x = 527
		self.y = 37
		
	def key_pressed(self, key):
		if key == K_LEFT:
			if self.pos > 0:
				self.pos -= 1
				self.x -= self.move_speed
				self.sol.atualizaSol(self.pos)
				
				
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
		
			
			

class IndicadorH():
	move_speed = 25
	
	
	def __init__(self):
		self.sol = Sol()
		self.pos=3
		self.surface = pygame.image.load("indicadorh.png").convert()
		self.surface.set_colorkey((0,0,0))

		#posicao do puto
		self.x = 687
		self.y = 213
		
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
	circuito = (pygame.image.load("PlacasDeNP.png"),(100,100))
	back  = (pygame.image.load("background.png"),(0,0))
	amperimetro = (pygame.image.load("amperimetro.png").convert(),(0,145))
	amperimetro[0].set_colorkey((0,0,0))	
	intensidade_bar = (pygame.image.load("barra_intensidade.png"),(500,0))
	frequencia_bar = (pygame.image.load("frequencia.png"),(635,95))
	
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
		funcoes.draw(screen, indicador.getPos(), indicadorh.getpos())
		screen.blit(self.amperimetro[0], self.amperimetro[1])
		
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


			
funcoes = FuncoesFisicas()
raios = []
eletrons = []
for i in range(0, 102):
	eletrons.append(Eletron())
for i in range(0,8):
	raios.append(Raio())
indicador = Indicador()			
indicadorh = IndicadorH()
exp = EfeitoVoltaico()
exp.run()	

