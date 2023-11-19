import os
import whisper

# Load the whisper model
model = whisper.load_model("base")

# Get the list of WAV files in the current directory
wav_files = [file for file in os.listdir() if file.endswith(".wav")]

# Sort the WAV files in numeric order
wav_files = sorted(wav_files, key=lambda x: int(os.path.splitext(x)[0]))

# Open a text file for writing the transcripts
with open("transcript.txt", "w") as transcript_file:
    # Iterate through each WAV file
    for wav_file in wav_files:
        print(wav_file)
        # Transcribe the current WAV file
        result = model.transcribe(wav_file)

        # Remove leading and trailing spaces from the transcribed text
        transcribed_text = result['text'].strip()

        # Write the result to the transcript file without space after '|'
        transcript_file.write(f"wavs/{wav_file}|{transcribed_text}\n")

print("Transcription complete. Check 'transcript.txt' for results.")
