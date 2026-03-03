import sounddevice as sd
import numpy as np
import sys
import time

import matplotlib.pyplot as plt
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation

from fourier import fourierFunc
from painting import paintingFunc

fs = 44100 # frequência de amostragem
##duration = 0.4  # segundos
blocksize = 8192
volume = 0
color = [0, 0, 0]
try:
    def callback(indata, frames, time, status):
        global volume
        global color
        audio = indata[:, 0]

        volume = np.sqrt(np.mean(audio**2))
        if volume < 0.01:
            return  #se o som for pouco volumoso, não processa
        
        musicNote = fourierFunc(audio)
        print(musicNote)
        color = paintingFunc(musicNote)
        print(color)
        print(volume)

    with sd.InputStream(
        samplerate=fs,
        channels=1,
        blocksize=blocksize,
        callback=callback
    ):
        while True:

            time.sleep(0.1)
            plt.style.use('fivethirtyeight')

            x_vals = []
            y_vals = []
            fig, ax = plt.subplots()
            index = count()

            def animate(i):
                x_vals.append(next(index))
                y_vals.append(volume)

                #plt.plot(x_vals, y_vals, color = color)
                if len(x_vals) > 1:
                    ax.plot(x_vals[-2:], y_vals[-2:], color=color)

            ani = FuncAnimation(plt.gcf(), animate, interval=50)

            plt.tight_layout()
            plt.show()

            pass

except KeyboardInterrupt:
    try:
        sys.exit(0)
    except Exception as e:
        print("Erro:", e)