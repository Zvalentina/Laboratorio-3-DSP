# ANÁLISIS ESPECTRAL DE LA VOZ
# TABLA DE CONTENIDOS
1. Objetivos.
2. Metodología del experimento.
3. Marco coneptual.
4. Diagramas de flujo.
5. Adquisición de la señal.
6. Análisis de resultados.
7. Conclusiones.
8. Aplicaciones biomédicas.

# 1. Objetivos.
La presente práctica tiene como objetivos:
- Capturar y procesar señales de voz masculinas y femeninas.
- Aplicar la Transformada de Fourier como herramienta de análisis espectral de la voz.
- Extraer parámetros característicos de la señal de voz: frecuencia fundamental, frecuencia media, brillo, intensidad, Jitter y Shimmer.
- Comparar las diferencias principales entre señales de voz de hombres y mujeres a partir de su análisis en frecuencia.
- Desarrollar conclusiones sobre el comportamiento espectral de la voz humana en funcion del genero.

# 2. Metodología del experimento.
La presente práctica se hizo empleando técnicas como el cálculo de la transformada de Fourier para cada señal de voz masculina y femenina, para visualizarla en el dominio de la frecuencia. Además, se aplicó un filtro pasabanda para una señal de voz de un hombre y una mujer, con el objetivo de visualizar la señal con menor ruido y finalmente, se hizo la medición de Jitter y Shimmer para determinar si una voz es patológica.

<img width="200" height="300" alt="image" src="https://github.com/user-attachments/assets/ce5f70f6-3188-4bf7-94d7-efd6e6b5b389" />

# 3. Marco Conceptual.
**Transformada de Fourier:** Es una operación matemática de gran importancia para el procesamiento digital de señales, ya que nos permite descomponer una señal que se encuentra en el dominio del tiempo al dominio de la frecuencia, revelando los componentes sinusoidales de diferentes frecuencias.

**Filtrado pasabanda:** Se compone con la union de un filtro pasa alto y uno pasa bajo, en el que su función es permitir el paso de ciertas frecuencias localizadas dentro de un ancho de banda determinado y atenuar las que se encuentran fuera del mismo.

<img width="394" height="197" alt="image" src="https://github.com/user-attachments/assets/346399a4-308b-45c6-a15d-9cbafbd37a56" />


**Medición de Jitter:** Esta operación es importante para el análisis de la calidad vocal, donde se identifican las variaciones en la frecuencia fundamental, lo que puede indicar enfermedades en las cuerdas vocales. Ademas, esta medición puede ayudar a diferenciar de una voz distorsionada o robotizada.

**Medición de Shimmer:** Este tipo de operaciones sirve para identificar y cuantificar las variaciones en la amplitud de la señal de la voz, siendo importante para diagnosticar patologías vocales, como por ejemplo que ellas no se juntan correctamente. El aumento en la medición de Shimmer puede suponer una voz áspera o temblorosa.

# 4. Diagramas de flujo.
# 5. Adquisicón de la señal.
Para adquirir las señales de la voz, se hizo mediante la grabación de un audio de voz de aproximadamente 5 segundos y se guardo en un formato .wav (Waveform Audio File Format), el cual es un formato de audio digital para almacenar sonido. Seguido de esto se importó el archivo en python para visualizar la señal de la voz.

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/1acd61dd-b28c-4427-b0fa-9996e38127f9" />

# 6. Análisis de resultados.
# 7. Conclusiones.
# 8. Aplicaciones biomédicas.
