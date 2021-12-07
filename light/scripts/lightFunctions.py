import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def sign(num):
    return -1 if num < 0 else 1
#2560 1440
def readIntensity(photoName, plotName, data):
    lamp, surface = data
    photo = imageio.imread(photoName)
    background = photo[510:1330, 870:1370, 0:3].swapaxes(0, 1)
    
    cut = photo[510:1330, 870:1370, 0:3].swapaxes(0, 1)
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
    cor = len(luma_mercury_big)//coef
    luma_mercury = np.array([0]*cor)

    for i in range(len(luma_mercury_big)):
        luma_mercury[i//coef] += luma_mercury_big[i]

    derivative = luma_mercury[1:] - luma_mercury[:-1]

    measured_max = []
    for i in range(1, len(derivative)):
        if (sign(derivative[i]) == sign(-derivative[i-1])) and (derivative[i] != 0 and derivative[i-1] != 0):
            measured_max.append(i)
    measured_max = np.array(measured_max)*coef
    print (measured_max)
    real_max = [404.6563, 435.8328, 546.0735, 578.2] #данные с википедии
    k = (578.2 - 404.6563)/(measured_max[4] - measured_max[0])

    print(measured_max)

    return [int(404.6563 - measured_max[0]*k), int((len(luma_mercury_big) - measured_max[0])*k + 404.6563)]

def data(names): #фуекция обработки названия файла для получения подписей графиков
    name = names.split("-")
    if (name[0] == 'blue'): surface = "синий лист"
    if (name[0] == 'green'): surface = "зеленый лист"
    if (name[0] == 'red'): surface = "красный лист"
    if (name[0] == 'white'): surface = "белый лист"
    if (name[0] == 'yellow'): surface = "желтый лист"
    if (name[1] == 'tungsten.jpg'): lamp = "лампа накаливания"
    if (name[1] == 'mercury.jpg'): lamp = "ртутная лампа"
    return [lamp, surface]

def nice(): print("Nice") #функция которая выводит Nice