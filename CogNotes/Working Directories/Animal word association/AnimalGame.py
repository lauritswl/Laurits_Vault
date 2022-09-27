
# The Animal Association Game
# Allows the participant to write animal names and press enter while recording reaction times with high precision 
# @Kristian Tylén
# @Aarhus University 2020

# import modules
from psychopy import visual, event, core, gui, data
import pandas as pd
import os 


# gui requesting participant info
participant_id = gui.Dlg(title='The Animal Association Game') 
participant_id.addText('Subject Info')
participant_id.addField('ID: ')
participant_id.addField('Time (in sec): ')
participant_id.show()
if participant_id.OK:
    ID = participant_id.data

# set time
t = int(ID[1])

# Set up window
win = visual.Window(fullscr = True, color = "black")

# set up text field
text = visual.TextStim(win, text='')

# word entry function 
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'æ', u'ø', u'å']

# get timestamp for unique logfile id
date = data.getDateStr()

# Making sure there is a logfile directory
if not os.path.exists("logfiles"):
    os.makedirs("logfiles")
    
# set up log file
DATA = pd.DataFrame(columns = ["time_stamp", "global_time", "ID", "word", "reaction_time"])
filename = "logfiles/logfile_{}_{}.csv".format(ID[0], date)

# set relative logfile path 
path = "logfiles/"

# txt
intro_txt = """
You now have {} seconds to name as many different {} as you can think of. 
Enter the animal names one-by-one and press enter after each one.\n\nPress any key when you are ready to start.""".format(t, "animals")

goodbye = "The experiment is done. Thank you for your participation"

intro_txt2 = visual.TextStim(win, text = "Type an animal name and press enter...", pos = [0, -0.5], height=.05)

#display info text and wait for key press
def info(string, wait = 0):
    disp = visual.TextStim(win, text=string, height=.08)
    disp.draw()
    win.flip()
    core.wait(wait)
    event.waitKeys()
    win.flip()
    
def show_text(word): 
    W = visual.TextStim(win, text=word, height=.08)
    W.draw()
    win.flip()
    core.wait(1.5)

###################################################
############### Start Experiment ##################
###################################################

info(intro_txt)

# initialize abort option
endTrial = False
# initialize clock
clock = core.Clock()
stopwatch = core.Clock()

intro_txt2.draw()
win.flip()

while not endTrial:
    # Wait for response...
    if clock.getTime() > t:
        endTrial = True
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

        # If return, save word to panda and reset input
        elif response[0] == 'return':
            DATA = DATA.append({
            'time_stamp': date,
            'global_time': clock.getTime(),
            'ID': ID[0],
            'word': text.text,
            'reaction_time': stopwatch.getTime()
            }, ignore_index = True)
            
            text.setText(text='')
            stopwatch.reset()
        
        # If esc key - end experiment
        elif response[0] == 'escape': 
            endTrial = True
        
    # Display updated text
    intro_txt2.draw()
    text.draw()
    win.flip()

info(goodbye, 2)

DATA.to_csv(filename)

win.close()
print(DATA)
