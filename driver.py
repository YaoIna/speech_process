'''
driver.py
'''

import numpy

from mydsp.audioframes import AudioFrames
from mydsp.rmsstream import RMSStream
import matplotlib.pyplot as plt
import os


def driver():
    # Construct an RMS stream for the file "shaken.wav"
    # with the specified parameters.  Iterate to create a list
    # of frame intensities.  Plot them with time on the abcissa (x)
    # axis in seconds and RMS intensity on the ordinate (y) axis.

    # Be sure to listen to the audio to see if the intensity plot looks
    # correct.

    # Here's where you write lots of exciting stuff!

    # Might want to set a breakpoint here if your windows are closing on exit
    pass


len_ms = 20
adv_ms = 10
module_path = os.path.dirname(__file__)
frames = AudioFrames(module_path + '/shaken.wav', adv_ms, len_ms)
rms_stream = RMSStream(frames)
x_list = list()
for i in range(len(rms_stream)):
    if i == 0:
        x_list.append(len_ms / 1000)
    else:
        x_list.append(len_ms / 1000 + i * (len_ms - adv_ms) / 1000)
x_array = numpy.array(x_list)

plt.figure()
plt.plot(x_array, rms_stream.rms_data)
plt.title('Relative Intensity')
plt.xlabel('time(s)')
plt.ylabel('dB rel.')
plt.show()

if __name__ == '__main__':
    # If invoked as the main module, e.g. python driver.py, execute
    driver()
