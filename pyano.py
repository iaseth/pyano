import random
import tkinter as tk

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100
DURATION = 0.40


def synth(frequency, duration=DURATION, sampling_rate=SAMPLE_RATE):
    frames = int(duration * sampling_rate)
    arr = np.cos(2*np.pi*frequency*np.linspace(0, duration, frames))
    arr = arr + np.cos(4*np.pi*frequency*np.linspace(0, duration, frames))
    arr = arr - np.cos(6*np.pi*frequency*np.linspace(0, duration, frames))
    arr = arr / max(np.abs(arr))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    return sound


def get_piano_sounds():
    sounds = []
    freq = 16.3516
    for idx in range(108):
        mod = int(idx/36)
        sound = synth(freq)
        sounds.append({
            "idx": idx,
            "frequency": freq,
            "sound": sound
        })
        freq = freq * 2 ** (1/12)

    return sounds


def play_random_sounds():
    for i in range(50):
        key = random.randint(48, 60)
        sound = piano_sounds[key]
        print(f"[{i+1}] Playing #{key} at {sound['frequency']:.2f}Hz")
        sd.play(sound["sound"], SAMPLE_RATE, blocking=True)


def piano_gui():
    window = tk.Tk()
    window.mainloop()


piano_sounds = get_piano_sounds()
piano_gui()
