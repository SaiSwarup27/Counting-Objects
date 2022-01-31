import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import SUNKEN, filedialog

def select_image():
    global panelA,panelB,entry
    path=filedialog.askopenfilename()
    image=cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    canny = cv2.Canny(blur, 30, 100)
    dilated = cv2.dilate(canny, (1, 1), iterations=0)
    cnt, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb2 = cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    rgb2 = Image.fromarray(rgb2)
    rgb2 = ImageTk.PhotoImage(rgb2)

    panelA = tk.Label(image=image)
    panelA.image = image
    panelA.grid(row=0,column=0)

    panelB = tk.Label(image=rgb2)
    panelB.image = rgb2
    panelB.grid(row=0,column=1)

    entry=tk.Entry(width=30)
    entry.grid(row=1,column=0,columnspan=2)
    entry.insert(0,'Number of Objects: ')
    entry.delete(20,tk.END)
    entry.insert(20,len(cnt))

 
window=tk.Tk()
panelA = None
panelB = None
entry = None
button=tk.Button(text="select image",width=40,relief=SUNKEN,command=select_image)
button.grid(row=2,column=0,columnspan=2,pady=10)

window.mainloop()
