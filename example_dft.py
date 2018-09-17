import numpy
import matplotlib.pyplot as plt

frame_s = 20 / 1000
Fs = 8000
frame_N = int(numpy.round(Fs * frame_s))
time_idx = numpy.arange(frame_N) / Fs
omega = numpy.array([1000, 2000, 2500])
amplitudes = numpy.array([1, .5, .25])
x = numpy.zeros(frame_N)
for idx in range(len(omega)):
    x += (amplitudes[idx] * numpy.sin(2 * numpy.pi * omega[idx] * time_idx[idx]))

# plt.figure()
# plt.plot(time_idx, x)
# plt.title('Signal')
# plt.xlabel('Time(s)')
# plt.ylabel('Pressure(counts)')
# plt.show()

bins_HZ = numpy.arange(frame_N) / frame_N * Fs
window = numpy.hamming(frame_N)
windowed_x = x * window
d_x = numpy.fft.fft(windowed_x)
magX = numpy.abs(d_x)
mag_dB = 20 * numpy.log10(magX)

plt.figure()
plt.plot(bins_HZ, mag_dB)
plt.title('Discrete Fourier Transform')
plt.xlabel('Hz')
plt.ylabel('dB rel.')
plt.show()
