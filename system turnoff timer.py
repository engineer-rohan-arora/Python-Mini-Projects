import os
a=int(input("enter no. of hours after which the system has to be turned off "))
b=int(input("enter no. of minutes after which the system has to be turned off "))
c=int(input("enter no. of seconds after which the system has to be turned off "))
d= (3600 * a) + (60*b) + c

x = "shutdown.exe -s -t " ,d  
t = str(x)
r=""
for f in (t) :
    if f not in [ "(" , ")" , "'" , ","] :
        r=r+f
q=open('hit.bat','w')
q.write(r)
q.close()
qer = os.getcwd()
from subprocess import Popen
p = Popen("hit.bat", cwd=r"C:\Users\dell\Desktop")
stdout, stderr = p.communicate()
print " Execution sucessful "
os.remove("hit.bat")
while True:
    print " press 1 to abort shut down"
    print " press 2 to make changes "
    print " enter any other number to exit"
    ch =int(raw_input("enter your choice"))
    if ch == 1 :
        q=open('can.bat','w')
        q.write('shutdown.exe -a')
        q.close()
        qer = os.getcwd()
        from subprocess import Popen
        p = Popen("can.bat", cwd=r"C:\Users\dell\Desktop")
        stdout, stderr = p.communicate()
        print " Execution aborted "
        os.remove("can.bat")
    if ch==2 :
        q=open('can.bat','w')
        q.write('shutdown.exe -a')
        q.close()
        qer = os.getcwd()
        from subprocess import Popen
        ra = Popen("can.bat", cwd=r"C:\Users\dell\Desktop")
        stdout, stderr = ra.communicate()
        print " Execution aborted "
        os.remove("can.bat")
        a=int(raw_input("enter no. of hours after which the system has to be turned off "))
        b=int(raw_input("enter no. of minutes after which the system has to be turned off "))
        c=int(raw_input("enter no. of seconds after which the system has to be turned off "))
        d= (3600 * a) + (60*b) + c
        x = "shutdown.exe -s -t " ,d
        t = str(x)
        r=""
        for f in (t) :
            if f not in [ "(" , ")" , "'" , ","] :
                r=r+f
        q=open('hit.bat','w')
        q.write(r)
        q.close()
        qer = os.getcwd()
        from subprocess import Popen
        p = Popen("hit.bat", cwd=r"C:\Users\dell\Desktop")
        stdout, stderr = p.communicate()
        print " Execution sucessful "
        os.remove("hit.bat")
    if ch not in [ 1, 2 ]:
        break
        


        

