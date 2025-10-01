import cv2
import numpy as np
import random
import pandas as pd

img_original = cv2.imread("mancha.png", cv2.IMREAD_GRAYSCALE)
h, w = img_original.shape
img_con_puntos = img_original.copy()
resultados = []
coordenadas_utilizadas = set() 
num_tiros = 10000

# Verificar que no sea una coordenada ya usada
for i in range(num_tiros):
    intentos = 0
    while intentos < 100:
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        

        if (x, y) not in coordenadas_utilizadas:
            coordenadas_utilizadas.add((x, y))
            break
        intentos += 1
    
# Verificar en la imagen original.
    valor_pixel = img_original[y, x]
    
    if valor_pixel >= 200:
        color = "Blanco"
    else:
        color = "No blanco"
    
    resultados.append({
        "Tiro N": i + 1,
        "Color": color,
        "Coordenada X": x,
        "Coordenada Y": y,
        "Valor Pixel": valor_pixel
    })
    
    # Dibujar en la copia de visualización
    img_con_puntos = cv2.circle(img_con_puntos, (x, y), 1, 0, -1)

df = pd.DataFrame(resultados)
df.to_csv("resultados_tiros.csv", index=False)

# Mostrar estadísticas
blancos = len(df[df["Color"] == "Blanco"])
no_blancos = len(df[df["Color"] == "No blanco"])
print(f"\nEstadísticas:")
print(f"Blancos: {blancos} ({blancos/num_tiros*100:.1f}%)")
print(f"No blancos: {no_blancos} ({no_blancos/num_tiros*100:.1f}%)")

cv2.imshow("Original", img_original)
cv2.imshow("Con puntos", img_con_puntos)
cv2.waitKey(0)
cv2.destroyAllWindows()
