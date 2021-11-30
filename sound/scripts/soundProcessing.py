import numpy as np
import matplotlib.pyplot as plt

data = open(r"C:\Users\Keys\Desktop\sound\data\conditions.txt", "r")
spisoc = data.read().split(" ")
T = float(spisoc[6]) + 273.15 # температура воздуха
Vlag = float(spisoc[3]) # влажность воздуха
R  = 8.314 # постоянная газовая

print("Введите относительный объём углекислого газа в процентах (от 0.03 процента до 5)")
Procmin = (float(input()) / 100) # относительный объём углексислого газа
e = 2.7182818284 ** (0.0387 * (T - 273.15)) # нахождение аргумента экспоненциальной функции
PlVod = e * 1.1742 * Vlag # абсолютная плотность воды
PlVoz = 1195 # абсолютная плотность воздуха
PlCO2 = 1700 # абсолютная плотность углекислого газа
Proc1 = 0.01 # абсолютная влажность
Procvoz = 1 - Proc1 - Procmin # относительный объём воздуха

μ = (((Procvoz * 28.97) + (Proc1 * 18.01) + (Procmin * 44.01))) # моллекулярная масса
γ = (((28.97 * 1.0036 * Procvoz) + (18.01 * 1.863 * Proc1) + (44.01 * Procmin)) / ((28.97 * 0.7166 * Procvoz) + (18.01 * 1.403 * Proc1) + (44.01 * 0.649 * Procmin)) * 1000)
a = float(γ) * float(R) * float(T) / float(μ)
b = a ** (0.5)
print("Скорость звука составляет:", b, " м/c")

Procminl = (0 / 100) # относительный объём углексислого газа
e = 2.7182818284 ** (0.0387 * (T - 273.15)) # нахождение аргумента экспоненциальной функции
PlVod = e * 1.1742 * Vlag # абсолютная плотность воды
PlVoz = 1195 # абсолютная плотность воздуха
PlCO2 = 1700 # абсолютная плотность углекислого газа
Proc1 = 0.01 # абсолютная влажность
Procvoz = 1 - Proc1 - Procminl # относительный объём воздуха

μ1 = (((Procvoz * 28.97) + (Proc1 * 18.01) + (Procminl * 44.01))) # моллекулярная масса
γ1 = (((28.97 * 1.0028 * Procvoz) + (18.01 * 1.863 * Proc1) + (44.01 * Procminl)) / ((28.97 * 0.7166 * Procvoz) + (18.01 * 1.403 * Proc1) + (44.01 * 0.649 * Procminl)) * 1000)
a1 = float(γ1) * float(R) * float(T) / float(μ1)
b1 = a1 ** (0.5)

Procmins = (5 / 100) # относительный объём углексислого газа
e = 2.7182818284 ** (0.0387 * (T - 273.15)) # нахождение аргумента экспоненциальной функции
PlVod = e * 1.1742 * Vlag # абсолютная плотность воды
PlVoz = 1195 # абсолютная плотность воздуха
PlCO2 = 1700 # абсолютная плотность углекислого газа
Proc1 = 0.01 # абсолютная влажность
Procvoz = 1 - Proc1 - Procmins # относительный объём воздуха

μ2 = (((Procvoz * 28.97) + (Proc1 * 18.01) + (Procmins * 44.01))) # моллекулярная масса
γ2 = (((28.97 * 1.0028 * Procvoz) + (18.01 * 1.863 * Proc1) + (44.01 * Procmins)) / ((28.97 * 0.7166 * Procvoz) + (18.01 * 1.403 * Proc1) + (44.01 * 0.649 * Procmins)) * 1000)
a2 = float(γ2) * float(R) * float(T) / float(μ2)
b2 = a2 ** (0.5)
print('Коэффициент k:', (b2 - b1) / (Procmins * 100 - Procminl * 100), ' Коэффициент b:', b1)


from matplotlib import pyplot as plt   
   
x = [Procminl*100,Procmins*100]   
y = [b1,b2]   
fig, ax = plt.subplots(figsize=(13, 10), dpi=75)
plt.plot(x,y, 'o-r', alpha=0.7, label="first", lw=1, mec='b', mew=1, ms=1)
ax.scatter(0.205, 344.64, color='blue', marker='+', s=150, linewidth=2)
ax.scatter(3.344, 342.6, color='green', marker='+', s=150, linewidth=2)
plt.minorticks_on()
plt.grid(which='major', linewidth = 0.5, color = 'k')
plt.grid(which='minor', linestyle = ':')
plt.axis([Procminl*100,Procmins*100,b2 - 0.1,b1 + 0.1])
plt.legend(['Линейная зависимость', 'Вдох: скорость воздуха - 344.64 [m/c], концентрация CO2 - 0.205 процента', 'Выдох: скорость воздуха - 342.61 [m/c], конценртация CO2 - 3.344 процента'])
plt.title("Зависимость скорости звуки от концентрация углекислого газа", fontsize = 13)   
plt.ylabel('Скорость звука, [м/c]', fontsize = 13)   
plt.xlabel('Концентрация CO2, [%]', fontsize = 13)   
plt.show()
