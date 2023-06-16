import serial
import pyautogui as pg
import AppOpener as Ao

port = "com16"
baudRate = 9600

ard = serial.Serial(port="com16", baudrate=9600)
while True:
    output = ard.readline().decode(encoding="utf-8").strip()
    # print(output)
    if output == "Up":
        pg.move(0, -35)
    elif output == "Down":
        pg.move(0, 35)
    elif output == "Right":
        pg.move(35, 0)
    elif output == "Left":
        pg.move(-35, 0)
    elif output == "Ok":
        pg.click()
        ard.reset_input_buffer()
    elif output == "VolumeUp":
        pg.press("volumeup")
    elif output == "VolumeDown":
        pg.press("volumedown")
    elif output == "Mute":
        pg.press("volumemute")
        ard.reset_input_buffer()
    elif output == "Menu":
        pg.press("win")
        ard.reset_input_buffer()
    elif output == "Info":
        Ao.open("settings")
        ard.reset_input_buffer()
    elif output == "Exit":
        pg.click(1910, 1045)
        ard.reset_input_buffer()
    elif output == "F1":
        Ao.open("file explorer")
        ard.reset_input_buffer()
    elif output == "F2":
        Ao.open("terminal")
        ard.reset_input_buffer()
    elif output == "F3":
        Ao.open("google chrome")
        ard.reset_input_buffer()
    elif output == "F4":
        Ao.open("task manager")
        ard.reset_input_buffer()
    elif output == "Play-Pause":
        pg.press("playpause")
        ard.reset_input_buffer()
    elif output == "Forward":
        pg.press("right")
        ard.reset_input_buffer()
    elif output == "Backward":
        pg.press("left")
        ard.reset_input_buffer()
    elif output == "ScrollUp":
        pg.scroll(100)
    elif output == "ScrollDown":
        pg.scroll(-100)
    elif output == "Power":
        pg.hotkey("win", "tab")
        ard.reset_input_buffer()
