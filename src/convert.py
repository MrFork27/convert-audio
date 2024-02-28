import moviepy.editor as mp

def convert(mp4FileName, mp3FileName):
  try:
    # Load .mp4 file
    clip = mp.VideoFileClip(mp4FileName)

    # Write audio in .mp3 file
    clip.audio.write_audiofile(mp3FileName)
  except Exception as error:
    print(error)

# Test file path
mp4File = "./media/audio-video.mp4"
mp3File = "./media/audio.mp3"

convert(mp4File, mp3File)
