from moviepy.editor import *
from moviepy.video.tools.drawing import color_split


#clip = VideoClip(make_frame, duration=4) # for custom animations (see below)
clip1 = ImageClip("my.png").set_duration(10) # or .jpeg, .tiff, ...
clip2 = ImageClip('sen.jpg').set_duration(10).fx( vfx.resize, width=360)
clip3 = ImageClip('kir.jpg').set_duration(10).fx( vfx.resize, width=360)
start_clip = ImageClip('friends.jpg').set_duration(10).fx( vfx.resize, width=360)
audio = AudioFileClip("audio.mp3").subclip(5,15)

#clip = VideoFileClip("myvideo.mp4").margin(10) # add 10px contour


cc = CompositeVideoClip([clip2.set_pos('left'),clip3.set_pos('right')],size = (720,480))
cc.set_audio(audio).write_videofile("my_stack.mp4",fps=30)

#final_clip = clips_array([[clip1, clip2]])
#final_clip.resize(width=720).set_audio(audio).write_videofile("my_stack.mp4",fps=30)
#clip = ColorClip(size=(720,480), color=[R,G,B])