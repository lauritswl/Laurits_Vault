from psychopy import visual, event, core, gui, data
import glob
import random
import pandas as pd
from datetime import datetime
import os #to use os. fucntions


 #Allow æøå
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'æ', u'ø', u'å']
 #Core Clock
clock = core.Clock()
 #Get date for logfile names
date = data.getDateStr()
 #Prepare pandas data frame for recorded data
columns = ['Identifikation', 'Alder', 'Køn', 'Condition','Video', 'Svar']
logfile = pd.DataFrame(columns=columns)

# define dialogue box (important that this happens before you define window)
def personalData(): 
    box = gui.Dlg(title = "Sentence understanding experiment")
    box.addField("Identifikation: ") 
    box.addField("Alder: ")
    box.addField("Køn: ", choices=["Kvinde", "Mand", "Andet"])
    box.show()
    if box.OK: # To retrieve data from popup window
        ID = box.data[0]
        AGE = box.data[1]
        GENDER = box.data[2]
    elif box.Cancel: # To cancel the experiment if popup is closed
        core.quit()


# Introduction Text
#instructions
instruction = '''
Velkommen til sætningsforståelses eksperimentet!\n\n
Om et øjeblik, bliver du præsenteret for nogle sætninger, hvor din opgave er, at forstå, hvad der bliver sagt.
Når sætningen stopper, skal du skrive sætningen ned, som den blev sagt.\n\n
Sætningerne bliver præsenteret som lydfiler eller videoer. \n\n
Når du er klar til at starte, tryk på space tasten. 
'''
goodbye = '''
Eksperimentet er slut.\n\n
Tak for din deltagelse!'''


#Fixation cross
def fixcross(win):
    cross = """+"""
    fixStim = visual.TextStim(win, text = cross)
    fixStim.draw()
    win.flip()
    core.wait(1)

#Get random intervals for condition selection:
cond = random.sample(range(4), 4)
vid = random.sample(range(4), 4)

#Display Video !!!
def getVideo(win, mov):
    stim = visual.MovieStim3(win, mov)
    while stim.status != constants.FINISHED:
        stim.draw()
        win.flip()
   
    
#Using random numbers for video selection: 
def loadVideo(cond, vid):
    if cond == 0:
        if vid == 0:
            getVideo(win, "Stimuli/control_video1.mp4")
        elif vid == 1:
            getVideo(win, "Stimuli/control_video2.mp4")
        elif vid == 2:
            getVideo(win, "Stimuli/control_video3.mp4")
        elif vid == 3:
            getVideo(win, "Stimuli/control_video4.mp4")
    elif cond == 1:
        if vid == 0:
            getVideo(win, "Stimuli/noise_video1.mp4")
        elif vid == 1:
            getVideo(win, "Stimuli/noise_video1.mp4")
        elif vid == 2:
            getVideo(win, "Stimuli/noise_video1.mp4")
        elif vid == 3:
            getVideo(win, "Stimuli/noise_video1.mp4")
    elif cond == 2:
        if vid == 0:
            getVideo(win, "Stimuli/black_video1.mp4")
        elif vid == 1:
            getVideo(win, "Stimuli/black_video2.mp4")
        elif vid == 2:
            getVideo(win, "Stimuli/black_video3.mp4")
        elif vid == 3:
            getVideo(win, "Stimuli/black_video4.mp4")
    elif cond == 3:
        if vid == 0:
            getVideo(win, "Stimuli/blackcontrol_video1.mp4")
        elif vid == 1:
            getVideo(win, "Stimuli/blackcontrol_video1.mp4")
        elif vid == 2:
            getVideo(win, "Stimuli/blackcontrol_video1.mp4")
        elif vid == 3:
            getVideo(win, "Stimuli/blackcontrol_video1.mp4")



#Running functions!!!
personalData()
win = visual.Window(fullscr = True, color = [0,0,0])
msg(intruction)
fixcross(win)
loadVideo(cond[0], vid[0])
#function som gemmer text og condition/video

fixcross(win)
loadVideo(cond[1], vid[1])
#function som gemmer text og condition/video

fixcross(win)
loadVideo(cond[2], vid[2])
#function som gemmer text og condition/video

fixcross(win)
loadVideo(cond[3], vid[3])
#function som gemmer text og condition/video

#Create Log Files path
if not os.path.exists("logfiles"):
    os.makedirs("logfiles")
# define logfile name
logfile_name = "logfiles/logfile_{}.csv".format(date)
# save data to directory
logfile.to_csv(logfile_name)

