import lightFunctions as func
from matplotlib import pyplot as plt
import numpy as np

def data(names): #фуекция обработки названия файла для получения подписей графиков
	name = names.split("-")
	if (name[0] == 'blue'): surface = "синий лист"
	if (name[0] == 'green'): surface = "зеленый лист"
	if (name[0] == 'red'): surface = "красный лист"
	if (name[0] == 'white'): surface = "белый лист"
	if (name[0] == 'yellow'): surface = "желтый лист"
	if (name[1] == 'tungsten.png'): lamp = "лампа накаливания"
	if (name[1] == 'mercury.png'): lamp = "ртутная лампа"
	return [lamp, surface]

def graph(lumas, label, x, y, name, y_label):
	fig, ax = plt.subplots(figsize=(11, 9), dpi=200)
	colors = ['b','g','r','w','y']
	lengh = np.linspace(x, y, len(lumas[5]))
	for i in range(5):
		plt.plot(lengh, lumas[i], alpha=1, label="first", lw=1.9, c=colors[i], mew=0.4, ms=0, mec = 'b')

	plt.minorticks_on()
	plt.grid(which='major', linewidth = 0.5, color = 'k')
	plt.grid(which='minor', linestyle = '-')
	ax.set_facecolor((0.85, 0.85, 0.85))

	plt.axis([x - 5,y + 5,0,max(lumas[3])*1.05])
	plt.legend(["синий лист", "зеленый лист", "красный лист", "белый лист", "желтый лист"])
	plt.title(label, fontsize = 13)   
	plt.ylabel(y_label, fontsize = 13)   
	plt.xlabel('Длинна волны [нм]', fontsize = 13)   
	plt.savefig(name)

pics = ["blue-tungsten.png", "green-tungsten.png", "red-tungsten.png","white-tungsten.png", "yellow-tungsten.png", "white-mercury.png"]

print("Считыываем данные и строим графики интенсивности отраженного излучения")
lumas = []
for name in pics:
	luma = func.readIntensity(name, name.split(".")[0]+"-plot.jpeg", data(name))
	lumas.append(luma)
lumas = np.array(lumas)
x, y = func.calibration(lumas[5])
lumas[3] += 1

# строим график зависимости
graph(lumas, "Отраженная интенсивность\n излучения лампы накаливания", x, y, "intensites.png", 'Яркость')
graph(lumas/lumas[3], "Альбедо поверхностей", x, y, "albedos.png", 'Альбедо')
