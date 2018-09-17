import matplotlib.pyplot as plt
import numpy
import scipy

N = 600
T = 1.0 / 800
x = numpy.linspace(0.0, N * T, N)
a = numpy.sin(50.0 * 2.0 * numpy.pi * x)
b = 0.5 * numpy.sin(80.0 * 2 * numpy.pi * x)
y = a + b
yf = scipy.fft(y)
print(len(yf))
Y = 2.0 / N * numpy.abs(yf[0:int(N / 2)])
X = numpy.linspace(0.0, 1.0 / (2.0 * T), int(N / 2))
plt.plot(X, Y)
plt.grid()
plt.show()
