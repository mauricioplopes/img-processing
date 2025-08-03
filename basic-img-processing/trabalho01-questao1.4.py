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
# Questão 1.4 - Imagens coloridas
# ------------------------------------------


# ------------------------------------------
# (a) dada uma imagem colorida no formato RGB,
# altere a imagem conforme as seguintes operações
#
# R' = 0.393R + 0.769G + 0.189B
# G' = 0.349R + 0.686G + 0.168B
# B' = 0.272R + 0.534G + 0.131B
# ------------------------------------------

# lendo uma imagem colorida
im_color = iio.imread('https://webpages.tuni.fi/imaging/tampere17/t095.png')

# cálculos
nova_im = np.ones((512, 512, 3))
nova_im[:, :, 0] = im_color[:, :, 0] * 0.393 + im_color[:, :, 1] * 0.769 + im_color[:, :, 2] * 0.189
nova_im[:, :, 1] = im_color[:, :, 0] * 0.349 + im_color[:, :, 1] * 0.686 + im_color[:, :, 2] * 0.168
nova_im[:, :, 2] = im_color[:, :, 0] * 0.272 + im_color[:, :, 1] * 0.534 + im_color[:, :, 2] * 0.131

# ajusde da imagem para profundidade de 0 a 255
nova_im = (((nova_im - nova_im.min()) * 255) / (nova_im.max() - nova_im.min())).astype(int)


# ------------------------------------------
# (b) dada uma imagem colorida no formato RGB,
# altere a imagem tal que ela contenha apenas
# uma banda de cor, cujos valores são calculados
# pela médis ponderada:
#
# I = 0.2989R + 0.5870G + 0.1140B
# ------------------------------------------
I = np.array((512, 512))
I = (im_color[:, : , 0] * 0.2989 + im_color[:, : , 1] * 0.5870 + im_color[:, : , 2] * 0.1140).astype(int)



# ------------------------------------------
# plot das imagens
# ------------------------------------------
imagens = [im_color, nova_im, I]
labels = ["Original", "Alterada", "Uma banda de cor"]
fig, axs = plt.subplots(1, 3, figsize=(10, 5))
for i in range(3):
	axs[i].imshow(imagens[i], cmap = "gray")
	axs[i].set_title(label = labels[i])
	axs[i].axis("off")
plt.savefig("trabalho01-questao1.4.png")
plt.show()






















