import os
import argparse
from pydub import AudioSegment

# create argument parser
parser = argparse.ArgumentParser(description='Convert MP3 files to WAV files.')
parser.add_argument('input_folder', type=str, help='Path to input MP3 files folder.')
parser.add_argument('output_folder', type=str, help='Path to output WAV files folder.')
args = parser.parse_args()

# create output folder if it does not exist
if not os.path.exists(args.output_folder):
    os.makedirs(args.output_folder)

# iterate through files in input folder
for filename in os.listdir(args.input_folder):
    if filename.endswith('.mp3'):
        # load MP3 file and export as WAV file
        mp3_file = AudioSegment.from_file(os.path.join(args.input_folder, filename), format='mp3')
        wav_file = os.path.splitext(filename)[0] + '.wav'
        wav_path = os.path.join(args.output_folder, wav_file)
        mp3_file.export(wav_path, format='wav')