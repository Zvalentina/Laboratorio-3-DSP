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


**parte C**
Tras mirar las seis señales de voz (tres femeninas y tres masculinas) se puede ver  diferencias entre los parámetros  de ambos grupos.

**Comparación de la frecuencia fundamental.**
Las voces femeninas presentan frecuencias fundamentales  en el rango de 180 a 250 Hz mientras que las masculinas se ubican entre 90 y 140 Hz. Esta diferencia se debe a que las cuerdas vocales de las mujeres son más cortas y ligeras, lo que produce vibraciones más rápidas y por esto tonos más agudos en contraste las cuerdas vocales masculinas son más largas y gruesas  generando una frecuencia fundamental más baja.

**Diferencias en brillo y frecuencia media.**
El brillo (energía relativa en frecuencias altas) fue mayor en las voces femeninas mostrando picos más definidos y una mayor densidad de armónicos en la región superior a los 1500 Hz.
Las voces masculinas mostraron menos brillo concentrando la energía en frecuencias graves lo que se asocia con un timbre más oscuro y menos resonante.

**Intensidad y energía total.**
La intensidad varió ligeramente según el volumen de grabación pero en promedio no se observaron diferencias significativas entre géneros sin embargo se notó que las señales femeninas tendían a una mayor variación de amplitud mientras que las masculinas fueron más estables.

**Análisis de estabilidad vocal (Jitter y Shimmer).**
Los parámetros de estabilidad temporal reflejan la regularidad en la vibración de las cuerdas vocales:

El Jitter relativo (%) fue levemente mayor en algunas voces femeninas (≈ 0.8–1.0%), lo cual indica pequeñas fluctuaciones en la frecuencia fundamental.
El Shimmer relativo (%) fue más alto en las mujeres (≈ 3–4%) que en los hombres (≈ 2–3%), evidenciando mayor variabilidad en la amplitud de los ciclos glóticos.

Estos resultados son consistentes con estudios fisiológicos que indican que las mujeres tienden a presentar mayor variabilidad acústica debido a diferencias anatómicas y hormonales.

El análisis comparativo también demuestra la utilidad biomédica de los parámetros Jitter y Shimmer ya que variaciones elevadas en estos valores podrían indicar trastornos  o lesiones en las cuerdas vocales en condiciones normales se espera que el jitter relativo sea menor al 1% y el shimmer menor al 5% tal como se observó en las grabaciones analizadas lo que sugiere voces saludables y estables.

**Interpretación general**
En conjunto las voces femeninas presentan mayor frecuencia fundamental y brillo menor estabilidad de amplitud y frecuencia y espectros  en armónicos altos y en las voces masculinas en cambio tenen frecuencias más bajas menor brillo y una mayor estabilidad temporal lo cual se traduce en un timbre más uniforme.

# 6. Análisis de resultados.

Se analizaron seis señales de voz (tres femeninas y tres masculinas) grabadas en formato .wav con una frecuencia de muestreo de 44.1 kHz y una duración promedio de 5 segundos a  continuacion se presentan los hallazgos más relevantes del procesamiento en el dominio del tiempo y la frecuencia:

**Transformada de Fourier (FFT).**
Las gráficas en el dominio de la frecuencia mostraron una distribución característica entre los dos grupos:
Las voces femeninas presentaron frecuencias fundamentales  más altas situadas entre 180 Hz y 250 Hz lo que se muestra en un timbre más agudo las voces masculinas mostraron un promedio entre 90 Hz y 140 Hz evidenciando un espectro más concentrado en bajas frecuencias lo cual se asocia a un tono más grave el cálculo de la frecuencia media y el brillo permitió identificar que las señales femeninas poseen una mayor energía  por encima de los 1500 Hz mientras que las masculinas concentran la energía por debajo de este rango la energía totalvarió ligeramente entre sujetos influenciada por el volumen y la distancia al micrófono pero sin alterar las tendencias espectrales observadas.

