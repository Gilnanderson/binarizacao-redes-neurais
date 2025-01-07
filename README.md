# Binarização de Imagens

Este projeto implementa um algoritmo de binarização de imagens em Python utilizando a biblioteca OpenCV, como parte do desafio proposto. O objetivo do desafio era:

Converter uma imagem colorida para escala de cinza (valores de 0 a 255).
Binarizar a imagem, transformando-a em uma versão preto e branco (valores de 0 e 255).

# Funcionalidades

Carregamento da Imagem: O código carrega uma imagem a partir do disco.
Conversão para Escala de Cinza: A imagem colorida é convertida para escala de cinza.

Binarização: Dois tipos de binarização são aplicados:
  - Binarização simples.
  - Binarização invertida.
Visualização dos Resultados: As etapas do processo são exibidas lado a lado, incluindo:
  - A imagem original.
  - A imagem em escala de cinza.
  - A versão binarizada.
  - A versão com máscara aplicada.
    
# Como o código cumpre o desafio

O código converte a imagem de um espaço de cores RGB para escala de cinza, atendendo à primeira parte do desafio.
A aplicação de thresholds (limiares) permite transformar a imagem em preto e branco, cumprindo a segunda parte do desafio.
Além disso, o código exibe os resultados de forma clara em uma janela, demonstrando as transformações realizadas.
