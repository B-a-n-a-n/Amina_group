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

#--------------------------------------------------построение графиков в спокойном состоянии
print("Строим графики до физической активности")
#-----------------анализ данных из памяти
with open("rest.txt", "r") as datas:
	i = 0
	data_calm = []
	data_calm_app = []
	for el in datas.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			n = int(a[4])
		if i == 7:
			a = el.split(' ')
			period = 1/int(a[4])
		if i > 10:
			data_calm.append(int(str(el)))

summ = 0
n = 1000
data_calm_app = []
data_calm_pulse = []
for i in range(1,len(data_calm)):
	if i%n == 0:
		data_calm_app.append(summ/n)
		summ = 0
	if i > n:
		data_calm_pulse.append(data_calm[i] - data_calm_app[(i)//n-1])
	summ += data_calm[i]

pressure = np.array(data_calm)*(0.089)
time = np.linspace(0,period*(len(data_calm)), len(data_calm))
pressure_app = np.array(data_calm_pulse)*(0.089)
time_app = np.linspace(0,period*(len(data_calm_pulse)), len(data_calm_pulse))

#-------------------------------построение зависимости давления от времени
print("Строим график зависимости давления от времени")
fig2, ax2 = plt.subplots(figsize = (16,10), dpi = 300)
ax2.plot(time, pressure, alpha=0.9, label='Давление - ' + str(157) + '/'+ str(110) + ' [мм рт.ст.]', lw=0.6, c='b', mew=0.4, ms=10, mfc = 'orange', mec = 'm')
ax2.plot(10,10,'ro', ms = 100) 

#настройка осей
plt.axis([0,60,105, 157])
ax2.minorticks_on()
ax2.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax2.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей

mask = np.abs(time-3) < 0.01
plt.scatter(time[mask], pressure[mask], color='red', s=50, marker='o')
ax2.text(5, 147, 'Systole', fontsize = 14)

mask = np.abs(time-57) < 0.01
plt.scatter(time[mask], pressure[mask], color='red', s=50, marker='o')
ax2.text(53, 107, 'Diatole', fontsize = 14)

font = 8
plt.title('Артериальное давление до физической нагрузки')
plt.xlabel('Время [с]' )
plt.ylabel('Давление [мм рт. ст.]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig2.savefig("calm-pressure.png")
#plt.show()

#-------------------------------построение зависимости пульса от времени

print("Строим график зависимости пульса от времени")
fig2, ax2 = plt.subplots(figsize = (16,10), dpi = 300)
ax2.plot(time_app, pressure_app, alpha=0.9, label='Пульс - 84 уд/мин', lw=0.6, c='b', mew=0.4, ms=10, mfc = 'b', mec = 'b')

#настройка осей
plt.axis([10,30,-3, 3])
ax2.minorticks_on()
ax2.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax2.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей
font = 8
plt.title('Пульс до физической нагрузки')
plt.xlabel('Время [с]')
plt.ylabel('Изменение давления в артерии [мм рт. ст.]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig2.savefig("calm-pulse.png")
#plt.show()

#--------------------------------------------------построение графика давления от времени в напряженном состоянии
print("Строим графики после физической активности")
#-----------------анализ данных из памяти
with open("fitness.txt", "r") as datas:
	i = 0
	data_fitness = []
	for el in datas.read().split("\n"):
		i+=1
		if i == 8:
			a = el.split(' ')
			n = int(a[4])
		if i == 7:
			a = el.split(' ')
			period = 1/int(a[4])
		if i > 10:
			data_fitness.append(int(str(el)))

summ = 0
n = 1000
data_fitness_app = []
data_fitness_pulse = []
for i in range(1,len(data_fitness)):
	if i%n == 0:
		data_fitness_app.append(summ/n)
		summ = 0
	if i > n:
		data_fitness_pulse.append(data_fitness[i] - data_fitness_app[(i)//n-1])
	summ += data_fitness[i]

pressure = np.array(data_fitness)*(0.089)
time = np.linspace(0,period*(len(data_fitness)), len(data_fitness))
pressure_app = np.array(data_fitness_pulse)*(0.089)
time_app = np.linspace(0,period*(len(data_fitness_pulse)), len(data_fitness_pulse))

#-------------------------------построение зависимости давления от времени
print("Строим график зависимости давления от времени")
fig3, ax3 = plt.subplots(figsize = (16,10), dpi = 300)
ax3.plot(time, pressure, alpha=0.9, label='Давление - ' + str(150) + '/'+ str(101) + ' [мм рт.ст.]', lw=0.6, c='orange', mew=0.4, ms=10, mfc = 'orange', mec = 'orange')

#настройка осей
plt.axis([0,58,95, 170])
ax3.minorticks_on()
ax3.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax3.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей

mask = np.abs(time-6) < 0.01
plt.scatter(time[mask], pressure[mask], color='red', s=50, marker='o')
ax3.text(6.1, 153, 'Systole', fontsize = 14)

mask = np.abs(time-57) < 0.01
plt.scatter(time[mask], pressure[mask], color='red', s=50, marker='o')
ax3.text(54, 106, 'Diatole', fontsize = 14)

font = 8
plt.title('Артериальное давление после физической нагрузки')
plt.xlabel('Время [с]')
plt.ylabel('Давление [мм рт. ст.]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig3.savefig("fitness-pressure.png")
#plt.show()

#-------------------------------построение зависимости пульса от времени

print("Строим график зависимости пульса от времени")
fig2, ax2 = plt.subplots(figsize = (16,10), dpi = 300)
ax2.plot(time_app, pressure_app, alpha=0.9, label='Пульс - 90 уд/мин', lw=0.6, c='orange', mew=0.4, ms=10, mfc = 'orange', mec = 'orange')

#настройка осей
plt.axis([10,30,-3, 3])
ax2.minorticks_on()
ax2.grid(which='major', color = 'k', linewidth = 2, alpha = 0.3)
ax2.grid(which='minor', color = 'k', linestyle = '--', alpha = 0.1)
#настройка подписей

font = 8
plt.title('Пульс после физической нагрузки')
plt.xlabel('Время [с]')
plt.ylabel('Изменение давления в артерии [мм рт. ст.]')
plt.legend()
#сохранение графика в формате svg
print("Сохраняем график")
fig2.savefig("fitness-pulse.png")
#plt.show()