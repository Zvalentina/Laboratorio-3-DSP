import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

fs= 44000

#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer-1.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Mujer 1")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)  
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental mujer 1:", f_fundamental)
print("Frecuencia media mujer 1:", f_media)
print("Brillo señal mujer 1:", brillo)
print("Intensidad señal mujer 1:",intensidad)
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer -2.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Mujer 2")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental mujer 2:", f_fundamental)
print("Frecuencia media mujer 2:", f_media)
print("Brillo señal mujer 2:", brillo)
print("Intensidad señal mujer 2:",intensidad)
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer -3.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Mujer 3")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental mujer 3:", f_fundamental)
print("Frecuencia media mujer 3:", f_media)
print("Brillo señal mujer 3:", brillo)
print("Intensidad señal mujer 3:",intensidad)
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre_1.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Hombre 1")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental Hombre 1:", f_fundamental)
print("Frecuencia media Hombre 1:", f_media)
print("Brillo señal Hombre 1:", brillo)
print("Intensidad señal Hombre 1:",intensidad)
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre -2.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Hombre 2")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental Hombre 2:", f_fundamental)
print("Frecuencia media Hombre 2:", f_media)
print("Brillo señal Hombre 2:", brillo)
print("Intensidad señal Hombre 2:",intensidad)
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre_3.wav')
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Graficar señal
plt.figure(figsize=(12, 4))
plt.plot(t, data, color='blue')
plt.title("Hombre 3")
plt.xlabel("Tiempo [s]")
plt.grid(True)
plt.show()
#Calculo transformada de Fourier
F = fft(data)
X = fftfreq(len(data), 1/fs)
#Calculo de magnitud frecuencial
F_mag = np.abs(F)
# Graficar transformada y densidad espectral de potencia
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(F_mag, color='red')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia")
#Calculo de frecuencia fundamental
pico= np.argmax(np.abs(F[1:len(data)//2])) + 1
f_fundamental = X[pico]
#Calculo frecuencia media
f_media = np.sum(X * F_mag) / np.sum(F_mag)
#Calculo del brillo
umbral = 1500  #Energia por encima de 1500 Hz
idx_umbral = np.where(X >= umbral)[0]
e_total = np.sum(F_mag**2)
e_alta = np.sum(F_mag[idx_umbral]**2)
brillo = e_alta / e_total
#Calculo de la Intensidad
intensidad = np.sum(data**2)
print("Frecuencia fundamental Hombre 3:", f_fundamental)
print("Frecuencia media Hombre 3:", f_media)
print("Brillo señal Hombre 3:", brillo)
print("Intensidad señal Hombre 3:",intensidad)
