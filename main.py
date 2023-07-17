import os
from pydub import AudioSegment

# Define the path to the folder containing the WAV files
sound_folder = "inputSounds/"

# Create a dictionary to map each alphabet with its corresponding WAV file
sound_mapping = {}

# Iterate over the files in the sound folder
for file_name in os.listdir(sound_folder):
    if file_name.endswith(".wav"):
        alphabet = file_name[0].lower()
        sound_mapping[alphabet] = os.path.join(sound_folder, file_name)

# Get user input
sentence = input("Enter the sentence to convert to speech: ")

# Convert the sentence to lowercase
sentence = sentence.lower()

# Define the duration of the pause (in milliseconds)
pause_duration = 500  # Adjust the duration as needed

# Create a list to store the audio segments
audio_segments = []

# Load the corresponding WAV files and append to the audio segments list
for i, char in enumerate(sentence):
    if char in sound_mapping:
        sound_path = sound_mapping[char]
        sound = AudioSegment.from_wav(sound_path)
        audio_segments.append(sound)

    # Add a pause between words (except for the last character)
    if char == " " and i < len(sentence) - 1 and sentence[i+1] != " ":
        pause = AudioSegment.silent(duration=pause_duration)
        audio_segments.append(pause)

# Concatenate all audio segments
output = sum(audio_segments)

# Generate a unique output file name
output_file = "output_{}.mp3".format(sentence.replace(" ", "_"))

# Export the concatenated audio as an MP3 file
output.export(output_file, format="mp3")

