from pygame import mixer
import pyaudio
import threading
from tkinter import messagebox

click =False
running = False
music_list =["./1.mp3",
             "./2.mp3",
             "./3.mp3",
             "./4.mp3",
             "./5.mp3",
             "./6.mp3",
             "./7.mp3",
             "./8.mp3",
             "./9.mp3"]
#streaming function
def start_audio():
    global running,click
    
    try:
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        p = pyaudio.PyAudio()

        stream_in = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        
        stream_out = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True)

        while running:
            data = stream_in.read(CHUNK)
            stream_out.write(data)
    except Exception:
        messagebox.showerror("Streaming Error","Check default input output settings and restart the application")
        click=False
        running=False
    finally:
        stream_in.stop_stream()
        stream_in.close()
        stream_out.stop_stream()
        stream_out.close()
        p.terminate()

    

    
#streaming thread
def start_thread():
    global audio_thread
    audio_thread = threading.Thread(target=start_audio)
    audio_thread.start()
    
#button functions
def button_func_1():
    global music_list
    try:
        mixer.music.load(music_list[0])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
        

def button_func_2():
    try:
        mixer.music.load(music_list[1])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
    
def button_func_3():
    try:
        mixer.music.load(music_list[2])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")

def button_func_4():
    try:
        mixer.music.load(music_list[3])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
        
def button_func_5():
    try:
        mixer.music.load(music_list[4])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
        
def button_func_6():
    try:
        mixer.music.load(music_list[5])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
 
def button_func_7():
    try:
        mixer.music.load(music_list[6])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
        
        
def button_func_8():
    try:
        mixer.music.load(music_list[7])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")

def button_func_9():
    try:
        mixer.music.load(music_list[8])
        mixer.music.play()
        
    except:
        messagebox.showerror("Sound File Error","Check the existing file in appliaction location.The File name must be 1 to 9 .mp3")
        
        
#volume set function
def volume_set_func(value):
    mixer.music.set_volume(value)
    
#streaming button
def streaming_button():
    global click,running
    
    if click == False:
        click =True
        running = True
    else:    
        running = False
        click = False
        
        
    start_thread() 
    
    
#Periodicly set or reset radio button     
def periodic_func_1000(app,stream_radio_button):
    
    if running == True:
        stream_radio_button.select()
        
    else:
        stream_radio_button.deselect()
        
    
    
    app.after(1000, periodic_func_1000,app,stream_radio_button)
    

    
    

