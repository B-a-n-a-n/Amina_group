import numpy as np
import matplotlib.pyplot as plt
import time

print("Получаем данные из файлов")
#обрабатываем данные из разных файлов
#--------------------------------------------------построение калибровочного графика
data = []
with open("40 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("80 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("120 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

with open("160 mmHg.txt", "r") as settings:
	i = 0
	sett = []
	for el in settings.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i > 10:
			sett.append(str(el))
summ = 0
for i in range(n):
	summ += int(sett[i])
data.append(summ/n)

real_data = [40,80,120,160]
p = 0
for i in range(4):
    p += real_data[i] / data[i]
p = int(1000*(p/4))/1000
# построение графика
print("Строим график")
fig1, ax1 = plt.subplots(figsize = (16,10), dpi = 300)
ax1.plot(real_data, data, alpha=0.9, label= ("P = " + str(p) + " * (N-10)[Па]"), lw=0.6, c='b', mew=0.4, ms=10, marker = ".", markevery = 100, mfc = 'b', mec = 'b')

#настройка осей
plt.axis([35,165,400, 1800])
ax1.minorticks_on()
ax1.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax1.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей
font = 8
plt.title('Калибровачный график зависимости показаний АЦП от давления')
plt.xlabel('Давление [Па]')
plt.ylabel('Отсчеты АЦП')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig1.savefig("pressure-calibration.png")
#plt.show()

#--------------------------------------------------построение графика давления от времени в спокойном состоянии

with open("rest.txt", "r") as datas:
	i = 0
	data_calm = []
	for el in datas.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i == 7:
			a = el.split(' ')
			print(a)
			period = 1/int(a[4])
		if i > 10:
			data_calm.append(int(str(el)))

pressure = np.array(data_calm)*(0.089)
time = np.linspace(0,period*(len(data_calm)), len(data_calm)) - 1

print(pressure)
# построение графика
print("Строим график")
fig2, ax2 = plt.subplots(figsize = (16,10), dpi = 300)
ax2.plot(time, pressure, alpha=0.9, label='Давление - ' + str(145) + '/'+ str(78) + ' [мм рт.ст.]', lw=0.6, c='b', mew=0.4, ms=10, mfc = 'b', mec = 'b')

#настройка осей
plt.axis([0,60,40, 190])
ax2.minorticks_on()
ax2.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax2.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей
font = 8
plt.title('Артериальное давлдение до физической нагрузки')
plt.xlabel('Давление [мм рт. ст.]')
plt.ylabel('Время [с]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig2.savefig("calm-pressure.png")
#plt.show()


#--------------------------------------------------построение графика давления от времени в спокойном состоянии

with open("fitness.txt", "r") as datas:
	i = 0
	data_fitness = []
	for el in datas.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			print(a)
			n = int(a[4])
		if i == 7:
			a = el.split(' ')
			print(a)
			period = 1/int(a[4])
		if i > 10:
			data_calm.append(int(str(el)))

pressure = np.array(data_calm)*(0.089)
time = np.linspace(0,period*(len(data_calm)), len(data_calm)) - 1

print(pressure)
# построение графика
print("Строим график")
fig3, ax3 = plt.subplots(figsize = (16,10), dpi = 300)
ax3.plot(time, pressure, alpha=0.9, label='Давление - ' + str(145) + '/'+ str(78) + ' [мм рт.ст.]', lw=0.6, c='b', mew=0.4, ms=10, mfc = 'b', mec = 'b')

#настройка осей
plt.axis([0,58,40, 190])
ax3.minorticks_on()
ax3.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax3.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей
font = 8
plt.title('Артериальное давлдение до физической нагрузки')
plt.xlabel('Давление [мм рт. ст.]')
plt.ylabel('Время [с]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig3.savefig("fitness-pressure.png")
#plt.show()
