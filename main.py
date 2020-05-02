import youtube_dl
import ffmpeg
import os

print("##########################################################################################")
print("#     SplitterUI 0.0.1  Made by VectorKappa 9F2B6C24AA8181320B10ED44F72AFA3FFE28AB5C     #")
print("##########################################################################################\n\n")

SourceSelect = input("Choose source:\n 1)Local File\n 2)URL\n")
if SourceSelect == "1":
    InputFilePath = input("Input direct path to file:\n\n").strip("\"")
    ffmpeg.run(ffmpeg.output(ffmpeg.input(InputFilePath), f'{os.path.splitext(os.path.basename(InputFilePath))[0]}.wav'))
    FileToSplit = os.path.abspath(f'{os.path.splitext(os.path.basename(InputFilePath))[0]}.wav')
elif SourceSelect == "2":
    InputFileURL = input("Enter a valid file URL:\n\n")
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': '%(title)s.%(ext)s', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', }], }) as ydl:
        FileToSplit = os.path.abspath(f"{ydl.extract_info(InputFileURL)['title']}.wav")
else:
    print("Enter '1' or '2'!\n\n")
    quit()