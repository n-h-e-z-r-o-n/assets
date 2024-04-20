import tkinter as tk
import ctypes as ct


def title_bar_color(color):
    global root
    root.update()
    if color.startswith('#'):
        blue = color[5:7]
        green = color[3:5]
        red = color[1:3]
        color = blue + green + red
    else:
        blue = color[4:6]
        green = color[2:4]
        red = color[0:2]
        color = blue + green + red
    print(color)
    get_parent = ct.windll.user32.GetParent
    HWND = get_parent(root.winfo_id())

    color = '0x' + color
    color = int(color, 16)

    ct.windll.dwmapi.DwmSetWindowAttribute(HWND, 35, ct.byref(ct.c_int(color)), ct.sizeof(ct.c_int))


root = tk.Tk()
title_bar_color("#123454") # color in hex format
root.mainloop()
