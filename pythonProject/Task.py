import pyautogui
import time
time.sleep(4)
# s = "Do not Mean a Thing If it is not Got That Swing"
s = "ti pidor"
# s = 'I love you I love you I love you'
# s = 'Relax'
# s = "I love you"
for i in range(1):
    messege = s
    pyautogui.typewrite(messege)
    pyautogui.press("enter")
for n in range(211):
    a = (s[n % len(s):] + s[:n % len(s)])
    messege = a
    pyautogui.typewrite(messege)
    pyautogui.press("enter")
for i in range(2):
    messege = s
    pyautogui.typewrite(messege)
    pyautogui.press("enter")
# for i in f:
#     time.sleep(2)
#     messege = i
#     pyautogui.typewrite(messege)
#     pyautogui.press("enter")







