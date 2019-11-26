import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui
from text_to_voice import Text

ser = serial.Serial('/dev/ttyUSB0',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established
print (ser.readline())
while True:
    incoming = str (ser.readline()) #read the serial data and print it as line
    print (incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.press(['space'])
        time.sleep(3.5)

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')
        

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if ' userabsent' in incoming:
    	pass
    	#pyautogui.hotkey('ctrl', 'alt', 'del')
    	#time.sleep(2)
    	#pyautogui.press('enter')

    incoming = "";
    