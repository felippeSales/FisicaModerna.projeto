# coding: utf- 08

import pygame
import random
import time
import sys

from pygame.locals import *
	
class experimento:
	def __init__(self):
			self.comprimento_de_onda = 500.0
			self.intensidade = 0.0
			self.corrente = 0.0
			
class luz:
	def _init_(self):
		self.intensidade = 0.0
		self.comprimento_de_onda = 0.0
	def mudaCor(intensidade, cdo)
		self.intensidade = intensidade
		self.comprimento_de_onda  = cdo
class eletron:
	def _init_(self)
		self.velocidade = 0
	def mudaVelocidade(nova)
		self.vecocidade =nova
	
	
	
def main():
		experimento = Experimento()
		experimento.set_background("Imagens/background_2.png")
		experimento.character.set_surface("Imagens/square.png")
		experimento.base.set_surface("Imagens/base_1.png")
		experimento.chao.set_surface("Imagens/chao_1.png")
		experimento.rock.set_surface("Imagens/pedra.png")
		experimento.run()