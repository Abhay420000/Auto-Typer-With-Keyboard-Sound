from playsound import playsound
import pyautogui
import time

srting_to_Write = """A paragraph is a series of related sentences developing a central idea, called the topic.
Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a
group of sentences that supports one central, unified idea. Paragraphs add one idea at a
time to your broader argument.
"""

op = input("Mechanical-Keyboard|Non-M-Keyboard: ")
pause_time = float(input("Input break Time: "))

ts = int(input("Time to Start: "))

print(f"Starting in {ts}sec.")
time.sleep(ts)

kb_Sound = {'!':'1.mp3','"':'1.mp3','#':'1.mp3','$':'1.mp3','%':'1.mp3','&':'1.mp3','"':'1.mp3','(':'1.mp3',')':'1.mp3','*':'1.mp3','+':'1.mp3',',':'1.mp3','-':'1.mp3','.':'1.mp3','/':'1.mp3','0':'1.mp3','1':'1.mp3','2':'1.mp3','3':'1.mp3','4':'1.mp3','5':'1.mp3','6':'1.mp3','7':'1.mp3','8':'1.mp3','9':'1.mp3',':':'1.mp3',';':'1.mp3','<':'1.mp3','=':'1.mp3','>':'1.mp3','?':'1.mp3','@':'1.mp3','[':'1.mp3','\\':'1.mp3',']':'1.mp3','^':'1.mp3','_':'1.mp3','`':'1.mp3','a':'6.mp3','b':'6.mp3','c':'8.mp3','d':'1.mp3','e':'7.mp3','f':'7.mp3','g':'6.mp3','h':'1.mp3','i':'1.mp3','j':'8.mp3','k':'6.mp3','l':'1.mp3','m':'7.mp3','n':'8.mp3','o':'7.mp3','p':'1.mp3','q':'8.mp3','r':'6.mp3','s':'8.mp3','t':'1.mp3','u':'6.mp3','v':'8.mp3','w':'7.mp3','x':'8.mp3','y':'8.mp3','z':'7.mp3','{':'1.mp3','|':'1.mp3','}':'1.mp3','~':'1.mp3',"'":'1.mp3',
             'shift':"2.mp3",
             '\n':"3.mp3",'\r':"3.mp3",
             '\t':"4.mp3",
              ' ':"5.mp3"}

def playS(letter):
    try:
        playsound(f'./{op}/{kb_Sound[letter]}', block = False)
    except:
        playsound(f'./{op}/default.mp3', block = False)

for letter in srting_to_Write:
    playS(letter)
    pyautogui.write(letter)
    time.sleep(pause_time)
