from tkinter import*

import Speech_to_text
import action


root = Tk()
root.title("Virtual Assistant")
root.geometry('550x675')
root.resizable(False,False)
root.config(bg="#6F87AF")

def ask():
    user_val =Speech_to_text.speech_to_txt()
    bot_val = action.Action(user_val)
    text.insert(END , 'Me :'+ user_val+"\n")
    if bot_val != None:
        text.insert(END , "Bot :"+str(bot_val)+"\n")
    if bot_val == "ok sir" :
        root.destroy()
    
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END , 'Me :'+ send+"\n")
    if bot != None:
        text.insert(END , "Bot :"+str(bot)+"\n")
    if bot == "ok sir" :
        root.destroy()

def delete():
    text.delete('1.0', "end")

#frame
frame = LabelFrame(root, padx=100, pady=7,borderwidth=3 , relief="raised")
frame.config(bg="#6F87AF")
frame.grid(row=0, column= 1, padx=55, pady=10)

#txt label
text_lable = Label(frame, text="Virtual Assistant", font=("cosmic Sams ms", 14, "bold"), bg="#356696")
text_lable.grid(row=0, column=0, padx=55, pady=10)

#Text widget
text =Text(root, font=("courier 10 bold"),bg ="#356696")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

#Entry widget
entry =Entry(root, justify=CENTER)
entry.place(x=100, y=500, width= 350, height=30)

#buttons
#1
Button1 =Button(root, text="ASK", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)
#2
Button2 =Button(root, text="SEND", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)
#3
Button3 =Button(root, text="Delete", bg="#356696", padx=40, pady=16, borderwidth=3, relief=SOLID, command=delete)
Button3.place(x=225, y=575)

root.mainloop()