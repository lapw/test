from moviepy.editor import *

#sum = 0

clip = ["chip1","chip2","chip3","chip4","chip5","chip6","chip7","chip8"]
audio = ["audio1","audio2","audio3","audio4","audio5","audio6","audio7","audio8"]
count = 0


# performing sum of natural
# number
#for sum in range(0, 8):
#    sum = sum+1

if count < 8:

    count += 1
# Import the audio(Insert to location of your audio instead of audioClip.mp3)
    audio[count] = AudioFileClip(str(count)+".m4a")

# Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
    chip[count] = ImageClip(str(count)+".jpg").set_duration(audio[count].duration)

# Set the audio of the clip
    chip[count] = clip[count].set_audio(audio[count])
# Export the clip


else :

    videos = [clip[i+1] for i in range(count)]
    video = concatenate(videos)
    video.write_videofile('test.avi', fps=24, codec='mpeg4')

# concatenating both the clips
#final = concatenate_videoclips(chip1)

#clip.write_videofile("render.mp4", fps=24, audio_codec='aac')