from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

with open('settings.txt') as file:
  settings=[float(i) for i in file.read().split('\n')]
#считываем показания компаратора и переводим через шаг квантования в вольты
data=numpy.loadtxt('data.txt', dtype=int) * settings[1]
#массив времен, создаваемый черед количество измерений и известный шаг по времени
data_time=numpy.array([i*settings[0] for i in range(data.size)])
#параметры фигуры
fig, ax=pyplot.subplots(figsize=(16, 10), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

# Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
# Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

# Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Процесс зарядки и разрядки конденсатора в RC цепи', 60)), loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

#подпись осей
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")

#линия с легендой
ax.plot(data_time, data, c='blue', linewidth=1, label = 'V(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'red', s=10)

# Находим индексы максимального и минимального значения
max_index = numpy.argmax(data)
min_index = numpy.argmin(data[len(data)//2:]) + len(data)//2

# Вычисляем время достижения максимального и минимального значения
time_to_max = data_time[max_index]
time_to_min = data_time[min_index]
# Добавляем надписи на график

ax.text(1.3, 0.7, 'Время зарядки=5,189', size=15, weight='roman', color='blue')
ax.text(1.3, 0.4, 'Время разрядки=6,811', size=15, weight='roman', color='red')



ax.legend(shadow = False, loc = 'right', fontsize = 15)

#сохранение
fig.savefig('graph.png')
fig.savefig('graph.svg')
