# -*- coding: utf-8 -*-
# Emotion systems Exp 2021


"""
Structure: 
    SET VARIABLES
    GET PARTICIPANT INFO USING GUI
    SPECIFY TIMING AND MONITOR
    STIMULI
    OUTPUT
    FUNCTIONS FOR EXPERIMENTAL LOOP
    DISPLAY INTRO TEXT AND AWAIT SCANNER TRIGGER
    CALL FUNCTION RUNNING THE EXPERIMENTAL LOOP

"""

# Import the modules that we need in this script
from __future__ import division
from psychopy import core, visual, event, gui, data, monitors, event, prefs
from itertools import product, repeat
from random import sample, choices
import pandas as pd
import glob
import numpy as np
import os


"""
SET VARIABLES
"""
# Monitor parameters
MON_DISTANCE = 60  # Distance between subject's eyes and monitor 
MON_WIDTH = 20  # Width of your monitor in cm
MON_SIZE = [1000,1200]  # Pixel-dimensions of your monitor
FRAME_RATE=60 # Hz


"""
GET PARTICIPANT INFO USING GUI
"""
# Intro-dialogue. Get subject-id and other variables.
# Save input variables in "V" dictionary (V for "variables")
EXP_info= {'ID':'','gender':['male','female','other'],'handedness':['left','right'],'age':''}
if not gui.DlgFromDict(EXP_info, order=['ID','gender','handedness','age']).OK: # dialog box; order is a list of keys 
    core.quit()

"""
SPECIFY TIMING AND MONITOR
"""

# Clock and timer
clock = core.Clock()  # A clock wich will be used throughout the experiment to time events on a trial-per-trial basis (stimuli and reaction times).
date = data.getDateStr()
# Create psychopy window
my_monitor = monitors.Monitor('testMonitor', width=MON_WIDTH, distance=MON_DISTANCE)  # Create monitor object from the variables above. This is needed to control size of stimuli in degrees.
my_monitor.setSizePix(MON_SIZE)
win = visual.Window(monitor=my_monitor, units='deg', fullscr=True, allowGUI=False, color='black')  # Initiate psychopy Window as the object "win", using the myMon object from last line. Use degree as units!

# The image size and position using ImageStim, file info added in trial list sbelow.
stim_image = visual.ImageStim(win,  # you don't have to use new lines for each attribute, but sometime it's easier to read that way
     mask=None,
    pos=(0.0, 0.0),
    size=(14.0, 10.5),
    ori=1)

#Prepare Fixation cross
stim_fix = visual.TextStim(win, '+')#, height=FIX_HEIGHT)  # Fixation cross is just the character "+". Units are inherited from Window when not explicitly specified.


delay=(1*FRAME_RATE)
dur=int(2*FRAME_RATE) # duration in seconds multiplied by 60 Hz and made into integer
dur=3
global condition
condition='emotion_systems' #Just a variable. If the script can run several exp. then this can be called in GUI. Not relevant here.

"""
STIMULI
"""
#iMAGE FILES
img_neu = glob.glob("images_neutral/neutral_*") 
img_tp1 = glob.glob("images_type1_emotion/type1_*")
img_tp2 = glob.glob("images_type2_emotion/type2_*")

all_stimuli = img_neu + img_tp1 + img_tp2

catN=np.repeat('N',len(img_neu),axis=0)
catTp1=np.repeat('tp1',len(img_tp1),axis=0)
catTp2=np.repeat('tp2',len(img_tp2),axis=0)
categories=np.concatenate((catN, catTp1,catTp2), axis=0)


"""
RESPONSES
"""

############# RESPONSES AND OTHER COMMANDS ################################
# Relevant keys
KEYS_quit = ['escape','q']  # Keys that quits the experiment
KEYS_trigger = ['t','space'] # The MR scanner sends a "t" to notify that it is starting
KEYS_emotion =['e']#T is response key for target present.
KEYS_neutral =['w','r']#Y and R (present next to T) are response key for target absent. One can be used for righthanders, the other for lefthanders



############# OUTPUT LOGFILE ################################
# Define output folder

OUTPUT_folder = 'emotion_systems_data'  # Log is saved to this folder.

# If folder does not exist, do create it
if not os.path.exists(OUTPUT_folder):
    os.makedirs(OUTPUT_folder)

# Set filename

OUTPUT_filename = OUTPUT_folder + '/emo_sys_log_' + str(EXP_info['ID']) + '_' + date + '.csv'


############ FUNCTIONS TO RUN EXP ########################

""" FUNCTIONS FOR EXPERIMENTAL LOOP"""

