from playsound import playsound
from pydub import AudioSegment
from time import sleep
import wave
import numpy as np
import matplotlib.pyplot as plt

LAT_MORSE = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ', ': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}

MORSE_LAT = {'.-': 'A', '-...': 'B',
             '-.-.': 'C', '-..': 'D', '.': 'E',
             '..-.': 'F', '--.': 'G', '....': 'H',
             '..': 'I', '.---': 'J', '-.-': 'K',
             '.-..': 'L', '--': 'M', '-.': 'N',
             '---': 'O', '.--.': 'P', '--.-': 'Q',
             '.-.': 'R', '...': 'S', '-': 'T',
             '..-': 'U', '...-': 'V', '.--': 'W',
             '-..-': 'X', '-.--': 'Y', '--..': 'Z',
             '.----': '1', '..---': '2', '...--': '3',
             '....-': '4', '.....': '5', '-....': '6',
             '--...': '7', '---..': '8', '----.': '9',
             '-----': '0', '--..--': ', ', '.-.-.-': '.',
             '..--..': '?', '-..-.': '/', '-....-': '-',
             '-.--.': '(', '-.--.-': ')'
             }

short = AudioSegment.from_wav("morse_voice/short.wav")
long = AudioSegment.from_wav("morse_voice/long.wav")
pause_between_symbols = AudioSegment.from_wav("morse_voice/pause_between_symbols.wav")
pause_between_letters = AudioSegment.from_wav("morse_voice/pause_between_letters.wav")
pause_between_words = AudioSegment.from_wav("morse_voice/pause_between_words.wav")


def to_morse(latin: str):
    words = latin.upper().split()
    res = ""

    for word in words:
        for letter in word:
            res += LAT_MORSE[letter] + " "
        res += "| "

    res = res[:-2]
    return res


def to_latin(morse: str):
    symbols = morse.split()
    res = ""

    for symbol in symbols:
        if symbol != "|":
            res += MORSE_LAT[symbol]
        else:
            res += " "

    return res


def decode_morse(audio_file):
    # Open audio file and read the data
    with wave.open(audio_file, 'r') as file:
        data = file.readframes(-1)
        data = np.fromstring(data, dtype=np.int16)
        # Plot the audio data
        plt.plot(data)
        plt.show()

    # Define threshold for detecting a beep
    threshold = np.mean(data)

    # Define parameters for dot and dash
    # dot_duration = 0.05  # in seconds
    # dash_duration = 0.3  # in seconds
    dot = 5000
    dash = 10000
    short_pause = 10000
    long_pause = 50000

    # Define parameters for space between characters and words
    char_space = 0.5  # in seconds
    word_space = 1  # in seconds
    # Decode the audio data
    isCandle = False
    morse = ''
    length_of_candle = 0
    pause = 0
    for sample in data:
        if sample != 0:
            if pause > long_pause:
                morse += " | "
            if pause > short_pause:
                morse += " "
            pause = 0
            length_of_candle += 1
        else:
            if length_of_candle > dash:
                morse += "-"
            elif length_of_candle > dot:
                morse += "."
            length_of_candle = 0
            pause += 1

    return morse


def morse_sound(morse: str):
    symbols = morse.split()
    voice = 0

    for letter in symbols:
        for symbol in letter:
            if symbol == "|":
                voice += pause_between_words
                break
            if symbol == ".":
                voice += short
            if symbol == "-":
                voice += long
            voice += pause_between_symbols

        voice += pause_between_letters

    voice.export("morse_voice/in_morse.wav", format="wav")
