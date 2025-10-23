# Simulación Monte Carlo para Estimación de Área

## Objetivo
Estimar el área de una mancha de forma irregular mediante el método de Monte Carlo,
utilizando muestreo aleatorio de puntos sobre la imagen.

## Metodología
1. Se genera una distribución uniforme de puntos aleatorios sobre la imagen
2. Se clasifica cada punto según si cae dentro (blanco) o fuera (no blanco) de la mancha
3. El área se estima mediante la proporción: 
   Área_estimada = (Puntos_dentro / Total_puntos) × Área_total_imagen


## EJEMPLO: 
Usando la imagen del "Circulo.png" se estima que el lado del cuadrado es 5.
Ahora Area-cuadrado =5x5= 25, y  π*(R)²= Area-Circulo
