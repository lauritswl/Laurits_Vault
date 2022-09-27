from psychopy import visual, event, core, gui, data, constants
import glob
import random
import pandas as pd
from datetime import datetime
import os #to use os. fucntions

 #Allow æøå
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
 #Core Clock
clock = core.Clock()
 #Get date for logfile names
date = data.getDateStr()

# Condition to text
def condtotext(cond):
    global ConditionText
    if cond == 0:
        ConditionText = "No noise with video"
    elif cond == 1:
        ConditionText = "Noise with video"
    elif cond == 2:
        ConditionText = "No noise without video"
    elif cond == 3:
        ConditionText = "Noise without video"

# make sure that there is a logfile directory and otherwise make one
if not os.path.exists("logfiles"):
    os.makedirs("logfiles")

# define dialogue box (important that this happens before you define window)
def personalData(): 
    global ID
    global AGE
    global GENDER
    global FLUENCY
    global CONSENT
    box = gui.Dlg(title = "Sentence understanding experiment")
    box.addField("Identifikation: ") 
    box.addField("Alder: ")
    box.addField("Køn: ", choices=["Kvinde", "Mand", "Andet"])
    box.addField("Taler du flydende dansk?", choices=["Ja", "Nej"])
    box.addField("Giver du samtykke?", choices=["Ja", "Nej"])
    box.show()
    if box.OK: # To retrieve data from popup window
        ID = box.data[0]
        AGE = box.data[1]
        GENDER = box.data[2]
        FLUENCY = box.data[3]
        CONSENT = box.data[4]
    elif box.Cancel: # To cancel the experiment if popup is closed
        core.quit()

# define logfile 
# prepare pandas data frame for recorded data
columns = ['time_stamp','consent' 'id', 'age', 'gender', 'fluent_in_danish', 'video', 'condition', 'text']
logfile = pd.DataFrame(columns=columns)

#run log data
personalData()

# Introduction Text
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

# function for showing text and waiting for key press
def msg(txt):
    message = visual.TextStim(win, text = txt, alignText = "left", height = 0.05)
    message.draw()
    win.flip()
    event.waitKeys()

#text from participant
def getWords():
    
    txt2 = visual.TextStim(win, text = "Skriv den sætning du hørte og tryk 'enter'...", pos = [0, -0.5], height=.05)
    txt2.draw()
    win.flip()
    
    # set up text field
    text = visual.TextStim(win, text='')
    endTrial = False
    while not endTrial:
        response = event.waitKeys()
        
        if response:
            # If backspace, delete last character
            if response[0] == 'backspace':
                text.setText(text.text[:-1])
                
            # Insert space
            elif response[0] == 'space':
                text.setText(text.text + ' ')
    
            # Else if a letter, append to text:
            elif response[0] in chars:
                text.setText(text.text + response[0])
    
            # If esc key - end experiment
            elif response[0] == 'escape': 
                endTrial = True
            
            # If return, save word to panda and reset input
            elif response[0] == 'return':
                endTrial = True
            
        # Display updated text
        txt2.draw()
        text.draw()
        win.flip()
    
    return text.text
    text.setText(text='')

#Fixation cross
def fixcross(win):
    cross = """+"""
    fixStim = visual.TextStim(win, text = cross)
    fixStim.draw()
    win.flip()
    core.wait(0.2)

#Display Video !!!
def show_stim(mov):
    stim = visual.MovieStim3(win, mov)
    while stim.status != constants.FINISHED:
        stim.draw()
        win.flip()

#Get random intervals for condition selection:
cond = random.sample(range(4), 4)
vid = random.sample(range(4), 4)

#Using random numbers for video selection: 
def loadVideo(cond, vid):
    if cond == 0:
        if vid == 0:
            show_stim("videos/control/control_video1.mp4")
        elif vid == 1:
            show_stim("videos/control/control_video2.mp4")
        elif vid == 2:
            show_stim("videos/control/control_video3.mp4")
        elif vid == 3:
            show_stim("videos/control/control_video4.mp4")
    elif cond == 1:
        if vid == 0:
            show_stim("videos/noise/noise_video1.mp4")
        elif vid == 1:
            show_stim("videos/noise/noise_video2.mp4")
        elif vid == 2:
            show_stim("videos/noise/noise_video3.mp4")
        elif vid == 3:
            show_stim("videos/noise/noise_video4.mp4")
    elif cond == 2:
        if vid == 0:
            show_stim("videos/black/black_video1.mp4")
        elif vid == 1:
            show_stim("videos/black/black_video2.mp4")
        elif vid == 2:
            show_stim("videos/black/black_video3.mp4")
        elif vid == 3:
            show_stim("videos/black/black_video4.mp4")
    elif cond == 3:
        if vid == 0:
            show_stim("videos/blackcontrol/blackcontrol_video1.mp4")
        elif vid == 1:
            show_stim("videos/blackcontrol/blackcontrol_video2.mp4")
        elif vid == 2:
            show_stim("videos/blackcontrol/blackcontrol_video3.mp4")
        elif vid == 3:
            show_stim("videos/blackcontrol/blackcontrol_video4.mp4")

#function for saving log data
def log(vid):
    logfile = logfile.append({
        'time_stamp': date,
        'consent': CONSENT,
        'id': ID,
        'age': AGE,
        'gender': GENDER,
        'fluent_in_danish': FLUENCY,
        'video': vid, 
        'condition': ConditionText,
        'text': words}, ignore_index = True)         
    core.wait(0.5)


#Running functions!!!

win = visual.Window(fullscr = True, color = "black")
msg(instruction)

#Video 1
fixcross(win)
loadVideo(cond[0], vid[0])
condtotext(cond[0])
words = getWords()
logfile = logfile.append({
    'time_stamp': date,
    'consent': CONSENT,
    'id': ID,
    'age': AGE,
    'gender': GENDER,
    'fluent_in_danish': FLUENCY,
    'video': vid[0], 
    'condition': ConditionText,
    'text': words}, ignore_index = True)         
core.wait(0.5)


#Video 2
fixcross(win)
loadVideo(cond[1], vid[1])
condtotext(cond[1])
words = getWords()
logfile = logfile.append({
    'time_stamp': date,
    'consent': CONSENT,
    'id': ID,
    'age': AGE,
    'gender': GENDER,
    'fluent_in_danish': FLUENCY,
    'video': vid[1], 
    'condition': ConditionText,
    'text': words}, ignore_index = True)         
core.wait(0.5)


#Video 3
fixcross(win)
loadVideo(cond[2], vid[2])
condtotext(cond[2])
words = getWords()
logfile = logfile.append({
    'time_stamp': date,
    'consent': CONSENT,
    'id': ID,
    'age': AGE,
    'gender': GENDER,
    'fluent_in_danish': FLUENCY,
    'video': vid[2], 
    'condition': ConditionText,
    'text': words}, ignore_index = True)         
core.wait(0.5)


#Video 4
fixcross(win)
loadVideo(cond[3], vid[3])
condtotext(cond[3])
words = getWords()
logfile = logfile.append({
    'time_stamp': date,
    'consent': CONSENT,
    'id': ID,
    'age': AGE,
    'gender': GENDER,
    'fluent_in_danish': FLUENCY,
    'video': vid[3], 
    'condition': ConditionText,
    'text': words}, ignore_index = True)         
core.wait(0.5)


# save data to directory
logfile_name = "logfiles/logfile_{}_{}.csv".format(ID,date)
logfile.to_csv(logfile_name)

msg(goodbye)




#Click here when starting script


