import pydub
from scipy.io import wavfile
import numpy as np

# Define a dictionary to map morse code to letters
MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
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
                   '-.--.': '(', '-.--.-': ')'}


# Function to decrypt morse code
def decrypt(cipher):
    message = ""
    morse_code = ""
    for char in cipher:
        if (char == '.') or (char == '-'):
            morse_code += char
        elif char == ' ':
            message += MORSE_CODE_DICT[morse_code]
            morse_code = ""
    return message


# Function to decode morse audio and return the decoded message
def morse_audio_decoder(audio_file):
    # Read the audio file using pydub
    audio = pydub.AudioSegment.from_file(audio_file)
    # Convert the audio data to a NumPy array
    samples = np.array(audio.get_array_of_samples())
    # Use the scipy library to perform signal processing on the audio data
    # to detect the presence of the dot and dash sounds
    rate, data = wavfile.read(audio_file)
    # Use the result of the signal processing to determine the morse code
    morse_code = ""
    for sample in data:
        if sample > 0:
            morse_code += "-"
        else:
            morse_code += "."
    return decrypt(morse_code)


print(morse_audio_decoder("morse_voice/in_morse.wav"))
