import numpy as np

fs = 44100 # frequência de amostragem

def fourierFunc(recording):
    try: 
        N = len(recording)
        T = 1/fs #Período de amostragem
        freq = np.fft.fftfreq(N, T)[:N//2]  #indices das frequencias de fourier 
        window = np.hanning(N) #window pra evitar vazamento espectral
        mag = np.abs(np.fft.fft(recording.flatten() * window))[:N//2] #magnitudes das transformadas de fourier

        ##limitar as frequencias entre 20 e 20khz, pois são as únicas úteis para som
        mask = (freq >= 20) & (freq <= 20000)
        freqFiltered = freq[mask]
        magFiltered = mag[mask]

        domFreqIndex = np.argmax(magFiltered) #Pega o index da magnitude máxima
        finalFreq = freqFiltered[domFreqIndex]  #A frequencia maxima do intervalo gravado 

        return finalFreq 

    except Exception as e:
        print("Erro na função fourier:", e)