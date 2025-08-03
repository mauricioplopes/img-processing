'''
Universidade Estadual de Campinas
Instituto de Computação

MO443 - Introdução ao Processamento Digital de Imagem - 1S2023
Professor Hélio Pedrini

Trabalho 01


Aluno:
Maurício Pereira Lopes
RA: 225242
'''

# ------------------------------------------
# Carregamento de bibliotecas
import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
import random
# ------------------------------------------


# ------------------------------------------
# Questão 1.7 - Planos de Bits
# ------------------------------------------

# lendo ima imagem
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')

# definindo uma lista dos planos de bits a serem plotados
plano_bit = [0, 1, 2, 3, 4, 5, 6, 7]

# gerando as imagens dos planos de bits e salvando em uma lista
new_im_list = []
for i in plano_bit:
    new_im_list.append(im & (2 ** i))

# plotando as imagens
plano_bit_idx = 0
fig, axs = plt.subplots(2, 4, figsize=(15, 8))
for i in range(2):
    for j in range(4):
    	if plano_bit_idx < 8:
        	axs[i, j].imshow(new_im_list[plano_bit_idx], cmap='gray')
        	axs[i, j].set_title(label = ("plano de bit = " + str(plano_bit[plano_bit_idx])))
        	axs[i, j].axis("off")
        	plano_bit_idx = plano_bit_idx + 1
plt.savefig("trabalho01-questao1.7.png")
plt.show()