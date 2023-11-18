from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissors Paper")
root.geometry("655x368")

# Chargez l'image d'arrière-plan
bg_image = Image.open('images/natural_reduit.png')
bg_photo = ImageTk.PhotoImage(bg_image)

# Créez un canvas et ajoutez-y l'image
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# picture
# for user
rock_img_user = ImageTk.PhotoImage(Image.open("images/rocks_users.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("images/papers_users.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("images/scissors_users.png"))

# for ordinareur
rock_img = ImageTk.PhotoImage(Image.open("images/rocks_computer.png"))
paper_img = ImageTk.PhotoImage(Image.open("images/papers_computer.png"))
scissor_img = ImageTk.PhotoImage(Image.open("images/scissors_computer.png"))

user_label = Label(canvas, image=scissor_img_user, bg='#bee7fb')  ##bee7fb   ##bce4fb
user_label.grid(row=1, column=4, pady=10)
comp_label = Label(canvas, image=scissor_img, bg='#bee7fb')
comp_label.grid(row=1, column=0, pady=10)

# scores
playerscore = Label(canvas, text=0, font=100, bg='#bee7fb', fg="black")
playerscore.grid(row=1, column=3, pady=10)
computerscore = Label(canvas, text=0, font=100, bg='#bee7fb', fg="black")
computerscore.grid(row=1, column=1, pady=10)

# indication
user_indicator = Label(canvas, font=50, text="USER", bg='#bee7fb', fg="black")
user_indicator.grid(row=0, column=3, pady=10)
comp_indicator = Label(canvas, font=50, text="COMPUTER", bg='#bee7fb', fg="black")
comp_indicator.grid(row=0, column=1, pady=10)

# messages
msg = Label(canvas, font=50, bg='#bee7fb', fg="black")
msg.grid(row=1, column=2, pady=10)

# update message
def updatemessage(x):
    msg["text"] = x

# update user score
def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

# update computer score
def updatecomputerscore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

# check winner
def checkwiner(player, computer):
    if player == computer:
        updatemessage("its a tie !!!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("you loose")
            updatecomputerscore()
        else:
            updatemessage("you win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
           updatemessage("you loose")
           updatecomputerscore()
        else:
            updatemessage("you win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updatemessage("you loose")
            updatecomputerscore()
        else:
            updatemessage("you win")
            updateuserscore()
    else:
        pass

# update choices
choices = ["rock", "paper", "scissor"]
def updatechoice(x):
    # for computer
    compchoice = choices[randint(0, 2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)
    # for user
    if x=="rock":
        user_label.configure(image=rock_img_user)
    elif x=="paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)
    checkwiner(x, compchoice)

# Ajout des boutons de réinitialisation et de sortie
def reset_game():
    playerscore["text"] = "0"
    computerscore["text"] = "0"
    user_label.configure(image=scissor_img_user)
    comp_label.configure(image=scissor_img)
    updatemessage("Game Reset!")

def quit_game():
    root.destroy()

reset_button = Button(canvas, width=10, height=1, text="Reset Game", bg="#FF3E4D", fg="white", command=reset_game)
reset_button.grid(row=3, column=1, pady=30)

quit_button = Button(canvas, width=10, height=1, text="Quit Game", bg="#FAD02E", fg="white", command=quit_game)
quit_button.grid(row=3, column=3, pady=30)

# Vos boutons existants
rock_button = Button(canvas, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updatechoice("rock"))
rock_button.grid(row=2, column=1, pady=10)

paper_button = Button(canvas, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updatechoice("paper"))
paper_button.grid(row=2, column=2, pady=10)

scissor_button = Button(canvas, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updatechoice("scissor"))
scissor_button.grid(row=2, column=3, pady=10)

root.mainloop()