**Mujer 1:**

<img width="780" height="298" alt="image" src="https://github.com/user-attachments/assets/e519b8c8-83c9-445f-9466-7aafaf303ed8" />
<img width="788" height="235" alt="image" src="https://github.com/user-attachments/assets/f8e7435f-9ae4-4618-a715-b964b0e6235a" />

**Mujer 2:**

<img width="787" height="298" alt="image" src="https://github.com/user-attachments/assets/f6c8eb78-cff6-46c0-8e1b-cdb88fbc7bf5" />
<img width="783" height="230" alt="image" src="https://github.com/user-attachments/assets/bf14318b-42f5-45c4-a3da-56cd8f27c580" />

**Mujer 3:**

<img width="782" height="296" alt="image" src="https://github.com/user-attachments/assets/33210b1b-3d48-4eba-8461-1cb2a382dc34" />
<img width="787" height="232" alt="image" src="https://github.com/user-attachments/assets/54d39864-b7b6-417d-9809-642d7beb1d5d" />

**Hombre 1:**

<img width="786" height="296" alt="image" src="https://github.com/user-attachments/assets/7127f185-547a-41ae-bc68-57ee1dc61efe" />
<img width="785" height="239" alt="image" src="https://github.com/user-attachments/assets/24abb1e0-582c-499f-9d74-5bdabe3013be" />

**Hombre 2:**

<img width="786" height="299" alt="image" src="https://github.com/user-attachments/assets/8c4c2453-77c7-48ff-bf3a-dcae6f6af8b4" />
<img width="789" height="235" alt="image" src="https://github.com/user-attachments/assets/de6fadcb-d792-4e7b-b947-8daaee25ff0d" />

**Hombre 3:**

<img width="782" height="299" alt="image" src="https://github.com/user-attachments/assets/6bcf1f43-17ee-48b2-b1bb-7997aade6578" />
<img width="783" height="228" alt="image" src="https://github.com/user-attachments/assets/4fc3fa18-52ea-476d-aeaa-6682cfa5edb5" />


**Filtrado pasabanda FIR**
Se implementó un filtro FIR pasabanda con las siguientes bandas
Mujeres: 150–500 Hz  Hombres: 80–400 Hz.
El filtrado permitió eliminar el ruido de baja y alta frecuencia manteniendo únicamente la banda donde se concentra la voz las señales filtradas mostraron una reducción notable de interferencias y un contorno de onda más regular lo que facilita la detección de picos y cruces por cero en etapas posteriores (Jitter y Shimmer).

**Medición de Jitter y Shimmer**
El Jitter mide la variación en la frecuencia fundamental entre ciclos consecutivos mientras que el Shimmer cuantifica las variaciones de amplitud los resultados obtenidos para las seis grabaciones se mantuvieron dentro de los rangos típicos de voces normales:

Jitter relativo: menor al 1% en la mayoría de los casos.
Shimmer relativo: entre 2% y 4%, dentro del rango esperado para voces no patológicas.

En general, las voces femeninas mostraron mayor variabilidad en amplitud en el shimmer mientras que las masculinas presentaron mayor estabilidad periódica menor jitte.


# 7. Conclusiones.
Las voces femeninas presentan una frecuencia fundamental significativamente mayor que las masculinas.
La Transformada de Fourier permitió evidenciar diferencias claras en el espectro las mujeres concentran energía en frecuencias altas mientras que los hombres lo hacen en bajas frecuencias.
El filtrado pasabanda FIR fue efectivo para aislar las frecuencias vocales principales y reducir ruido ambiental mejorando la calidad de las características de la señal.
En términos generales estos parámetros son útiles para el diagnóstico temprano.
El análisis espectral confirma que las diferencias de género en la voz se reflejan directamente en la estructura de frecuencias pudiendo ser cuantificadas mediante herramientas de procesamiento digital de señales.

# 8. Aplicaciones biomédicas.
