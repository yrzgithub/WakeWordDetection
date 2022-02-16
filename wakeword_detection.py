import struct
import time

import pyaudio
import pvporcupine
import os

wake_word_path = r"D:\pythonProject2\known\wake words"
audio = pyaudio.PyAudio()
key_words_paths = []
assistant_names = []
for word in os.listdir(wake_word_path):
    print(word)
    key_words_paths.append(os.path.join(wake_word_path, word))
    assistant_names.append(word)

print('\n\n\n\n')

sensitivies = [0.7 for i in key_words_paths]
wake_up = pvporcupine.create(keyword_paths=key_words_paths, sensitivities=sensitivies)
wake_mic = audio.open(frames_per_buffer=wake_up.frame_length, channels=1, rate=wake_up.sample_rate, input=True,
                      format=pyaudio.paInt16)

while 1:
    pcm = wake_mic.read(wake_up.frame_length)
    pcm = struct.unpack("h" * wake_up.frame_length, pcm)
    index = wake_up.process(pcm=pcm)  # pcm audio sample
    if index == -1:
        continue
    print(assistant_names[index])
    time.sleep(1)