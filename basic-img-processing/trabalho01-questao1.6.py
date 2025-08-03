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
# Questão 1.6 - Quantização de Imagens
# ------------------------------------------


# lendo uma imagem e a convertendo para níveis de 0 a 1
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')
im_0_to_1 = ((im * ((1 - 0) / 255)) + 0)

# definindo uma lista de níveis de profundidade da imagem
depth = [256, 64, 32, 16, 8, 4, 2]

# fazendo a quantização da imagem e salvando as imagens
# quantizadas em uma lista
im_quantizada = []
for i in range(0, 7):
    im_quantizada.append((im_0_to_1 * depth[i]).astype(int))


# plotando as imagens quantizadas
depth_idx = 0
fig, axs = plt.subplots(2, 4, figsize=(15, 8))
for i in range(2):
    for j in range(4):
        if depth_idx < 7:
            axs[i, j].imshow(im_quantizada[depth_idx], cmap='gray')
            axs[i, j].set_title(label = ("profundidade = " + str(depth[depth_idx])))
            axs[i, j].axis("off")
            depth_idx = depth_idx + 1
fig.delaxes(axs[1,3])
plt.savefig("trabalho01-questao1.6.png")
plt.show()