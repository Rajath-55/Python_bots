from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

search_box = './images/search.png'
message_box = './images/message.png'

browser = wb.get('google-chrome')

names = ['Chinmaya Bhat']
messages = []
file = open('dante.txt', 'r')
for line in file:
    messages.append(line)
    
browser.open('https://web.whatsapp.com')
coordinates = None
x = 1

while coordinates == None:
    sleep(5)
    x+=1
    if x==12:
        print("Error in locating search box!")
        break
    coordinates = locateOnScreen(search_box)
    
x1,y1 = center(coordinates)
print(x1,y1)

moveTo(x1,y1)
click()
typewrite(names[0], interval = 0.25)
sleep(2)
press('enter')

c = confirm(text = "Did we get the right person? Pls say yes", title="Hopes ",buttons = ['Yes', 'Cancel'])

if c=='Cancel':
    sys.exit()

msg_coordinates = None

# while msg_coordinates == None:
#     sleep(5)
#     x+=1
#     if x==12:
#         print("Error in locating message box!")
#         break
#     msg_coordinates = locateOnScreen(message_box)
#     print(msg_coordinates)

# x2,y2 = center(msg_coordinates)

# moveTo(x2,y2)
# click()
sleep(2)
count=50

# while count!=0:
#     count-=1
for message in messages:
    typewrite(message)
    press('enter')

print('Success!')    
