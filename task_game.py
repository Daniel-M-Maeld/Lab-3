import tkinter as tk
import random
import pygame


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Heroes.mp3")
pygame.mixer.music.play()


def close():
    window.destroy()


coding = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
    }

def keygen():
    key = []
    for i in range(3):
        block, block_weight = genblock()
        key.append(block)
    return '-'.join(key)


def genblock():    
    while True:
            block = random.choices(list(coding.keys()), k=4)
            block_weight = sum(coding[letter] for letter in block)
            if 30 < block_weight < 35:
                return ''.join(block), block_weight


def start():
    lbl_result.configure(text=keygen())


window = tk.Tk()
window.title('Heroes 3 (under my influence)')
window.geometry('1280x720')
bg_img = tk.PhotoImage(file='Heroes.png')

label_pic = tk.Label(window, image=bg_img)
label_pic.place(x=0, y=0, relwidth=1, relheight=1)


frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.95, anchor='s')




lbl_result = tk.Label(frame, text='Now we are gonna play the game))', font=('courier', 20))
lbl_result.grid(column=1, row=1)


btn_start = tk.Button(frame, text='start game!!', width=10, height=2, command=start)
btn_start.grid(column=0, row=3, padx=15, pady=15)
btn_exit = tk.Button(frame, text='exit', width=10, height=2, command=close)
btn_exit.grid(column=2, row=3, padx=15, pady=15)


window.mainloop()
