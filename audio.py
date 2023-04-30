import gtts  
from playsound import playsound  

t1 = gtts.gTTS("Far.mp3")
t2 = gtts.gTTS("Near.mp3")  

# # saving the audio file  
# t1.save("far.mp3")  
# t2.save("near.mp3")

playsound("far.mp3")