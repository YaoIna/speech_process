import scipy.io.wavfile as wf
import numpy
import matplotlib.pyplot as plt

sample_rate, data = wf.read('./whistle.wav')
frame_N = len(data)
h_data = list()
for i in range(frame_N):
    h_data.append(data[i][0])

bins_HZ = numpy.arange(frame_N) / frame_N * sample_rate
window = numpy.hamming(frame_N)

windowed_data = h_data * window
d_data = numpy.fft.fft(windowed_data)
magX = numpy.abs(d_data)
mag_dB = 20 * numpy.log10(magX)

plt.figure()
plt.plot(bins_HZ, mag_dB)
plt.title('Discrete Fourier Transform')
plt.xlabel('Hz')
plt.ylabel('dB rel.')
plt.show()
