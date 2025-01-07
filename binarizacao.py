import cv2  # Importa a biblioteca OpenCV
import numpy as np  # Importa o numpy para operações matriciais

# Lê a imagem original do disco
img = cv2.imread('Weiss.jpeg')

# Converte a imagem para escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica o blur (suavização) na imagem em escala de cinza
suave = cv2.GaussianBlur(img_gray, (7, 7), 0)

# Realiza a binarização da imagem. Pixels abaixo de um limiar são 0 (preto), e acima de 160 são 255 (branco)
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)

# Converte a imagem em escala de cinza de volta para 3 canais para combinar com a imagem colorida
img_gray_3channel = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# Converte a imagem binarizada (2D) para 3 canais para combinar com a imagem de 3 canais
bin_3channel = cv2.cvtColor(bin, cv2.COLOR_GRAY2BGR)

# Combina as imagens em uma única saída (imagem original, em escala de cinza e binarizada)
resultado = np.vstack([
    np.hstack([img, img_gray_3channel]),  # Original e escala de cinza (3 canais)
    np.hstack([bin_3channel, cv2.bitwise_and(img_gray_3channel, img_gray_3channel, mask=bin)])  # Binária e máscara
])

# Exibe as imagens combinadas (original, cinza e binarizada)
cv2.imshow("Resultado da Binarizacao", resultado)

# Espera um evento do teclado para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()

