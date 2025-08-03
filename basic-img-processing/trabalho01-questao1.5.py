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
# Questão 1.5 - Ajuste de Brilho
# ------------------------------------------

# ------------------------------------------
# lendo uma imagem
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')

# definindo os valores de gama
gamma = [1, 1.5, 2.5, 3.5]

# convertendo os pixels para os valores de 0 a 1
im_0_to_1 = ((im * ((1 - 0) / 255)) + 0)

# aplicando a equação B = A ** (1/gamma)
# e salvando as imagens em uma lista de arrays
# após convertê-las de volta para 0 a 255
im_B = []
for i in range(4):
    im_B.append(im_0_to_1 ** (1/gamma[i]))
    im_B[i] = (im_B[i] * 255).astype(int)


# plotando as imagens
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
for i in range(4):
    axs[i].imshow(im_B[i], cmap='gray')
    axs[i].set_title(label = ("gamma = " + str(gamma[i])))
    axs[i].axis("off")
plt.savefig("trabalho01-questao1.5.png")
plt.show()