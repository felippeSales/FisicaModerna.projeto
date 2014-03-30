# coding: utf- 08

import pygame
import random
import time
import sys

from pygame.locals import *

def fase_um():
	class Square:

		def __init__(self):
			self.rect_sq = pygame.image.load("Imagens/square.png").get_rect()
			self.rect_sq.x = 0
			self.rect_sq.y = 520
			
		# Poe uma imagem no objeto: 
		def set_surface(self, imagem):
			self.surface = pygame.image.load(imagem).convert()
			self.surface.set_colorkey((0,255,0))

	class Plataforma:
		def __init__(self):
			self.rect_base = pygame.image.load("Imagens/teste.png").get_rect()
			self.rect_base.x = 430
			self.rect_base.y = 450
		def set_surface(self, imagem):
			self.surface = pygame.image.load(imagem).convert()
			self.surface.set_colorkey((0,255,0))
				
	class Chao:
		def __init__(self):
			self.rect_chao = pygame.image.load("Imagens/chao_1.png").get_rect()
			self.rect_chao.x = 0
			self.rect_chao.y = 570
		def set_surface(self, imagem):
			self.surface = pygame.image.load(imagem).convert()
			self.surface.set_colorkey((0,255,0))

	class Pedra:
		def __init__(self):
			self.rect_pedra = pygame.image.load("Imagens/pedra.png").get_rect()
			self.rect_pedra.x = random.randint(67,579)
			self.rect_pedra.y = -100
		def set_surface(self, imagem):
			self.surface = pygame.image.load(imagem).convert()
			self.surface.set_colorkey((255,255,255))

	class Jogo:
		
		def __init__(self):
			pygame.init()
			self.screen = pygame.display.set_mode((650,650),0,32)
			pygame.display.set_caption("Square Advetures")        
			self.character = Square()
			self.chao = Chao()
			self.rock = Pedra()
			self.checkpoint = (0,520)
			
	# Camera:
			self.camera1 = False
			self.camera2 = False
			self.camera3 = False
			self.contador_camera = 0
			self.contador_camera2 = 0
			self.contador_camera3 = 0
								
	# BASES:
			self.base = Plataforma()
			self.base2 = Plataforma2()
			self.base3 = Plataforma3()
			self.base4 = Plataforma4()
			self.base5 = Plataforma5()
			self.base6 = Plataforma6()
					
	# Lista dos retangulos
			self.bases = [self.base.rect_base, self.base2.rect_base, self.base3.rect_base
			, self.base4.rect_base, self.base5.rect_base, self.base6.rect_base] 
			
	# Coordenadas dos retangulos para o 1° estagio:		
			self.coordenadas1 = [(250,500),(100,400),(280,300), (450,200),(280,80)]				
	# Coordenadas dos retangulos para o 2° estagio:		
			self.coordenadas2 = [(110,520),(280,400),(450,280), (280,150),self.base5.rect_base,
			(110,55)]
	# Coordenadas dos retangulos para o 3° estagio:		
			self.coordenadas3 = [(290,500),(100,400),(280,350), (450,280),(310,150)]
			
			"""
			Direcao a qual o personagem esta voltado:
			True == Direita
			False == Esquerda
			None == virado pra tela
			"""
			self.direcao = None
			self.move_speed = 10
			
	# Instrucoes para o pulo:
			self.pulo = False
			self.x_p = 0
			self.y_p = 0     
			self.len_pulo = 12
			
			self.clock = pygame.time.Clock();
			pygame.key.set_repeat(75)
			
	# Coordenadas do Background: 
			self.back_y = -1753

		##def game_over(self):
			
		def mata_person(self):
			time.sleep(1)
			self.character.rect_sq.x = self.checkpoint[0]
			self.character.rect_sq.y = self.checkpoint[1]
			if self.camera3 == False:
				self.rock.rect_pedra.y = 0
				self.rock.rect_pedra.x = random.randint(67,579)
			self.pulo = False
			self.contador = 0
			self.y_p = 0
			self.x_p = 0
			self.direcao = None
			game.character.set_surface("Imagens/square.png")
			self.screen.blit(self.character.surface,(self.character.rect_sq))
			
		def muda_fase(self):
			if self.camera3 == True:
				if self.character.rect_sq.colliderect(self.base5.rect_base):
					sys.exit()
		
		def atualiza_tela(self):
	# Atualiza a tela:
			self.screen.blit(self.background,(0,self.back_y))
			# Atualiza bases:
			for base in self.bases:
				self.screen.blit(self.base.surface,(base))
			self.screen.blit(self.character.surface,(self.character.rect_sq))
			self.screen.blit(self.rock.surface,(self.rock.rect_pedra))
			pygame.display.flip()

		def colisao_chao(self):
			if self.character.rect_sq.colliderect(self.chao.rect_chao):
				self.apoiado_c = True
				self.character.rect_sq.y = (self.chao.rect_chao.y - 43)
				self.back_y = -1753
			else:
				self.apoiado_c = False
				
		def colisao_base(self):
			verificador = 0  
			for base in self.bases:
				if self.character.rect_sq.colliderect(base) == True:
					self.apoiado_b = True
					self.character.rect_sq.y = (base[1] - 43)
					verificador = 1
					if base == self.base6.rect_base and self.base6.rect_base[1] == 50:
						self.camera1 = True
						
					if base == self.base5.rect_base and self.base5.rect_base[1] == 80:
						self.camera2 = True
						
					if base == self.base6.rect_base and  self.camera2 == True :
						self.camera3 = True
						
			if verificador == 0:
				self.apoiado_b = False

		def colisao_pedra(self):
			if self.character.rect_sq.colliderect(self.rock.rect_pedra) == True:
				self.stop_pedra = True
				if self.direcao == True:
					game.character.set_surface("Imagens/squarehit_r.png")
					self.character.surface.set_colorkey((255,255,255))
					
				else:
					game.character.set_surface("Imagens/squarehit_l.png")
					self.character.surface.set_colorkey((255,255,255))
					
				self.kill = True
			else:
				self.stop_pedra = False
				self.kill = False
		
		def gravity(self,chao,pulo,base):
			gravidade = 10
		# Movimenta a pedra
			if self.stop_pedra == False and self.camera3 == False: #and self.movendo_camera == False:
				self.rock.rect_pedra.y += 10
			if chao == False and pulo == False and base == False:
				self.character.rect_sq.y += gravidade
		# Reinicia a posição da pedra
			if self.rock.rect_pedra.y > 2000:
				self.rock.rect_pedra.y = 0
				self.rock.rect_pedra.x = random.randint(67,579)				

	# Verifica as teclas pressionadas e movimenta o personagem: 
		def key_pressed(self, key):
			"""if key == K_DOWN:
				self.back_y -= self.move_speed
				self.chao.rect_chao.y -= self.move_speed
				for base in self.bases:
					base[1] -= self.move_speed
								
			if key == K_UP:
				self.back_y += self.move_speed
				self.chao.rect_chao.y += self.move_speed
				for base in self.bases:
					base[1] += self.move_speed"""
				
			if key == K_LEFT:
				game.character.set_surface("Imagens/square_3.png")
				if (self.character.rect_sq.x - self.move_speed) >= 0:
					self.character.rect_sq.x -= self.move_speed
					self.direcao = False
				
			if key == K_RIGHT:
				game.character.set_surface("Imagens/square_2.png")
				if (self.character.rect_sq.x + self.move_speed) <= 600:
					self.character.rect_sq.x += self.move_speed
					self.direcao = True
			
		def movimenta_camera(self):
			if self.contador_camera <= 560:
				cam_velo = 5
				self.back_y += cam_velo
				self.chao.rect_chao.y += cam_velo
				for base in self.bases:
					base[1] += cam_velo		
				self.contador_camera += cam_velo
				
		def movimenta_camera2(self):
			if self.contador_camera2 <= 535:
				cam_velo = 5
				self.back_y += cam_velo
				self.chao.rect_chao.y += cam_velo
				for base in self.bases:
					base[1] += cam_velo		
				self.contador_camera2 += cam_velo
				
		def movimenta_camera3(self):
			if self.contador_camera3 <= 560:
				cam_velo = 5
				self.back_y += cam_velo
				self.chao.rect_chao.y += cam_velo
				for base in self.bases:
					base[1] += cam_velo		
				self.contador_camera3 += cam_velo
				self.rock.rect_pedra.y = -100
	# Redefine as posicoes das bases, e o checkpoint:						
		def bases_estagio1(self):
			if self.back_y == -1188:
				for i in range(len(self.coordenadas1)):
					(self.bases[i])[0] = self.coordenadas1[i][0]
					(self.bases[i])[1] = self.coordenadas1[i][1]
				self.movendo_camera = False
				self.checkpoint = (self.base6.rect_base[0],self.base6.rect_base[1])
		def bases_estagio2(self):
			if self.back_y == -648:
				for i in range(len(self.coordenadas2)):
					(self.bases[i])[0] = self.coordenadas2[i][0]
					(self.bases[i])[1] = self.coordenadas2[i][1]
				self.movendo_camera = False
				self.checkpoint = (self.base5.rect_base[0],self.base5.rect_base[1])
		def bases_estagio3(self):
			if self.back_y == -83:
				for i in range(len(self.coordenadas3)):
					(self.bases[i])[0] = self.coordenadas3[i][0]
					(self.bases[i])[1] = self.coordenadas3[i][1]
				self.movendo_camera = False
				self.checkpoint = (self.base6.rect_base[0],self.base6.rect_base[1])
	#########################################3
			
		def set_background(self, imagem):
			self.background = pygame.image.load(imagem).convert()
						
	# Roda o jogo, frame a frame:
		def run(self):     
			self.contador = 0
			self.apoiado_b = False
			self.apoiado_c = False
			self.stop_pedra = False
			self.kill = False
			while True:
				self.clock.tick(40)
				
				self.colisao_base()
				self.colisao_chao()
				self.colisao_pedra()
				
				for event in pygame.event.get():
					# Fecha o jogo
					if event.type == QUIT:
						sys.exit()
					if event.type == KEYDOWN:
						self.key_pressed(event.key)
							
						# Inicia o pulo:
						if event.key == K_SPACE:
							if self.apoiado_c == True or self.apoiado_b == True:
								self.pulo = True
												
				# Pulo:
				if self.pulo == True:
					self.contador += 1	
					# Subida:
					if self.contador <= self.len_pulo:
						self.y_p += 2
						self.character.rect_sq.y -= self.y_p
						# Limites do Pulo:
						if self.direcao == True:
							if (self.character.rect_sq.x + 1)<= 600:
								self.x_p += 1
								self.character.rect_sq.x += self.x_p
						elif self.direcao == False:
							if (self.character.rect_sq.x - 1)>= 0:
								self.x_p += 1
								self.character.rect_sq.x -= self.x_p
					# Descida:
					if self.contador >= self.len_pulo and self.contador < (2*self.len_pulo):
						if self.apoiado_b == False and (self.character.rect_sq.y + self.y_p) < self.chao.rect_chao.y:
							self.character.rect_sq.y += self.y_p
							self.y_p -= 2
						
						# Limites do Pulo:
						if self.direcao == True:
							if (self.character.rect_sq.x + 1)<= 600:
								self.character.rect_sq.x += self.x_p
								self.x_p -= 1
						elif self.direcao == False:
							if (self.character.rect_sq.x - 1)>= 0:
								self.x_p -= 1
								self.character.rect_sq.x -= self.x_p								
						
											
					# Volta as condições iniciais:
					if self.contador == (2*self.len_pulo):
						self.pulo = False
						self.contador = 0
						self.y_p = 0
						self.x_p = 0
							
				# Movimentacao Cameras:
				if self.camera1 == True:
					self.movimenta_camera()
					self.bases_estagio1()
							
				if self.camera2 == True:
					self.movimenta_camera2()
					self.bases_estagio2()
				
				if self.camera3 == True:
					self.movimenta_camera3()
					self.bases_estagio3()
				############################
																
				self.gravity(self.apoiado_c,self.pulo,self.apoiado_b)
											
				self.atualiza_tela()
				
				if self.kill == True:
					self.mata_person()
				
				self.muda_fase()

	# Executa o jogo e define os locais das imagens:				
	game = Jogo()
	game.set_background("Imagens/background_2.png")
	game.character.set_surface("Imagens/square.png")
	game.base.set_surface("Imagens/base_1.png")
	game.chao.set_surface("Imagens/chao_1.png")
	game.rock.set_surface("Imagens/pedra.png")
	game.run()

fase_um()
