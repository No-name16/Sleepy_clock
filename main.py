import eel
import time
import threading
import pygame
from tkinter import messagebox  
import time
import os

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    
  
class Calculator :
    def _init_(self):
        self.hours = 0
        self.minutes = 0
        
    def count(self) :
        temp = self.hours
        temp2 = self.minutes
        self.hours -= 7
        self.minutes -=30
        if self.minutes < 0:
            self.minutes = 60 + self.minutes
            self.hours -=1
        if self.hours < 0:
            self.hours = 24+self.hours
        if self.hours < 10:
            self.hours = "0" +str(self.hours)
        if self.minutes < 10:
            self.minutes = "0" +str(self.minutes)
        else:
            self.hours = str(self.hours)
            self.minutes = str(self.minutes)
        last_time = str(self.hours)+":"+str(self.minutes)
        print(last_time)
        
        messagebox.showinfo("Calculator","Хороший сон состоит из 5–6 полных циклов. Чтобы встать в бодром состоянии, запланируйте пробуждение в конце цикла. Учтите: обычно, чтобы заснуть, человеку нужно 14 минут."+"\n")
        print("Хороший сон состоит из 5–6 полных циклов. Чтобы встать в бодром состоянии, запланируйте пробуждение в конце цикла. Учтите: обычно, чтобы заснуть, человеку нужно 14 минут.")
        return str(last_time)
           
class Alarm(threading.Thread):
    def __init__(self):
        super(Alarm, self).__init__()
        self.note = None
        self.line = None
        self.number = 0
        self.time_num = 0
        self.keep_running = True

    def run(self):
        if self.number == 1:
            try:
                while self.keep_running:
                    now = time.localtime()
                    print(int(now.tm_hour),int(self.hours) , int(now.tm_min) , int(self.minutes))
                    if (int(now.tm_hour) == int(self.hours) and int(now.tm_min) == int(self.minutes)):
                        pygame.mixer.init()
                        pygame.mixer.music.load(self.sound)
                        pygame.mixer.music.play()
                        messagebox.showinfo("Sleepy clock", str(self.note+"\n"+self.line))
                        pygame.mixer.music.pause()
                        self.keep_running = False
                        return 
                    
            except:
                return 
        
        elif self.number == 2:
            try:
                print ("foo")
                countdown(self.time_num)
                pygame.mixer.init()
                pygame.mixer.music.load(self.sound)
                pygame.mixer.music.play()
                messagebox.showinfo("Time is out","00:00"+"\n"+str(self.note+"\n"+self.line))
                pygame.mixer.music.pause()
                self.keep_running = False
                return 
                    
            except:
                return 
        
    def just_die(self):
        self.keep_running = False
        
alarm = Alarm()  
        
@eel.expose
def get_settings2(note, line):
    alarm.note = note
    alarm.line = line
    alarm.keep_running = True
    print(line)
    alarm.run()   
    
@eel.expose
def get_settings(time, sound):
    alarm.hours = time[:2]
    alarm.minutes = time[3:5]
    alarm.time_num = (int(alarm.hours))*60+int(alarm.minutes)
    print(alarm.hours)
    print(alarm.minutes)
    alarm.sound = sound
    print(sound)

@eel.expose
def get_settings1(number):
    alarm.number = number
    print(number)
        

    
make_count = Calculator()
@eel.expose
def calc(time):
    make_count.hours = int(time[:2])
    make_count.minutes = int(time[3:5])
    print(make_count.hours)
    print(make_count.minutes)
    return make_count.count()
    
    
    
eel.init("C:\\Users\\User\\Desktop\\проект\\web")
eel.start("main.html", size=(1920,1080))

