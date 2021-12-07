import lightFunctions as func
from matplotlib import pyplot as plt
import numpy as np

def graph(lumas, label, x1, x2, name, y_label):
	fig, ax = plt.subplots(figsize=(11, 9), dpi=60)
	colors = ['b','g','r','w','y']
	lengh = np.linspace(x1, x2, len(lumas[5]))
	for i in range(5):
		plt.plot(lengh, lumas[i], lw=1.9, c=colors[i], mew=0.4, ms=0, mec = 'b')

	plt.minorticks_on()
	plt.grid(which='major', linewidth = 0.5, color = 'k')
	plt.grid(which='minor', linestyle = '-')
	ax.set_facecolor((0.85, 0.85, 0.85))

	plt.axis([x1 - 5,x2 - 55,0,max(lumas[3])*1.05])
	plt.legend(["синий лист", "зеленый лист", "красный лист", "белый лист", "желтый лист"])
	plt.title(label, fontsize = 13)   
	plt.ylabel(y_label, fontsize = 13)   
	plt.xlabel('Длинна волны [нм]', fontsize = 13)   
	plt.savefig(name)

pics = ["blue-tungsten.jpg", "green-tungsten.jpg", "red-tungsten.jpg","white-tungsten.jpg", "yellow-tungsten.jpg", "white-mercury.jpg"]

print("Считыываем данные и строим графики интенсивности отраженного излучения")
lumas = []
for name in pics:
	luma = func.readIntensity(name, name.split(".")[0]+"-plot.jpeg", func.data(name))
	lumas.append(luma)
lumas = np.array(lumas)
x1, x2 = func.calibration(lumas[5])
lumas[3] += 0.7

# строим график зависимости
graph(lumas, "Отраженная интенсивность\n излучения лампы накаливания", x1, x2, "intensites.png", 'Яркость')
graph(lumas/lumas[3], "Альбедо поверхностей", x1, x2, "albedos.png", 'Альбедо')