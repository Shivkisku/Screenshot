import tkinter as tk
import pyautogui

win = tk.Tk()
win.title("LoopGlitch Screenshoter")

def callback():
    try:
        mySS = pyautogui.screenshot()
        mySS.save(r'E:\PyCharm\mySSpy.jpg')  #r'Path to save the screenshot\file name.png or jpg'
    except:
        print("Unable to take screenshot")

button = tk.Button(win, text="Screenshot This!", command=callback)
button.grid(row=0, column=0)

win.mainloop()
