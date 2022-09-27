# INTERFERENCE PILOT

from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']

# -*- coding: utf-8 -*-
# import libraries
from psychopy import core,visual,event,gui, sound
import random
import time
import datetime
import string
import os

TEXTHEIGHT=0.05 #height of text - 0.1 on my laptop
WRAPWIDTH=1.4 #text wrapping on instructions - 1.4 on my laptop
                
# function for instruction screen
def trialInst(window, inst):
    continuing = True
    textToShow = visual.TextStim(win=window, ori=0,  text=inst, 
    alignHoriz='center',font='Arial', pos=[0, 0], height=TEXTHEIGHT, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    textToShow.draw()
    window.flip()
    core.wait(1)
    while continuing:
        theseKeys = event.getKeys(keyList=['space', 'escape'])
        if len(theseKeys) > 0:
            if theseKeys == 'escape':
                window.close()
                core.quit()
            else:
                continuing = False
                window.flip()

# function for visual stimulus presentation
def visPres(window, patternSample):
    event.clearEvents('keyboard')
    receivedReturn = False
    #resp_times_cor = [] 
    #resp_times_false = []
    vis_i = 0
    #detected = 0
    true_pos = 0
    false_pos = 0
    polygons_series = []
    total_pres = 0
    timer = core.Clock()
    instructions = visual.TextStim(win=window, text = "Sit against the wall now! Press Q when you can't sit anymore and SPACE when you detect a 2-back match.", alignHoriz='center',font='Arial', pos=[0, 0.4], height=0.05, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    #stringToShow = visual.TextStim(win=window, text = str(round(int(timer.getTime()))), alignHoriz='center',font='Arial', pos=[0, 0.3], height=0.1, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    thisface = visual.ImageStim(window, image = patternSample[vis_i], pos = [0,0], size = [10, 10], units = 'cm')
    instructions.autoDraw = True
    #stringToShow.autoDraw = True
    thisface.autoDraw = True
    while timer.getTime() < 480:
        #stringToShow = visual.TextStim(win=window, text = numbers[i], alignHoriz='center',font='Arial', pos=[-0.3, 0.3], height=0.1, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
        if int(timer.getTime()) % 2 == 0:
            pre_clock = core.Clock()
            cur_trial = round(int(timer.getTime()))
        #    stringToShow.text = str(round(int(timer.getTime())))
            if patternSample[int(cur_trial/2)][-6:-4] in ['p1', 'p5','p9','13']:
                thisface.pos = [5, 2.5]
            elif patternSample[int(cur_trial/2)][-6:-4] in ['17','21','10','14']:
                thisface.pos = [-7.5, -5.5]
            elif patternSample[int(cur_trial/2)][-6:-4] in ['18','22','p4','11']:
                thisface.pos = [0, 3]
            elif patternSample[int(cur_trial/2)][-6:-4] in ['23','16','20','p8']:
                thisface.pos = [-1, -3]
            elif patternSample[int(cur_trial/2)][-6:-4] in ['p2','12','19','p7']:
                thisface.pos = [-7.5, 2]
            elif patternSample[int(cur_trial/2)][-6:-4] in ['p3','15','p6','24']:
                thisface.pos = [2, -3]
            thisface.image = patternSample[int(cur_trial/2)]
            if len(polygons_series) != 0:
                if polygons_series[-1] != patternSample[int(cur_trial/2)]:
                    polygons_series.append(patternSample[int(cur_trial/2)])
            else:
                polygons_series.append(patternSample[int(cur_trial/2)])
            #runOrBreak.draw()
            window.flip()
            #core.wait(1)
            theseKeys = event.getKeys(keyList=['space', 'escape', 'q']) # record keyboard presses
            if len(theseKeys) != 0:
                if theseKeys[0] == 'space': # if participant pressed space
                    trial_time = pre_clock.getTime()
                   # stringToShow.text = 'Pressed!'
                    #print('trial time: ' + str(trial_time))
                    window.flip()
                    total_pres += 1
                    if patternSample[int((cur_trial/2)-2)] == patternSample[int(cur_trial/2)]: # if current identical to current-2 = CORRECT
                        true_pos += 1
                        #resp_times_cor.append(trial_time)
                        event.clearEvents('keyboard')
                    else:
                        false_pos += 1 # otherwise INCORRECT
                        #resp_times_false.append(trial_time)
                        event.clearEvents('keyboard')
                if theseKeys[0] == 'q':
                    window.flip()
                 #   stringToShow.text = None
                 #   stringToShow.autoDraw = False
                    thisface.image = None
                    sit_duration = timer.getTime()
                    instructions.text = None
                    instructions.autoDraw = False
                    two_back_matches = 0
                    for i in range(len(polygons_series)):
                        if i < 2:
                            pass
                        if polygons_series[i] == polygons_series[i-2]:
                            two_back_matches += 1
                    return true_pos, false_pos, two_back_matches, total_pres, len(polygons_series), polygons_series, sit_duration
        else:
          #  stringToShow.text = str(round(int(timer.getTime())))
            #thisface.image = Non
            window.flip()
        window.flip()
    window.flip()
  #  stringToShow.text = None
   # stringToShow.autoDraw = False
    thisface.autoDraw = False
    sit_duration = timer.getTime()
    instructions.text = None
    instructions.autoDraw = False
    return true_pos, false_pos, two_back_matches, total_pres, len(polygons_series), polygons_series, sit_duration
    

def wordPres(window, wordSample):
    event.clearEvents('keyboard')
    resp_times_cor = [] 
    resp_times_false = []
    button_press_time = []
    #word_i = 0
    receivedReturn = False
    true_pos = 0
    false_pos = 0
    total_pres = 0
    word_series = []
    timer = core.Clock()
    pre_clock = time.time()
    instructions = visual.TextStim(win=window, text = "Sit against the wall now! Press Q when you can't sit anymore and SPACE when you detect a 2-back match.", alignHoriz='center',font='Arial', pos=[0, 0.4], height=0.05, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    instructions.autoDraw = True
    while timer.getTime() < 480: # change this when done debugging
        if int(timer.getTime()) % 2 == 0:
            cur_trial = round(int(timer.getTime()))
            thisword = sound.Sound(wordSample[int(cur_trial/2)])
            thisword.play()
           # stringToShow.text = str(round(int(timer.getTime())))
            window.flip()
            if len(word_series) != 0:
                if word_series[-1] != wordSample[int(cur_trial/2)]:
                    word_series.append(wordSample[int(cur_trial/2)])
            else:
                word_series.append(wordSample[int(cur_trial/2)])
            #core.wait(1)
            theseKeys = event.getKeys(keyList=['space', 'escape', 'q']) # record keyboard presses
            if len(theseKeys) != 0:
                if theseKeys[0] == 'space': # if participant pressed space
                    trial_time = time.time()
                    #button_press_time.append(int(pre_clock.getTime()))
                    trial_rt = (trial_time-pre_clock)-cur_trial
                    button_press_time.append(cur_trial)
                    #stringToShow.text = 'Pressed!'
                    #window.flip()
                    total_pres += 1
                    if wordSample[int((cur_trial/2)-3)] == wordSample[int((cur_trial/2)-1)]: #  has to be like this because the file changes right before switch
                        true_pos += 1
                        #word_i += 1
                        resp_times_cor.append(trial_rt)
                        event.clearEvents('keyboard')
                    else:
                        resp_times_false.append(trial_rt)
                        false_pos += 1 # otherwise INCORRECT
                        #word_i += 1
                        event.clearEvents('keyboard')
                if theseKeys[0] == 'q':
                        window.flip()
                        sit_duration = timer.getTime()
                        instructions.text = None
                        instructions.autoDraw = False
                        two_back_matches = 0
                        for i in range(len(word_series)):
                            if i < 2:
                                pass
                            if word_series[i] == word_series[i-2]:
                                two_back_matches += 1
                        return true_pos, false_pos, two_back_matches, total_pres, len(word_series), word_series, sit_duration
        else:
            #stringToShow.text = str(round(int(timer.getTime())))
            window.flip()
        window.flip()
    window.flip()
   # stringToShow.text = None
   # stringToShow.autoDraw = False
    core.wait(0.5)
    sit_duraction = timer.getTime()
    return true_pos, false_pos, two_back_matches, total_pres, len(word_series), word_series, sit_duration
    
def controlPres(window):
    event.clearEvents('keyboard')
    timer = core.Clock()
    instructions = visual.TextStim(win=window, text = "Sit against the wall! Press Q when you can't sit anymore.", alignHoriz='center',font='Arial', pos=[0, 0.4], height=0.05, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    #stringToShow = visual.TextStim(win=window, text = str(round(int(timer.getTime()))), alignHoriz='center',font='Arial', pos=[0, 0.3], height=0.1, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    instructions.autoDraw = True
    #stringToShow.autoDraw = True
    while timer.getTime() < 240:
     #   stringToShow.text = str(round(int(timer.getTime())))
        window.flip()
        theseKeys = event.getKeys(keyList=['space', 'escape', 'q']) # record keyboard presses
        if len(theseKeys) != 0:
            if theseKeys[0] == 'q': # if participant pressed space
                trial_duration = timer.getTime()
                #print('trial time: ' + str(trial_time))
                window.flip()
           #     stringToShow.text = None
            #    stringToShow.autoDraw = False
                instructions.text = None
                instructions.autoDraw = False
                return trial_duration
                
                
def perceivedExertion(window):
    event.clearEvents('keyboard')
    continuing = True
    instructions = visual.TextStim(win=window, text = "How exhausted do you feel on a scale from 1 (just regular being alive) to 9 (extremely exerted)? Press the relevant number button.", alignHoriz='center',font='Arial', pos=[0, 0.4], height=0.05, wrapWidth=WRAPWIDTH, color='white', colorSpace='rgb', opacity=1, depth=0.0)
    instructions.draw()
    window.flip()
    core.wait(1)
    while continuing:
        theseKeys = event.getKeys(keyList=['1', '2', '3','4','5','6','7','8','9'])
        if len(theseKeys) > 0:
            return theseKeys[0]
        

# function for creating random string of letters and numbers
def randomChars(stringLength):
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join(random.sample(lettersAndDigits, stringLength))
    
wordlist = ['pseudo_EN/w1.wav', 'pseudo_EN/w2.wav', 'pseudo_EN/w3.wav', 'pseudo_EN/w4.wav', 'pseudo_EN/w5.wav', 'pseudo_EN/w6.wav', 'pseudo_EN/w7.wav', 'pseudo_EN/w8.wav', 
                'pseudo_EN/w9.wav', 'pseudo_EN/w10.wav', 'pseudo_EN/w11.wav', 'pseudo_EN/w12.wav', 'pseudo_EN/w13.wav', 'pseudo_EN/w14.wav', 'pseudo_EN/w15.wav', 'pseudo_EN/w16.wav', 
                'pseudo_EN/w17.wav', 'pseudo_EN/w18.wav', 'pseudo_EN/w19.wav', 'pseudo_EN/w20.wav', 'pseudo_EN/w21.wav', 'pseudo_EN/w22.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w24.wav'] # 24 sound files of words
facelist = ['faces/p1.jpg', 'faces/p2.jpg', 'faces/p3.jpg', 'faces/p4.jpg', 'faces/p5.jpg', 'faces/p6.jpg', 'faces/p7.jpg', 'faces/p8.jpg', 
                'faces/p9.jpg', 'faces/p10.jpg', 'faces/p11.jpg', 'faces/p12.jpg', 'faces/p13.jpg', 'faces/p14.jpg', 'faces/p15.jpg', 'faces/p16.jpg', 
                'faces/p17.jpg', 'faces/p18.jpg', 'faces/p19.jpg', 'faces/p20.jpg', 'faces/p21.jpg', 'faces/p22.jpg', 'faces/p23.jpg', 'faces/p24.jpg'] # taken from https://www.thispersondoesnotexist.com
facelist = facelist*3 # repeat stimuli three times
wordlist = wordlist*3 # repeat stimuli three times

# polygons generated from: https://observablehq.com/d/74c576e556d9a0d9

# make fake-random lists for testing (four of each containing 30 items)
# there are 24 items, 6 should repeat
wordlists = [['pseudo_EN/w1.wav', 'pseudo_EN/w2.wav', 'pseudo_EN/w1.wav', 'pseudo_EN/w3.wav', 'pseudo_EN/w4.wav', 'pseudo_EN/w5.wav', 'pseudo_EN/w6.wav', 'pseudo_EN/w7.wav', 'pseudo_EN/w8.wav', 
                'pseudo_EN/w9.wav', 'pseudo_EN/w10.wav', 'pseudo_EN/w11.wav', 'pseudo_EN/w10.wav',  'pseudo_EN/w11.wav','pseudo_EN/w12.wav', 'pseudo_EN/w13.wav', 'pseudo_EN/w14.wav', 'pseudo_EN/w15.wav', 'pseudo_EN/w14.wav', 'pseudo_EN/w16.wav', 
                'pseudo_EN/w17.wav', 'pseudo_EN/w18.wav', 'pseudo_EN/w19.wav', 'pseudo_EN/w20.wav', 'pseudo_EN/w19.wav', 'pseudo_EN/w21.wav', 'pseudo_EN/w22.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w24.wav', 'pseudo_EN/w23.wav'],
                ['pseudo_EN/w11.wav', 'pseudo_EN/w8.wav', 'pseudo_EN/w20.wav', 'pseudo_EN/w8.wav','pseudo_EN/w20.wav','pseudo_EN/w1.wav', 'pseudo_EN/w15.wav', 'pseudo_EN/w5.wav', 'pseudo_EN/w3.wav', 'pseudo_EN/w10.wav','pseudo_EN/w3.wav', 'pseudo_EN/w4.wav', 
                'pseudo_EN/w19.wav', 'pseudo_EN/w17.wav', 'pseudo_EN/w9.wav', 'pseudo_EN/w6.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w13.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w21.wav', 'pseudo_EN/w2.wav', 'pseudo_EN/w22.wav', 
                'pseudo_EN/w18.wav', 'pseudo_EN/w16.wav','pseudo_EN/w18.wav', 'pseudo_EN/w14.wav', 'pseudo_EN/w24.wav', 'pseudo_EN/w7.wav', 'pseudo_EN/w12.wav', 'pseudo_EN/w7.wav'],
                ['pseudo_EN/w17.wav', 'pseudo_EN/w12.wav', 'pseudo_EN/w16.wav', 'pseudo_EN/w10.wav', 'pseudo_EN/w19.wav', 'pseudo_EN/w10.wav','pseudo_EN/w5.wav', 'pseudo_EN/w2.wav', 
                'pseudo_EN/w21.wav', 'pseudo_EN/w2.wav','pseudo_EN/w6.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w22.wav',  'pseudo_EN/w23.wav','pseudo_EN/w20.wav', 'pseudo_EN/w4.wav', 'pseudo_EN/w8.wav', 'pseudo_EN/w11.wav', 
                'pseudo_EN/w8.wav','pseudo_EN/w18.wav', 'pseudo_EN/w1.wav', 'pseudo_EN/w15.wav', 'pseudo_EN/w1.wav','pseudo_EN/w24.wav', 'pseudo_EN/w13.wav', 'pseudo_EN/w7.wav', 'pseudo_EN/w3.wav', 'pseudo_EN/w9.wav','pseudo_EN/w3.wav', 'pseudo_EN/w14.wav'],
                ['pseudo_EN/w4.wav', 'pseudo_EN/w8.wav','pseudo_EN/w4.wav', 'pseudo_EN/w7.wav', 'pseudo_EN/w24.wav', 'pseudo_EN/w16.wav', 'pseudo_EN/w1.wav', 'pseudo_EN/w22.wav', 'pseudo_EN/w1.wav','pseudo_EN/w22.wav','pseudo_EN/w9.wav', 
                'pseudo_EN/w21.wav', 'pseudo_EN/w11.wav', 'pseudo_EN/w10.wav', 'pseudo_EN/w3.wav', 'pseudo_EN/w13.wav','pseudo_EN/w3.wav', 'pseudo_EN/w2.wav', 'pseudo_EN/w12.wav', 'pseudo_EN/w20.wav', 
                'pseudo_EN/w14.wav', 'pseudo_EN/w17.wav', 'pseudo_EN/w19.wav', 'pseudo_EN/w17.wav','pseudo_EN/w18.wav', 'pseudo_EN/w5.wav', 'pseudo_EN/w23.wav', 'pseudo_EN/w6.wav', 'pseudo_EN/w23.wav','pseudo_EN/w15.wav']
                ]
facelists = [['polygons_2/p1.jpg', 'polygons_2/p2.jpg', 'polygons_2/p3.jpg', 'polygons_2/p2.jpg','polygons_2/p4.jpg', 'polygons_2/p5.jpg', 'polygons_2/p6.jpg', 'polygons_2/p5.jpg','polygons_2/p7.jpg', 'polygons_2/p8.jpg', 
                'polygons_2/p9.jpg', 'polygons_2/p10.jpg', 'polygons_2/p11.jpg', 'polygons_2/p12.jpg', 'polygons_2/p11.jpg','polygons_2/p13.jpg', 'polygons_2/p14.jpg', 'polygons_2/p15.jpg', 'polygons_2/p16.jpg', 'polygons_2/p15.jpg',
                'polygons_2/p17.jpg', 'polygons_2/p18.jpg', 'polygons_2/p19.jpg', 'polygons_2/p20.jpg', 'polygons_2/p19.jpg','polygons_2/p20.jpg','polygons_2/p21.jpg', 'polygons_2/p22.jpg', 'polygons_2/p23.jpg', 'polygons_2/p24.jpg'],
                ['polygons_2/p6.jpg', 'polygons_2/p12.jpg', 'polygons_2/p6.jpg','polygons_2/p8.jpg', 'polygons_2/p23.jpg', 'polygons_2/p15.jpg', 'polygons_2/p16.jpg', 'polygons_2/p15.jpg','polygons_2/p10.jpg', 'polygons_2/p24.jpg', 
                'polygons_2/p21.jpg', 'polygons_2/p14.jpg','polygons_2/p21.jpg', 'polygons_2/p1.jpg', 'polygons_2/p11.jpg', 'polygons_2/p4.jpg', 'polygons_2/p19.jpg', 'polygons_2/p5.jpg','polygons_2/p19.jpg', 'polygons_2/p20.jpg', 
                'polygons_2/p18.jpg', 'polygons_2/p17.jpg', 'polygons_2/p18.jpg','polygons_2/p7.jpg', 'polygons_2/p2.jpg', 'polygons_2/p3.jpg', 'polygons_2/p13.jpg', 'polygons_2/p22.jpg', 'polygons_2/p9.jpg','polygons_2/p22.jpg'],
                ['polygons_2/p6.jpg', 'polygons_2/p15.jpg', 'polygons_2/p10.jpg', 'polygons_2/p1.jpg','polygons_2/p10.jpg', 'polygons_2/p21.jpg', 'polygons_2/p18.jpg', 'polygons_2/p5.jpg', 'polygons_2/p18.jpg','polygons_2/p17.jpg', 
                'polygons_2/p7.jpg', 'polygons_2/p2.jpg', 'polygons_2/p23.jpg', 'polygons_2/p4.jpg','polygons_2/p23.jpg', 'polygons_2/p24.jpg', 'polygons_2/p20.jpg', 'polygons_2/p22.jpg', 'polygons_2/p19.jpg', 
                'polygons_2/p9.jpg', 'polygons_2/p19.jpg','polygons_2/p3.jpg', 'polygons_2/p14.jpg', 'polygons_2/p8.jpg', 'polygons_2/p11.jpg','polygons_2/p8.jpg', 'polygons_2/p16.jpg', 'polygons_2/p12.jpg', 'polygons_2/p13.jpg','polygons_2/p12.jpg'],
                ['polygons_2/p24.jpg', 'polygons_2/p16.jpg', 'polygons_2/p10.jpg', 'polygons_2/p16.jpg','polygons_2/p15.jpg', 'polygons_2/p11.jpg', 'polygons_2/p4.jpg', 'polygons_2/p9.jpg', 'polygons_2/p4.jpg','polygons_2/p7.jpg', 
                'polygons_2/p21.jpg', 'polygons_2/p14.jpg', 'polygons_2/p6.jpg', 'polygons_2/p14.jpg','polygons_2/p3.jpg', 'polygons_2/p17.jpg', 'polygons_2/p5.jpg', 'polygons_2/p18.jpg', 'polygons_2/p5.jpg','polygons_2/p19.jpg', 
                'polygons_2/p8.jpg', 'polygons_2/p22.jpg', 'polygons_2/p1.jpg', 'polygons_2/p20.jpg', 'polygons_2/p2.jpg', 'polygons_2/p23.jpg', 'polygons_2/p13.jpg', 'polygons_2/p23.jpg','polygons_2/p13.jpg','polygons_2/p12.jpg']
                ]

def runexp(ntrials):
    myWindow = visual.Window(size=(600, 800), units='height',fullscr=True, screen=0, allowGUI=True, allowStencil=False, monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb')
    trial_no = 1
    demographics = ','.join(list(expInfo.values()))
    if not os.path.exists('data_wallsit'):
        os.makedirs('data_wallsit')
    outputFile = open("data_wallsit/wallsit_{}.csv".format(datetime.datetime.now().strftime("%Y%m%d_polygons_" + str(demographics[0:3]))), "w")
    outputFile.write('participant,trial,distraction,true_pos,false_pos,total_matches, total_pressed,stim_count, stimuli, sit_duration, perceivedExertion\n')
    trialInst(myWindow, "Welcome! Today you'll be performing a visual or a verbal 2-back matching task while sitting against a wall. There will be three rounds in total, each lasting for as long as you are able to hold the wall-sit. Press SPACE when you're ready to begin.")
    condition_file = ['chars','grids','control']
    random.shuffle(wordlists)
    random.shuffle(facelists)
    random.shuffle(condition_file)
    w_index = 0
    v_index = 0
    for i in range(len(condition_file)):
        
        # find either 'g' (grid) or 'ch' (character) - historial reasons
        if condition_file[i].startswith('co'):
            trialInst(myWindow, "Now we'll just see how long you can do it without any interference. Place yourself sitting with your back against a wall with your knees bent at a right angle and the laptop within reach. Press SPACE when you're ready to begin.")
            condition = 'control'
            sit_duration = controlPres(myWindow)
            stimulus_list = 'NA'
            true_pos = 'NA'
            false_pos = 'NA'
            total_pressed = 'NA'
            stim_count = 'NA'
            total_matches = 'NA'
            stimuli = 'NA'
            #resp_times_cor = 'NA'
            #resp_times_false = 'NA'
            exertion = perceivedExertion(myWindow)
        if condition_file[i].startswith('g'):
            trialInst(myWindow, "In a moment, you'll start seeing some shapes on the screen one by one. Your task is to press SPACE when the pattern you see is the same as the one before the previous one. Place yourself sitting with your back against a wall with your knees bent at a right angle and the laptop within reach. Press SPACE when you're ready to begin.")
            flat_faces = [item for sublist in facelists for item in sublist]
            patternSample = flat_faces*2
            #pre_clock = core.Clock()
            true_pos, false_pos,total_matches, total_pressed, stim_count, stimuli, sit_duration = visPres(myWindow, patternSample)
            #trial_time = pre_clock.getTime()
            stimulus_list = patternSample
            #runOrBreak = 'SITTING'
            condition = 'visual'
            #v_index += 1
            exertion = perceivedExertion(myWindow)
        if condition_file[i].startswith('ch'):
            trialInst(myWindow, "In a moment, you'll start hearing some words one by one. Your task is to press SPACE when the word you hear is the same as the one before the previous one. Place yourself sitting with your back against a wall with your knees bent at a right angle and the laptop within reach. Press SPACE when you're ready to begin.")
            flat_words = [item for sublist in wordlists for item in sublist]
            wordSample = flat_words*2
            stimulus_list = wordSample
            #runOrBreak = 'SITTING'
            #pre_clock = core.Clock()
            true_pos, false_pos,total_matches, total_pressed, stim_count, stimuli, sit_duration = wordPres(myWindow, wordSample)
            #trial_time = pre_clock.getTime()
            condition = 'verbal'
            #w_index +=1
            exertion = perceivedExertion(myWindow)
        
        # then save that data
        
        breakText = "That was round number " + str(trial_no) + "! Take a break for five minutes and press SPACE when you're ready for the next round."
        trialInst(myWindow, breakText)
        outputFile = open("data_wallsit/wallsit_{}.csv".format(datetime.datetime.now().strftime("%Y%m%d_polygons_" + str(demographics[0:3]))), "a+")
        trial_data = demographics + ',' + str(trial_no) + ',' + str(condition) + ',' + str(true_pos) + ',' + str(false_pos) + ',' + str(total_matches) + ',' + str(total_pressed) + ','+ str(stim_count) + ','+ '_'.join(stimuli) + ',' + str(sit_duration) + ',' + str(exertion)+'\n' 
        outputFile.write(trial_data) # participant,trial,distraction,true_pos,false_pos,total_matches,total_pressed,stim_count,stimuli,sit_duration,perceivedExertion\
        outputFile.close()
        trial_no = trial_no + 1
        
    trialInst(myWindow, "That's it, well done! Thank you for participating!")
       
expInfo = {'Participant_ID':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title='Participant information')
if dlg.OK == False: 
    core.quit()  # user pressed cancel

event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

runexp(12)