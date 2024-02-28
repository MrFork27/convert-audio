import moviepy.editor as mp

name = "./media/audio-video.mp4"

try:
  # Load .mp4 file
  clip = mp.VideoFileClip(name)
except Exception as error:
  print('Error load .mp4 file')
  print(error)

try:
  # Write audio in .mp3 file
  clip.audio.write_audiofile("audio.mp3")
except Exception as error:
  print('Error write audio in .mp3 file')
  print(error)
