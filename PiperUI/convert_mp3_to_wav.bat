@echo off
setlocal enabledelayedexpansion

set "input_folder=%CD%"

:: Check if ffmpeg is available in the system path
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: ffmpeg not found in the system path.
    exit /b 1
)

:: Iterate through each MP3 file in the current folder
for %%F in ("%input_folder%\*.mp3") do (
    set /a count+=1
    set "output_file=!count!.wav"

    :: Execute ffmpeg command for each MP3 file
    ffmpeg -i "%%F" -acodec pcm_s16le -ar 22050 "!output_file!"
)

echo Conversion completed.
exit /b 0
