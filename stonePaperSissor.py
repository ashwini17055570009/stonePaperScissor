import tkinter as tk
from random import randint
from tkinter import Label, ttk
root=tk.Tk()
#root.iconbitmap('rpc.ico')
root.config(bg="white")#change background color to gray
rock= tk.PhotoImage(file='D:/MCA/Projects/rock.jpeg')
paper= tk.PhotoImage(file='D:/MCA/Projects/p.png')
scissor=tk.PhotoImage(file='D:/MCA/Projects/sci.jpeg')
#add image to a list
image_list=[rock,paper,scissor]
#pick random number between 0 and 2
pick_number=randint(0,2)
image_label= tk.Label(root,image=image_list[pick_number], bd=0)
image_label.pack(pady=20)
#create spin funtion
def spin():
    #pick random number
    pick_number=randint(0,2)
    #show image
    image_label.config(image=image_list[pick_number])
    # 0- rock
    # 1- paper
    # 2- scissor
    #convert dropdown choice to a number
    if user_choice.get()== "Rock":
        user_choice_value=0
    elif user_choice.get()=="Paper":
        user_choice_value=1
    else:
        user_choice_value=2
    #determine if we won or lost
    if user_choice_value==0:
        if pick_number ==0:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number==1:
            win_lose_label.config(text="Paper covers rock! You loose...")
        elif pick_number==2:
            win_lose_label.config(text="Rock can break scissor! You win...")
    if user_choice_value==1:
        if pick_number ==1:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number==2:
            win_lose_label.config(text="Scissor cuts paper! You loose...")
        elif pick_number==0:
            win_lose_label.config(text="Paper covers rock! You win...")
    if user_choice_value==2:
        if pick_number ==2:
            win_lose_label.config(text="It's a tie! Spin again...")
        elif pick_number==0:
            win_lose_label.config(text="Rock smash scissor! You loose...")
        elif pick_number==1:
            win_lose_label.config(text="Scissor cuts paper! You win...")
# create choice
user_choice=ttk.Combobox(root,value=("Rock","Paper","Scissor"))
user_choice.current(0)
user_choice.pack(pady=20)
#create spin button
spin_button=tk.Button(root,text="spin!",command=spin)
spin_button.pack(pady=10)
# label for result
win_lose_label=Label(root,text="",font=("Helvetica",18))
win_lose_label.pack(pady=50)
root.mainloop()