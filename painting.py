import numpy as np

def paintingFunc(frequency):
    ## 380(violeta) - 750(vermelho)nm, lambda inverso da frequencia, logo, frequencias menores -> lambdas maiores vice versa 
    try:
        y = (frequency-20)/(2000-20) #20000 muito alto, vou abaixar
        waveLengthNote = int(750 - (y*370))

        ## temos 370nm entre os extremos de cores, vamos dividir em 16 pedaços
        ## site de wavelengths to rgb https://405nm.com/wavelength-to-color/

        if waveLengthNote <= 403.125:
            color = [123, 0, 145]
        elif 403.125 < waveLengthNote <= 426.25:
            color = [120, 0, 233]
        elif 426.25 < waveLengthNote <= 449.375:
            color = [23, 0, 255]
        elif 449.375 < waveLengthNote <= 472.5:
            color = [0, 123, 255]
        elif 472.5 < waveLengthNote <= 495.625:
            color = [0, 230, 255]
        elif 495.625 < waveLengthNote <= 518.75:
            color = [0, 255, 56]
        elif 518.75 < waveLengthNote <= 541.875:
            color = [94, 255, 0]
        elif 541.875 < waveLengthNote <= 565:
            color = [173, 255, 0]
        elif 565 < waveLengthNote <= 588.125:
            color = [243, 255, 0]
        elif 588.125 < waveLengthNote <= 611.25:
            color = [255, 193, 0]
        elif 611.25 < waveLengthNote <= 634.375:
            color = [255, 111, 0]
        elif 634.375 < waveLengthNote <= 657.5: ### aparentemente daqui pra frente, é só vermelho mesmo
            color = [254, 0, 0]
        elif 657.5 < waveLengthNote <= 680.625:
            color = [233, 0, 0]
        elif 680.625 < waveLengthNote <= 703.75:
                color = [213, 0, 0]
        else:
            color = [150, 0, 0] 
                
        for i in range(len(color)):
            color[i] = color[i]/255
            
        return color
    
    except Exception as e:
        print("Erro na função painting", e)