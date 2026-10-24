from tkinter import *
# as gui does not support png,jpeg files, so for images we need to install "pip install pillow", then 
from PIL import Image,ImageTk
import speech_to_text
import text_to_speech
import action
import os

root=Tk()
root.title("AI Assistant")
root.geometry("600x870")   # width into height
root.resizable(False,False)     # to make window non-resizable
root.config(bg="#6F8FAF")

# ask fn
def ask():
    user_val = speech_to_text.speech_to_text()

    if not user_val:
        text_to_speech.text_to_speech("Voice not clear, please type your command")
        return

    text.insert(END, "User (voice) --> " + user_val + "\n")

    bot_val = action.Action(user_val)

    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")

    if bot_val == "ok sir":
        root.destroy()

# send fn
def send():
    user_val = entry.get()
    bot_val = action.Action(user_val)
    text.insert(END, "User --> "+user_val+"\n")
    if bot_val != None:
        text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()
    entry.delete(0,END)

def hotkey_action(command):
    bot_val = action.Action(command)

    text.insert(END, "Shortcut --> " + command + "\n")

    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")

# delete_text fn
def delete_text():
    text.delete("1.0", "end")
    

# frame
frame=LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", bg="#6F8FAF")     # intrenal padding
frame.grid(row=0, column=0, padx=80, pady=10)                                # external padding


# text
text_label= Label(frame, text="AI Assistant", font=("comic Sans ms",14,"bold"),bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)                       # external padding


# image
image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "image", "assistant.png")
image = ImageTk.PhotoImage(Image.open(image_path))
# image(open,edit,provess image) and imageTk(converts PIL image into tkinter compatible image) and photoimage(used to show images in tkinter)
image_label=Label(frame,image=image)                           # where to place
image_label.grid(row=1, column=0)


# textbox
text=Text(root, font=("courier",10,"bold"), bg="#356696")
text.grid(row=2, column=0)
text.place(x=115, y=375, width=375, height=100)           # x(dist from left side) and y(dist from top)


# entry widget
entry=Entry(root, justify=CENTER)
entry.place(x=127, y=500, width=350, height=30)


##### BUTTONS #####

# button 1
button1=Button(root, text="ASK", bg="#356696", borderwidth=3, relief=SOLID, command=ask)    # ask fn
button1.place(x=100, y=575, width=80, height=50)

# button 2
button2=Button(root, text="SEND", bg="#356696", borderwidth=3, relief=SOLID, command=send)    # send fn
button2.place(x=270, y=575, width=80, height=50)

# button 3
button3=Button(root, text="DELETE", bg="#356696", borderwidth=3, relief=SOLID, command=delete_text)    # delete_text fn
button3.place(x=440, y=575, width=80, height=50)

root.bind("<Control-g>", lambda event: hotkey_action("g"))                  # google
root.bind("<Control-y>", lambda event: hotkey_action("y"))                  # youtube
root.bind("<Control-t>", lambda event: hotkey_action("t"))                  # time
root.bind("<Control-d>", lambda event: hotkey_action("d"))                  # date
root.bind("<Control-m>", lambda event: hotkey_action("m"))                  # music
root.bind("<Control-l>", lambda event: delete_text())                       # clear text
root.bind("<Control-D>", lambda event: hotkey_action("day"))                # day(ctrl+shift+d)
root.bind("<Control-S>", lambda event: hotkey_action("shutdown"))           # shutdown(ctrl+shift+s)


root.mainloop()