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
# Questão 1.8 - Filtragem de Imagens
# ------------------------------------------

# ler uma imagem
im = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')


# definir os filtros
h1 = np.array([[0, 0, -1, 0, 0],
              [0, -1, -2, -1, 0],
              [-1, -2, 16, -2, -1],
              [0, -1, -2, -1, 0],
              [0, 0, -1, 0, 0]])

h2 = (1 / 256) * np.array([[1, 4, 6, 4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1, 4, 6, 4, 1]])

h3 = np.array([[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]])

h4 = np.array([[-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]])

h5 = np.array([[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]])

h6 = (1 / 9) * np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])

h7 = np.array([[-1, -1, 2],
              [-1, 2, -1],
              [2, -1, -1]])

h8 = np.array([[2, -1, -1],
              [-1, 2, -1],
              [-1, -1, 2]])

h9 = (1 / 9) * np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1]])

h10 = (1 / 8) * np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 8, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]])

h11 = np.array([[-1, -1, 0],
               [-1, 0, 1],
               [0, 1, 1]])


# definir uma função que recebe a imagem 512 por 512, e o filtro a ser aplicado
def filtrar(img, filtro):
    pad_size = int(filtro.shape[0] / 2)
    img_pad = np.pad(img, pad_size, mode = "reflect")
    new_img = np.ones((512, 512))
    
    for i in range(512):
        for j in range(512):
            new_img[i, j] = np.sum(img_pad[i:filtro.shape[0]+i, j:filtro.shape[1]+j] * filtro)
            
    new_img = ((new_img - new_img.min()) * 255) / (new_img.max() - new_img.min())
    

    
    return new_img


# aplicar os filtros solicitados e salvar as imagens em uma lista
im_filtradas = [im]
filtros = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11]
for i in filtros:
    im_filtradas.append((filtrar(im, i)).astype(np.uint8))

# aplicar os filtros h3 e h4 combinados
img_filtrada_h3 = filtrar(im, h3)
img_filtrada_h4 = filtrar(im, h4)
img_comb = np.sqrt((img_filtrada_h3) ** 2 + (img_filtrada_h4) ** 2).astype(int)
im_filtradas.append(img_comb)


# plotar e salvar arquivo com as imagens filtradas
labels = ["Original", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h3h4"]
labels_idx = 0
fig, axs = plt.subplots(4, 4, figsize=(10, 12))
for i in range(4):
    for j in range(4):
    	if labels_idx < 13:
        	axs[i, j].imshow(im_filtradas[labels_idx], cmap='gray', vmin=0, vmax=255)
        	axs[i, j].set_title(label = (str(labels[labels_idx])))
        	axs[i, j].axis("off")
        	labels_idx = labels_idx + 1
fig.delaxes(axs[3,1])
fig.delaxes(axs[3,2])
fig.delaxes(axs[3,3])
plt.savefig("trabalho01-questao1.8.png")
plt.show()







