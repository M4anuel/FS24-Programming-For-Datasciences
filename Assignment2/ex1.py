# Import dependencies
import time
import matplotlib.pyplot as plt
import sounddevice as sd 
from scipy.io.wavfile import read
fs_bird,sound_bird=read('./data/bird.wav')
fs_leaves,sound_leaves=read('./data/leaves.wav')
# Plot sounds in different subplots
plt.figure(figsize=(16,6))
plt.subplot(1,2,1)
plt.plot(sound_bird)
plt.title("Bird sound")
plt.subplot(1,2,2)
plt.plot(sound_leaves)
plt.title("Leaves sound")
plt.show()
# Play sounds
time.sleep(1)
sd.play(sound_bird,fs_bird)
time.sleep(1)
sd.play(sound_leaves,fs_leaves)
time.sleep(1)