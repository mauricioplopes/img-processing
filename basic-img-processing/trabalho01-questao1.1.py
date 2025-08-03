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
# Questão 1.1 - Mosaico
# Construir um mosaico de 4x4 blocos a partir de uma imagem monocromática.
# ------------------------------------------

# ler a imagem original
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')

# dividir a imagem original em 16 blocos
# os blocos foram salvos em uma lista
M = im.shape[0] // 4
N = im.shape[1] // 4
sub_imagens = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

# a lista foi reordenada randomicamente
random.shuffle(sub_imagens)

# e convertida em um array de dimensões 16, 128, 128
sub_im_array = np.array(sub_imagens)

# cada uma das 16 sub-imagens foram juntadas novamente em uma única
# imagem final de dimensões 512, 512, mas na ordem aleatório
final_im = np.empty((512, 512))
sub_im_index = 0
for bloco_coluna in range(0, 512, 128):
    for bloco_linha in range(0, 512, 128):
            final_im[bloco_linha:bloco_linha+128, bloco_coluna:bloco_coluna+128] = sub_im_array[sub_im_index]
            sub_im_index = sub_im_index + 1

# plotar e salvar as imagens
images = [im, final_im]
labels = ["Original", "Mosaico"]
fig, axs = plt.subplots(1, 2, figsize=(8, 5))
for i in range(2):
	axs[i].imshow(images[i], cmap = "gray")
	axs[i].set_title(label = labels[i])
	axs[i].axis("off")
plt.savefig("trabalho01-questao1.1.png")
plt.show()


