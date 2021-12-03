import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def sign(num):
    return -1 if num < 0 else 1

def readIntensity(photoName, plotName, data):
    lamp, surface = data
    photo = imageio.imread(photoName)
    background = photo[480:1030, 1130:1385, 0:3].swapaxes(0, 1)
    
    cut = photo[480:1030, 1170:1350, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()
    
    plt.imshow(background, origin='lower')

    plt.savefig(plotName)

    return luma

def calibration(luma_mercury_big):
    coef = 5
    cor = len(luma_mercury_big)//coef + 1
    luma_mercury = np.array([0]*cor)

    for i in range(550):
        luma_mercury[i//coef] += luma_mercury_big[i]
    derivative = luma_mercury[1:] - luma_mercury[:-1]

    measured_max = []
    for i in range(1, len(derivative)):
        if (sign(derivative[i]) == sign(-derivative[i-1])) and (derivative[i] != 0 and derivative[i-1] != 0):
            measured_max.append(i)
    measured_max = np.array(measured_max)*coef
    real_max = [404.6563, 435.8328, 546.0735, 578.2] #данные с википедии
    k = (real_max[3] - real_max[0])/(measured_max[10] - measured_max[0])
    return [int(real_max[0] - measured_max[0]*k), int((len(luma_mercury_big) - measured_max[0])*k + real_max[0])]

def nice(): print("Nice") #функция которая выводит Nice