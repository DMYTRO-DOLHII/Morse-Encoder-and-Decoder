import wave
import numpy as np
import matplotlib.pyplot as plt
from morse import *


print(to_latin(decode_morse("morse_voice/in_morse.wav")))

# Morse code dictionary
# morse_code = {'A': '.-', 'B': '-...',
#               'C': '-.-.', 'D': '-..', 'E': '.',
#               'F': '..-.', 'G': '--.', 'H': '....',
#               'I': '..', 'J': '.---', 'K': '-.-',
#               'L': '.-..', 'M': '--', 'N': '-.',
#               'O': '---', 'P': '.--.', 'Q': '--.-',
#               'R': '.-.', 'S': '...', 'T': '-',
#               'U': '..-', 'V': '...-', 'W': '.--',
#               'X': '-..-', 'Y': '-.--', 'Z': '--..',
#               '1': '.----', '2': '..---', '3': '...--',
#               '4': '....-', '5': '.....', '6': '-....',
#               '7': '--...', '8': '---..', '9': '----.',
#               '0': '-----', ', ': '--..--', '.': '.-.-.-',
#               '?': '..--..', '/': '-..-.', '-': '-....-',
#               '(': '-.--.', ')': '-.--.-'}
#
#
# def decode_morse(audio_file):
#     # Open audio file and read the data
#     with wave.open(audio_file, 'r') as file:
#         data = file.readframes(-1)
#         data = np.fromstring(data, dtype=np.int16)
#         # Plot the audio data
#         plt.plot(data)
#         plt.show()
#
#     # Define threshold for detecting a beep
#     threshold = np.mean(data)
#
#     # Define parameters for dot and dash
#     # dot_duration = 0.05  # in seconds
#     # dash_duration = 0.3  # in seconds
#     dot = 5000
#     dash = 10000
#     short_pause = 10000
#     long_pause = 50000
#
#     # Define parameters for space between characters and words
#     char_space = 0.5  # in seconds
#     word_space = 1  # in seconds
#     # Decode the audio data
#     isCandle = False
#     morse = ''
#     length_of_candle = 0
#     pause = 0
#     for sample in data:
#         if sample != 0:
#             if pause > long_pause:
#                 morse += "|"
#             if pause > short_pause:
#                 morse += " "
#             pause = 0
#             length_of_candle += 1
#         else:
#             if length_of_candle > dash:
#                 morse += "-"
#             elif length_of_candle > dot:
#                 morse += "."
#             length_of_candle = 0
#             pause += 1
#
#     # Convert morse code to text
#     text = ''
#     for char in morse.split():
#         if char == ' ':
#             text += ' '
#         else:
#             for key, value in morse_code.items():
#                 if char == value:
#                     text += key
#     return text
#
#
# # Test the function
# print(decode_morse("morse_voice/in_morse.wav"))
