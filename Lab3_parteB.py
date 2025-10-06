import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, filtfilt, freqz

fs = 44000

#Calculo filtro pasa banda mujer 1
def filtro_pasabanda1(filepath, sexo='mujer'):
    fs, x = wavfile.read(filepath)
    # Convertir a flotante
    x = x.astype(float)
    
    f_low, f_high = 150, 500
        
    f_low = 150
    f_high = 500
    nyquist = fs / 2
    low = f_low / nyquist
    high = f_high / nyquist
    # Filtro FIR pasa banda
    coef = firwin(100, [low, high], pass_zero=False)
    # Aplicar el filtro
    filtro = filtfilt(coef, [1.0], x)

    # 1. Respuesta en frecuencia del filtro
    w, h = freqz(coef, worN=8000)
    plt.figure(figsize=(10, 4))
    plt.plot((w/np.pi)*nyquist, 20 * np.log10(abs(h)))
    plt.title('Respuesta en Frecuencia del Filtro Pasa Banda FIR Mujer 1')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.grid(True)
    plt.show()
    
    t = np.arange(len(x)) / fs
    plt.figure(figsize=(10, 4))
    plt.plot(t, x)
    plt.title('Señal original')
    plt.xlabel('Tiempo [s]')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.plot(t, filtro, color = 'red')
    plt.title('Señal filtrada')
    plt.xlabel('Tiempo [s]')
    plt.legend()
    plt.grid(True)
    plt.show()

    return fs, x, filtro, coef

fs, x, filtro, coef = filtro_pasabanda1(r'C:\Users\danil\Downloads\Mujer-1.wav', sexo = 'mujer')

#Calculo filtro pasa banda Hombre 1
def filtro_pasabanda2(filepath, sexo='hombre'):
    fs, x = wavfile.read(filepath)
    # Convertir a flotante
    x = x.astype(float)
    f_low, f_high = 80, 400
        
    f_low = 150
    f_high = 500
    nyquist = fs / 2
    low = f_low / nyquist
    high = f_high / nyquist
    # Filtro FIR pasa banda
    coef = firwin(100, [low, high], pass_zero=False)
    # Aplicar el filtro
    filtro = filtfilt(coef, [1.0], x)

    # 1. Respuesta en frecuencia del filtro
    w, h = freqz(coef, worN=8000)
    plt.figure(figsize=(10, 4))
    plt.plot((w/np.pi)*nyquist, 20 * np.log10(abs(h)))
    plt.title('Respuesta en Frecuencia del Filtro Pasa Banda FIR Hombre 1')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.grid(True)
    plt.show()
    
    t = np.arange(len(x)) / fs
    plt.figure(figsize=(10, 4))
    plt.plot(t, x)
    plt.title('Señal original')
    plt.xlabel('Tiempo [s]')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.plot(t, filtro, color = 'red')
    plt.title('Señal filtrada')
    plt.xlabel('Tiempo [s]')
    plt.legend()
    plt.grid(True)
    plt.show()

    return fs, x, filtro, coef

fs, x, filtro, coef = filtro_pasabanda2(r'C:\Users\danil\Downloads\Mujer-1.wav', sexo = 'Hombre')

