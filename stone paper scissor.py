import random
import speech_recognition as sr  
import pyttsx3
def speak(a):
    engine = pyttsx3.init()
    engine.say(a)
    engine.runAndWait()
def recordchoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        alpha="Say your choice rock paper or scissor " 
        print(alpha)                                                                      
        speak(alpha)
        print("speak:")                                                                                   
        audio = r.listen(source)
    try:
        a=r.recognize_google(audio)
        a=a.lower()
        if a not in('rock','paper','scissor'):
            recordchoice()
        else:
            return a
    except sr.UnknownValueError:
        beta="Could not understand audio"
        print(beta)
        speak(alpha)
        recordchoice()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        recordchoice()
def rerecordnum():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        alpha="Speak No. Of times you want to play:"                                                                       
        print(alpha)
        speak(alpha)
        print("Speak:")                                                                                   
        audio = r.listen(source)
    try:
        a=r.recognize_google(audio)
        a=int(a)
        if a>0:
            return a
        else:
            rerecordnum()
    except sr.UnknownValueError:
        msg="Could not understand audio"
        print(msg)
        speak(msg)
        rerecordnum()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        rerecordnum()
    except ValueError:
        msg1="Unable to find integer value from the input Try again"
        print (msg1)
        speak(msg1)
        rerecordnum()
def rerecordname():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.say("Speak Your Name")
        engine.runAndWait()                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)
    try:
        a=r.recognize_google(audio)
        z=a
        j="Hello  "
        b="Welcome To The Game of Rock Paper and Scissor"
        a=j+a
        speak(a)
        speak(b)
        print(a)
        print(b)
    except sr.UnknownValueError:
        msg="Could not understand audio"
        print(msg)
        speak(msg)
        rerecordname()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        rerecordname()
    return z
def rechecknum(a):
    z=a
    alpha=1#yes
    beta=0#no
    print("Are you sure You want to play",a,"times")
    z="Are you sure You want to play "
    z=z+str(a)+" times"
    engine = pyttsx3.init()
    engine.say(z)
    engine.runAndWait()
    r = sr.Recognizer()
    alpha="Say Yes or No"
    print(alpha)
    speak(alpha) 
    with sr.Microphone() as source:                                                                       
        audio = r.listen(source)
    try:
        n=r.recognize_google(audio)
        if n.lower()=="yes":
            return alpha
        elif n.lower()=="no":
            return beta
        else:
            rerecordnum()
    except sr.UnknownValueError:
        print("Could not understand audio")
        rechecknum(z)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        rechecknum(z)
def checkwin(user,comp):
    i=0#draw
    j=1#user win
    k=2#comp win
    if user==comp:
        return i
    elif user=="rock":
        if comp=="paper":
            return k
        else:
            return j
    elif user=="paper":
        if comp=="rock":
            return j
        else:
            return k
    elif user=="scissor":
        if comp=="rock":
            return k
        else:
            return j
#code
choice=('rock','paper','scissor')
name=rerecordname()
print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")
engine = pyttsx3.init()
engine.say("Winning Rules of the Rock paper scissor game as follows")
engine.say("Rock versus paper paper wins ")
engine.say("Rock versus scissor Rock wins ")
engine.say("Paper versus scissor scissor wins ")
engine.say("Enter No. Of Times you want to play ")
engine.runAndWait()
#times=int(input("Enter No. Of Times you want to play"))
times=3
pointu=0
pointc=0
print("Let's start the game")
engine = pyttsx3.init()
engine.say("Let's start the game")
engine.runAndWait()
for a in range(times):
    user=recordchoice()
    z="User Choose "
    z=z+user
    print (z)
    speak(z)
    rint=random.randint(0,2)
    comp=choice[rint]
    sp="Computer Choose "
    sp=sp+comp
    print(sp)
    speak(sp)
    alpha=user+" versus "+comp
    print(user,"vs",comp)
    speak(alpha)
    win=checkwin(user,comp)
    if win==0:
        omega="Draw"
        print(omega)
        speak(omega)
    elif win==1:
        omega="User Wins"
        print(omega)
        speak(omega)
        pointu+=1
    else:
        omega="Computer Wins"
        print(omega)
        speak(omega)
        pointc+=1
msg1="Final Score"
msg2="User Scored "
msg2=msg2+str(pointu)
msg3="Computer Scored "
msg3=msg3+str(pointc)
print(msg1)
speak(msg1)
print(msg2)
speak(msg2)
print(msg3)
speak(msg3)
if pointu==pointc:
    z="The game is draw"
    print(z)
    speak(z)
elif pointu>pointc:
    z="User wins"
    print(z)
    speak(z)
else:
    z="computer wins"
    print(z)
    speak(z)

    
    
    
    