def make_trial_list(condition):
# Factorial design
    global trial_list
    data={'img':all_stimuli,'categories':categories}
    trial_list=pd.DataFrame(data)
        #Randomize order
    trial_list = trial_list.sample(frac = 1).reset_index(drop=True)
    
    trial_list['Date']=date
    
    cols_ID = ['ID','gender','handedness','age']
    cols_resp = ['Time','onset','offset','duration_measured','response', 'emotion_judge','key_t', 'rt']
    trial_list = pd.concat([trial_list, pd.DataFrame(columns = cols_ID + cols_resp)], axis = 1)

    # Fill with ID info
    trial_list[cols_ID] = list(EXP_info.values())
    # Fill with blanks for later response info
    trial_list[cols_resp] = ''
    trial_list['duration_frames']=dur
    trial_list['delay_frames']=delay
    
    
#    for i, image in enumerate(all_stimuli): # images
#                    # Add a dictionary for every trial
#                    trial_list += [{
#                        'ID': EXP_info['ID'],
#                        'age': EXP_info['age'],
#                        'gender': EXP_info['gender'],
#                        'condition': condition,
#                        'img': image, #image file
#                        'onset':'' ,# a place to note onsets
#                        'offset': '',
#                        'duration_measured':'',
#                        'duration_frames': dur,
#                        'delay_frames': delay,
#                        'category': categories[i],                       
#                        'emotion_judge':'',                        
#                        'response': '',
#                        'key_t':'',
#                        'rt': '',
#                    }]
    # A variable with number of trials for later use
    global TRIAL_NUM
    TRIAL_NUM=trial_list.shape[0]
    trial_list['no'] = np.arange(TRIAL_NUM)+1
    return trial_list


##### Define the experimental loop!
def run_condition():
    """
    Runs a block of trials. This is the presentation of stimuli,
    collection of responses and saving the trial
    """
    
    # Make global changes to the dataframe  
    global trial_list
    global offset
    offset=0
    # Loop over trials
    for i in range(TRIAL_NUM):
        trial = trial_list.iloc[i]

    
        for frame in range(trial['delay_frames']):
            stim_fix.draw()
            win.flip()
        
        event.clearEvents(eventType='keyboard')# clear keyboard input to make sure that no responses are logged that do not belong to stimulus
     
        # Prepare image
        stim_image.image = trial['img']
        key=[]
        # Display image and monitor time
        xx=0
        time_flip=core.monotonicClock.getTime() #onset of stimulus
        stim_image.draw()
        win.flip()
        #wait for buttonpress (maximum wait is set in duration parameter)
        keys = event.waitKeys(keyList=('e','r','w','escape'), maxWait=dur, clearEvents=True,timeStamped=True)   
        offset = core.monotonicClock.getTime()  # offset of stimulus
        stim_fix.draw()
        win.flip()
        key=keys[0][0]
        time_key=keys[0][1]
        trial['response']=key
        trial['key_t']=time_key-exp_start
        trial['rt'] = time_key-time_flip
        #check what responses were
        if trial['response']=='e': trial['emotion_judge'] = 1
        elif trial['response']=='r' or 'w': trial['emotion_judge'] = 0
        if key in KEYS_quit:  # Look at first reponse [0]. Quit everything if quit-key was pressed
            trial_list.iloc[i]=trial
            trial_list.to_csv(OUTPUT_filename)
            win.close()
            core.quit()
            
        #Log values
        trial['onset']=time_flip-exp_start
        trial['offset'] = offset-exp_start
        trial['duration_measured']=offset-time_flip
    
    
        # Save trials to csv file
        trial_list.iloc[i]=trial
        trial_list.to_csv(OUTPUT_filename)
        key=[]
 
############# SET UP INSTRUCTIONS ########################
def msg(txt):
    message = visual.TextStim(win, pos =[0,0], text = txt, height = 0.75, alignHoriz = 'center') # create an instruction text
    message.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented # flip the screen to reveal the stimulus
    win.flip()

introText='''
WARNING: 
THIS EXPERIMENT CONTAINS DISTURBING IMAGES
PARTICIPATION IS STRICTLY VOLUNTARY
The task is to judge as fast as possible
if images contains/evokes emotions

Sometimes the emotion is obvious, sometimes subtle

Use your dominant hand
Press E as fast as possible
if the image is EMOTIONAL
Press R (righthanders) or W (lefthanders)
if the image is NEUTRAL.

Press SPACE to start the experiment'
'''
outroText='''
This is the end of the experiment. 

Thank you for your participation!

Press SPACE to exit.
'''

############# RUN THE EXPERIMENT ########################
# Setup the dataframe
make_trial_list(condition)

# Display instructions 
msg(introText)       

#Wait for scanner trigger "t" to continue
event.waitKeys(keyList = KEYS_trigger) 

# Start timer
exp_start = core.monotonicClock.getTime()

# Run the experimental loop
run_condition()

# save logfile
trial_list.to_csv(OUTPUT_filename)

# outro
msg(outroText)

# wait for key press
event.waitKeys(keyList = KEYS_trigger) 

# stop experiment
win.close()
core.quit()