
from pygame import mixer

import tkinter as tk
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
import my_functions



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("213x250")#windows size
app.minsize(213,250)#constant size
app.maxsize(213,250)#constant size
app.title("Sound Effect Board")#window title


mixer.init()


#First Button Row -> Row=2
Button_1_text = "1"
Buttton_1 = customtkinter.CTkButton(master =app , text=Button_1_text,width=60,height=60,command=my_functions.button_func_1)
Buttton_1.grid(row=2, column=0,padx =5,pady = 5)

Button_2_text = "2"
Buttton_2 = customtkinter.CTkButton(master =app , text=Button_2_text,width=60,height=60,command=my_functions.button_func_2)
Buttton_2.grid(row=2, column=1,padx =5,pady = 5)

Button_3_text = "3"
Buttton_3 = customtkinter.CTkButton(master =app , text=Button_3_text,width=60,height=60,command=my_functions.button_func_3)
Buttton_3.grid(row=2, column=2,padx =5,pady = 5)



#Second Button Row -> Row=3
Button_4_text = "4"
Buttton_4 = customtkinter.CTkButton(master =app , text=Button_4_text,width=60,height=60,command=my_functions.button_func_4)
Buttton_4.grid(row=3, column=0,padx =5,pady = 5)

Button_5_text = "5"
Buttton_5 = customtkinter.CTkButton(master =app , text=Button_5_text,width=60,height=60,command=my_functions.button_func_5)
Buttton_5.grid(row=3, column=1,padx =5,pady = 5)

Button_6_text = "6"
Buttton_6 = customtkinter.CTkButton(master =app , text=Button_6_text,width=60,height=60,command=my_functions.button_func_6)
Buttton_6.grid(row=3, column=2,padx =5,pady = 5)



#Third Button Row -> Row=4
Button_7_text = "7"
Buttton_7 = customtkinter.CTkButton(master =app , text=Button_7_text,width=60,height=60,command=my_functions.button_func_7)
Buttton_7.grid(row=4, column=0,padx =5,pady = 5)

Button_8_text = "8"
Buttton_8 = customtkinter.CTkButton(master =app , text=Button_8_text,width=60,height=60,command=my_functions.button_func_8)
Buttton_8.grid(row=4, column=1,padx =5,pady = 5)

Button_9_text = "9"
Buttton_9 = customtkinter.CTkButton(master =app , text=Button_9_text,width=60,height=60,command=my_functions.button_func_9)
Buttton_9.grid(row=4, column=2,padx =5,pady = 5)



#streaming_button
streaming_button = customtkinter.CTkButton(master=app,width=70,height=15,command=my_functions.streaming_button,text='Stream')
streaming_button.place(relx=0.19, rely=0.95,anchor=tk.CENTER)

#
stream_radio_button = customtkinter.CTkRadioButton(master=app,text ='')
stream_radio_button.place(relx=0.60, rely=0.95,anchor=tk.CENTER)


#volume slider
volume_slider = customtkinter.CTkSlider(master=app,width=90,height=15,from_=0, to=1,command=my_functions.volume_set_func)
volume_slider.place(relx=0.54, rely=0.95,anchor="w")



my_functions.periodic_func_1000(app, stream_radio_button)

app.mainloop()
