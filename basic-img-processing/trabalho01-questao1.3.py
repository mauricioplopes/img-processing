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
# Questão 1.3 - Transformação de Intensidade
# ------------------------------------------

# ------------------------------------------
# (a) Dada uma imagem monocromática
# ------------------------------------------
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/city.png')

# ------------------------------------------
# (b) obter o negativo da imagem
# ------------------------------------------
im_negativa = 255 - im

# ------------------------------------------
# (c) converter o intervalo de intensidades para [100, 200]
# ------------------------------------------
lim_sup = 200
lim_inf = 100
im_contraste = ((im * ((lim_sup - lim_inf) / 255)) + lim_inf).astype(np.uint8)

# ------------------------------------------
# (d) inverter os valores dos pixels das linhas pares da imagem
# ------------------------------------------
im_linhas_inv = im.copy()

for r in range(0, 512, 2):
    im_linhas_inv[r, :] = im[r, ::-1]

# ------------------------------------------
# (e) espelhar as linhas da metade superior da imagem
# na parte inferior da imagem
# ------------------------------------------
im_espelhada = im.copy()

im_espelhada[256:, :] = im_espelhada[0:256, :][::-1, ...]

# ------------------------------------------
# (f) aplicar um espelhamento vertical na imagem
# levando-se em conta todas as linhas da imagem
# ------------------------------------------
im_flip_vertical = im.copy()

im_flip_vertical = im_flip_vertical[::-1, ...]


# ------------------------------------------
# plotar e salvar as imagens
# ------------------------------------------
imagens = np.array([["Original", "Negativo", "Intensidades de 100 a 200", "Linhas pares invertidas", "Espelhar metade", "Espelhamento vertical"],
                    [im, im_negativa, im_contraste, im_linhas_inv, im_espelhada, im_flip_vertical]],
                  dtype = "object")
fig, axs = plt.subplots(2, 3, figsize = (12, 7))

im_idx = 0
for i in [0, 1]:
    for j in [0, 1, 2,]:
        axs[i, j].imshow(imagens[1, im_idx], cmap = "gray")
        axs[i, j].set_title(imagens[0, im_idx])
        axs[i, j].axis("off")
        im_idx = im_idx + 1
plt.savefig("trabalho01-questao1.3.png")
plt.show()




















