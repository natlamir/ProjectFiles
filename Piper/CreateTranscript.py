import os
import whisper

# Load the whisper model
model = whisper.load_model("base")

# Get the list of WAV files in the current directory
wav_files = [file for file in os.listdir() if file.endswith(".wav")]

# Sort the WAV files in numeric order
wav_files = sorted(wav_files, key=lambda x: int(os.path.splitext(x)[0]))

# Dictionary to store transcripts and their corresponding files
transcript_dict = {}

# Open a text file for writing the transcripts
with open("transcript.csv", "w") as transcript_file:
    # Iterate through each WAV file
    for wav_file in wav_files:
        print(f"Transcribing {wav_file}")
        
        # Transcribe the current WAV file
        result = model.transcribe(wav_file)
        
        # Remove leading and trailing spaces from the transcribed text
        transcribed_text = result['text'].strip()
        
        # Check if this transcript already exists
        if transcribed_text in transcript_dict:
            print(f"Duplicate transcript found:")
            print(f"Current file: {wav_file}")
            print(f"Duplicate of: {transcript_dict[transcribed_text]}")
            print(f"Transcript: {transcribed_text}")
            print("---")
        else:
            # Add the transcript to the dictionary
            transcript_dict[transcribed_text] = wav_file
        
        # Write the result to the transcript file without space after '|'
        transcript_file.write(f"{wav_file}|{transcribed_text}\n")

print("Transcription complete. Check 'transcript.csv' for results.")
