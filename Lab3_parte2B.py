import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks

fs = 44000

#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer-1.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Mujer 1:", jitter_abs)
print("Jitter relativo Mujer 1:", jitter_rel, "%")
print("Shimmer absoluto Mujer 1:", shimmer_abs)
print("Shimmer relativo Mujer 1:", shimmer_rel, "%")
print("*")
print("*")


#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer -2.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Mujer 2:", jitter_abs)
print("Jitter relativo Mujer 2:", jitter_rel, "%")
print("Shimmer absoluto Mujer 2:", shimmer_abs)
print("Shimmer relativo Mujer 2:", shimmer_rel, "%")
print("*")
print("*")

fs, data = wavfile.read(r'C:\Users\danil\Downloads\Mujer -3.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Mujer 3:", jitter_abs)
print("Jitter relativo Mujer 3:", jitter_rel, "%")
print("Shimmer absoluto Mujer 3:", shimmer_abs)
print("Shimmer relativo Mujer 3:", shimmer_rel, "%")
print("*")
print("*")

#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre_1.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Hombre 1:", jitter_abs)
print("Jitter relativo Homre 1:", jitter_rel, "%")
print("Shimmer absoluto Hombre 1:", shimmer_abs)
print("Shimmer relativo Hombre 1:", shimmer_rel, "%")
print("*")
print("*")

#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre -2.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Hombre 2:", jitter_abs)
print("Jitter relativo Hombre 2:", jitter_rel, "%")
print("Shimmer absoluto Hombre 2:", shimmer_abs)
print("Shimmer relativo Hombre 2:", shimmer_rel, "%")
print("*")
print("*")

#Cargar archivo WAV
fs, data = wavfile.read(r'C:\Users\danil\Downloads\Hombre_3.wav')
x = data.astype(float)
# Crear vector de tiempo
t = np.linspace(0, len(data) / fs, num=len(data))
#Detección de los periodos de vibración
zero_crossings = np.where(np.diff(np.sign(x)) > 0)[0]
Ti = np.diff(zero_crossings) / fs

#Calculo Jitter absoluto
jitter_abs = np.mean(np.abs(np.diff(Ti)))
#Calculo Jitter relativo
jitter_rel = (jitter_abs / np.mean(Ti)) * 100
#Detección de amplitudes
pico, _ = find_peaks(x, height=0)
Ai = x[pico]    

#Calculo Shimmer absoluto
shimmer_abs = np.mean(np.abs(np.diff(Ai)))
#Calculo Shimmer relativo
shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

print("Jitter absoluto Hombre 3:", jitter_abs)
print("Jitter relativo Hombre 3:", jitter_rel, "%")
print("Shimmer absoluto Hombre 3:", shimmer_abs)
print("Shimmer relativo Hombre 3:", shimmer_rel, "%")
print("*")
print("*")


