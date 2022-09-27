#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Emotional Stroop Task
# @ Kristian Tylén
# @ AU Cognitive Science 2017

# import modules
from psychopy import visual, event, core, data, gui
import random
import pandas as pd
import time

# Create popup information box
popup = gui.Dlg(title = "The Stroop Experiment")
popup.addField("Alias: ") # Empty box
popup.addField("Age: ")
popup.addField("Gender: ", choices=["Male", "Female", "Other" ]) # Dropdown menu
popup.show()
if popup.OK: # To retrieve data from popup window
    ID = popup.data
elif popup.Cancel: # To cancel the experiment if popup is closed
    core.quit()

#########################################################################################
################################## Stroop Task ##########################################
#########################################################################################


NUM_REP = 6 # repetitions * 15 trials

intro = '''
Welcome to the experiment!

This is a version of the "Stroop Task". Please read the instructions very carefully.

Use the keys r, g, b, and y to indicate if the words on the screen are printed
in red, green, blue or yellow ink. Ignore the meaning of the words.

Example: if you see the word "horse" printed in green ink, you should press 'g'.
Please try to be as fast as possible. 

If you make a mistake, please do not try to correct it by pushing a second key. Just wait for the next trial.  

press any key when you are ready...
'''

outro = '''
The experiment is done. Thank you for your participation!
'''

# define window
win = visual.Window(fullscr=True, color = 'Black')

# get date for unique logfile id
date = data.getDateStr() 

# define a stop watch
stopwatch = core.Clock()                                  

# colors
Colors = ['red', 'blue', 'green', 'yellow']
# prepare words

Stimuli = [{'word': 'happy', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.92}, {'word': 'party', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.20}, 
    {'word':'good', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 1.82},{'word': 'gift', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.34},
    {'word':'friend', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.28}, {'word': 'sad', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -2.99},
    {'word':'angry', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.05}, {'word': 'crime', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.17}, 
    {'word':'pain', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.27},{'word': 'distress', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -2.67},
    {'word':'chair', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.06}, {'word':'window', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.72}, 
    {'word':'stone', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': -0.33},{'word': 'speak', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.52}, 
    {'word':'truck','emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.10}] 

Stimuli = Stimuli*NUM_REP
random.shuffle(Stimuli)

# prepare pandas data frame for recorded data
columns = ['ID', 'Age', 'Gender', 'Word', 'Color', 'Emotional', 'Valence','Sentiment', 'Correct', 'Reaction_time']
STROOP_DATA = pd.DataFrame(columns=columns)

# define function that shows text
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 0.05) # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus
    event.waitKeys() # wait for any key press


# show instructions
msg(intro)

# loop through trials
for i in range(len(Stimuli)):
    # choose random color from list
    col = random.choice(Colors)
    # Word
    txt = Stimuli[i]['word']
    # prepare stimulus
    stimulus = visual.TextStim(win, text=txt, color = col)
    # draw stimulus
    stimulus.draw()
    win.flip()
    # reset stop watch
    stopwatch.reset()                              #reset the clock to 0:0:0 
    # record key press
    key = event.waitKeys(keyList = ['escape', 'r', 'g', 'b', 'y'])                  # wait for any key press
    # get reaction time at key press
    reaction_time = stopwatch.getTime()            # asks the stopwatch for the time since reset and save to the variable reation_time
    
    # check if response is correct
    if key[0] == col[0]:
        correct = 1
    elif key[0] != col[0]:
        correct = 0
    elif key[0] == 'escape':
        core.quit()
        win.close()
        
    # append all recorded data to the pandas DATA 
    STROOP_DATA = STROOP_DATA.append({
        'ID': ID[0],
        'Age': ID[1],
        'Gender': ID[2],
        'Word': txt,
        'Color': col,
        'Emotional': Stimuli[i]['emotional'],
        'Valence': Stimuli[i]['valence'],
        'Sentiment': Stimuli[i]['sentiment'],
        'Correct': correct, 
        'Reaction_time': reaction_time
        }, ignore_index=True)
    
    # show blank screen
    stimulus = visual.TextStim(win, '')
    stimulus.draw()
    win.flip()
    core.wait(0.5)

print(STROOP_DATA)

logfile_name = 'logfile_{}_{}.csv'.format(ID[0],date)
STROOP_DATA.to_csv(logfile_name)

msg(outro)
core.quit()
