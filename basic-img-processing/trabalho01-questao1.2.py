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
# Questão 1.2 - Combinação de imagens
# Combinar duas imagens monocromaticas de mesmo tamanho por meio da média
# ponderada de seus níveis de cinza.
# ------------------------------------------

# ler duas imagens
im_A = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/baboon.png')
im_B = iio.imread('https://www.ic.unicamp.br/~helio/imagens_png/butterfly.png')

# calcular as imagens combinadas, plotar e salvar as imagens
pesos = np.array([0.2, 0.5, 0.8])
fig, axs = plt.subplots(1, 3, figsize=(15, 6))
fig.suptitle('Imagens combinadas', fontsize=24)



for c in range(3):
    im_comb = im_A * pesos[c] + im_B * pesos[-(c + 1)]
    axs[c].imshow(im_comb, cmap='gray')
    label = 'A * ' + str(pesos[c]) + ' + B * ' + str(pesos[-(c + 1)])
    axs[c].set_title(label)
    axs[c].axis("off")
plt.savefig("trabalho01-questao1.2.png")
plt.show()