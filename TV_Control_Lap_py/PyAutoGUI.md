# PyAutoGUI

   [Documentation](https://pyautogui.readthedocs.io/en/latest/)

> PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.

## Installation

```cmd
pip install pyautogui
```

- Type this command in the 'Command Prompt'

---

## Importing

```python
import pyautogui
```

- You should start your python code with this line to get access to all library features 

---

## Features

### 1] pyautogui.size

```python
pyautogui.size()
```

- Get the size of the primary monitor, return screenWidth and screenHeight

> ###### Example
> 
> ```python
> import pyautogui
> 
> screenWidth, screenHeight = pyautogui.size()
> 
> print("Screen Width: ", screenWidth)
> print("Screen Height: ", screenHeight)
> ```
> 
> ```python
> 1920
> 1080
> ```
> 
> - Both screenWidth and screenHeight are integers

------

### 2] pyautogui.position

```python
pyautogui.position()
```

- Get the XY position of the mouse

> ###### Example
> 
> ```python
> import pyautogui
> 
> while True:
>     currentPosition = tuple(pyautogui.position())
>     print(currentPosition)
> ```
> 
> ```python
> (774, 561)
> (774, 561)
> (774, 561)
> (761, 587)
> (761, 587)
> ....
> ...
> .
> ```
> 
> - `while`: so you can print as you want
> 
> - `tuple`: change its type into tuple to have a nice output

---

### 3] Mouse Control Functions

```python
pyautogui.moveTo(100, 150)
```

- Move the mouse to XY coordinates w.r.t screen size

```python
pyautogui.move(400, -10)
```

- Move the mouse 400 pixels to the right and 10 pixels to the top of its current position

```python
pyautogui.click()
```

- Left click on the mouse

```python
pyautogui.click(100, 200)
```

- Move the mouse to XY coordinates and click it

```python
pyautogui.doubleClick(1850, 1050, interval=2)
```

- 1850 --> X

- 1050 --> Y

- 2 sec --> Time Interval between the 2 clicks

> ###### Example
> 
> ```python
> import pyautogui
> import time
> 
> pyautogui.moveTo(340, 1050)
> pyautogui.click()
> # Right-Click on the Windows Icon
> pyautogui.move(925, -725)
> pyautogui.click()
> # Move to the settings icon
> time.sleep(3)
> # Wait for 3 seconds for the settings to open
> pyautogui.doubleClick(1850, 1050, interval=2)
> # Double-click on the calendar button
> ```
> 
> - Positions will differ from user to another

```python
pyautogui.moveTo(100, 200, 5)
```

- Moves mouse to X of 100, Y of 200 over 2 seconds

```python
pyautogui.dragTo(755, 65, duration=3, button='left')
```

- Go to the position while holding the left mouse button for 3 seconds

- can be `button='right'` to hold the right mouse button

- There is also `drag` to move relative to the current position

```python
pyautogui.click(button='right', clicks=3, interval=1)
```

- Press on the right mouse key 3 times with 1 sec between clicks

```python
pyautogui.scroll(1000)
```

- Scroll 1000 pixels upwards

- To scroll pixels downwards: `scroll(-500)`

---

### 4] Keyboard Control Functions

```python
pyautogui.write('Hello world!')
```

- Type "Hello world!" instantly where the cursor is selected

```python
 pyautogui.write('Hello world!', interval=0.5)
```

- Type "Hello world!" with time interval = 0.5 sec between each lette

```python
pyautogui.press('enter')
```

- Press the Enter key

```python
pyautogui.press('left', presses=3, interval = 0.1)
```

- 0.1 sec between each press

```python
pyautogui.hotkey("ctrl", "shift", "esc")
```

- Shortuct to open Task Manager

> ###### Example
> 
> ```python
> import pyautogui
> 
> screenWidth, screenHeight = pyautogui.size()
> 
> pyautogui.click(screenWidth / 2, screenHeight / 2)
> # Click in the center of the screen
> pyautogui.press("enter")
> # To make a new line
> pyautogui.write("# I am typing, Can you see me?", interval=0.2)
> pyautogui.press("enter")
> pyautogui.write("# I am going to delete what I have just written", interval=0.1)
> pyautogui.press("enter")
> pyautogui.write("# GoodBye", interval=0.15)
> pyautogui.press("backspace", presses=89, interval=0.1)
> # Open Task Manager
> ```

```python
pyautogui.platformModule.keyboardMapping.keys()
```

- Get valid keys names, you can enter while using keyboard control functions

> ###### Example
> 
> ```python
> import pyautogui
> 
> keys = pyautogui.platformModule.keyboardMapping.keys()
> 
> print(tuple(keys))
> ```
> 
> ![](https://github.com/Mohamed-Walid-24/TV_Control_Lap/blob/main/Pics/Keys.png?raw=true)
> 
> - You can also take a look from the following link [KeyBoard_Keys](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)

---

### 5] Message Box Functions

- For displaying message boxes as `alert`, `confirm`, `prompt`, `password`

[Message Box Functions &mdash; PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/msgbox.html#message-box-functions)

--- 

### 6] ScreenShot Functions

- Take screenshots of the screen and save them

- Locating images within the screen

[Screenshot Functions &mdash; PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/screenshot.html#screenshot-functions)

---
