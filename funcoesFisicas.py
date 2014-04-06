# frequencia = n x 10 ^ 12
violeta = 789.0
azul = 668.0
verde = 606.0
amarelo = 526.0
vermelho = 484.0
# Um metro
comprimento = 1.0

cargaEletron = 1.6 * (10**(-19))
massaEletron = 9.11 * (10**(-31))

# -34 + 12 da frequencia
planck = 6.63 * (10 ** (-34 + 12))

# Potassio
funcaoTrabalhoPotassio = 2.3 * cargaEletron

def energia_cinetica(frequencia , funcaoTrabalho):
	energia = planck*frequencia - funcaoTrabalho
	
	#Se a energia for negativa ele nao arranca eletrons 
	if energia < 0:
		energia = 0

	return energia

def velocidade(frequencia, funcaoTrabalho):
	# 0.5 representa a raiz quadrada
	return (2 * energia_cinetica(frequencia, funcaoTrabalho) / massaEletron) ** (0.5)

def tempo(frequencia, funcaoTrabalho):
	v = velocidade(frequencia, funcaoTrabalho)

	if v == 0:
		return 0.0

	return comprimento / velocidade(frequencia, funcaoTrabalho)

def calcula_corrente(frequencia, funcaoTrabalho, numeroEletrons):
	t = tempo(frequencia, funcaoTrabalho)
	
	if t == 0:
		return 0.0

	return 	(numeroEletrons * cargaEletron) / t 
	

max = calcula_corrente(violeta, funcaoTrabalhoPotassio, 8)
print calcula_corrente(verde, funcaoTrabalhoPotassio, 4) / max
