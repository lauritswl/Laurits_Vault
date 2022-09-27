from psychopy import data, visual, event, gui, core, sound
import random, os
import pandas as pd

#Initialize dialogue box
Dialoguebox = gui.Dlg(title = "Information")
Dialoguebox.addField("Participant alias:")
Dialoguebox.addField("Your native language:")
Dialoguebox.addField("Are you tone deaf?", choices=["No", "Yes", "Not sure"])
Dialoguebox.show()

#Save data from dialoguebox
if Dialoguebox.OK:
    ID = Dialoguebox.data[0]
    Language = Dialoguebox.data[1]
    ToneDeaf = Dialoguebox.data[2]
elif Dialoguebox.Cancel:
    core.quit()

# define window
win = visual.Window(fullscr = True, units = "height", color = "black")

# define stopwatch 
stopwatch = core.Clock()

# get date/time
timestamp = data.getDateStr()

# Making sure there is a logfile directory
if not os.path.exists("logfiles"):
    os.makedirs("logfiles")
    
# logfile
columns = ["timestamp", "ID", "Language", "ToneDeaf", "Stimulus", "Congruent", "Correct", "ReactionTime"]
logfile = pd.DataFrame(columns = columns)
logfilename = "logfiles/logfile_{}_{}.csv".format(ID,timestamp)

# text 
intro1 = '''
Welcome to this experiment investigating the spatial conceptualization of musical pitch.\n\nIn a moment you will be presented with pairs of two tones accompanied by a pair of visual stimuli.\n
Your task is to indicate - as fast as possible - if there is congruency or incongruency between the notes and the visual stimuli.\n\n\nPress space to continue...'''

intro2 = '''
The visual stimuli come in three sorts.\n\n
1) Either it consist of a bar being shown higher or lower at the screen\n\n
2) Or it consists of a sphere being bigger or smaller\n\n
3) Or it consists of a line being thinner or thicker\n\n
Congruency means that the musical note lower in pitch is presented together with the lower bar, the bigger sphere or the thicker line.\n
Incongruency means that the musical note lower in pitch is presented together with the higher bar, the smaller sphere or the thinner line, etc.\n\n
Press space to continue...'''

intro3 = '''
If you think the relation between sound and visual stimuli is congruent, press the right arrow key as fast as possible.\n
If you think the relation between sound and visual stimuli is incongruent, press the left arrow key as fast as possible.\n\n\n
Press space to proceed to the training trial...'''  

intro4 = '''
This was an example of the high/low visual stimuli.\n\n 
If you find that the visual stimuli were congruent with the pitch of the sound (i.e. the lower note was presented simultaneously with the lower visual bar), press the right arrow key.\n
If you find that the visual stimuli were incongruent with the pitch of the sound (the lower note was presented simultaneously with the higher visual bar), press the left arrow key.\n\n
When you have made your choice, you will proceed to the next training round...'''

intro5 = '''
This was an example of the big/small visual stimuli.\n\n 
If you find that the visual stimuli were congruent with the pitch of the sound (i.e. the lower note was presented simultaneously with the bigger sphere), press the right arrow key.\n
If you find that the visual stimuli were incongruent with the pitch of the sound (the lower note was presented simultaneously with the smaller sphere), press the left arrow key.\n\n
When you have made your choice, you will proceed to the next training round...'''

intro6 = '''
This was an example of the thick/thin visual stimuli.\n\n 
If you find that the visual stimuli were congruent with the pitch of the sound (i.e. the lower note was presented simultaneously with the thicker line), press the right arrow key.\n
If you find that the visual stimuli were incongruent with the pitch of the sound (the lower note was presented simultaneously with the thinner line), press the left arrow key.\n\n
When you have made your choice, you will proceed to the next training round...'''

intro7 = '''
Good job! Now we are ready to start the real experiment. Remember we will be recording your reaction times, so try to be as fast and accurate as possible. However, mind that you can only respond after the sound has stopped.\n\n
Press any key to proceed to the first trial...'''

outro = '''
The experiment is done. Thank you very much for your participation!'''

# tone stimuli
ToneStim = ['C', 'E', 'G']
Octaves = [[3,5], [4,6], [5,7]]

# visual stimuli
Height = visual.Line(win, start = [0, -0.3], end = [0, 0.3], lineWidth = 30, lineColor = "white")
MarkerH = visual.Line(win, start = [-0.03, 0.25], end = [0.03, 0.25], lineWidth = 15, lineColor = "white")
MarkerL = visual.Line(win, start = [-0.03, -0.25], end = [0.03, -0.25], lineWidth = 15, lineColor = "white")
Big = visual.Circle(win, radius = 0.3, lineWidth = 15, lineColor = "white")
Small = visual.Circle(win, radius = 0.05, lineWidth = 15, lineColor = "white")
Thick = visual.Rect(win, height = 0.5, width = 0.2, fillColor = "white")
Thin = visual.Rect(win, height = 0.5, width = 0.01, fillColor = "white")
message = visual.TextStim(win, text = "", height = 0.02, alignText = "left")

def msg(txt):
    message.text = txt
    message.draw()
    win.flip()
    event.waitKeys()

def ShowTrial(stim,number):
    if stim['stimulus'] == 'height':
        Height.draw()
    if number == 1:
        stim['stim1'].draw()
    else:
        stim['stim2'].draw()

height_stim = []
for congruent in [1,0]:
    for t in ToneStim:
        for o in Octaves:
            if congruent == 1:
                h = [MarkerL,MarkerH]
            else:
                h = [MarkerH,MarkerL]
            height_stim += [{
                "stimulus":"height",
                "congruent": congruent,
                "tone": t,
                "octave1": o[0],
                "octave2": o[1],
                "stim1": h[0],
                "stim2": h[1]}]
                
size_stim = []
for congruent in [1,0]:
    for t in ToneStim:
        for o in Octaves:
            if congruent == 1:
                s = [Big,Small]
            else:
                s = [Small,Big]
            size_stim += [{
                "stimulus":"size",
                "congruent": congruent,
                "tone": t,
                "octave1": o[0],
                "octave2": o[1],
                "stim1": s[0],
                "stim2": s[1]}]                    

thickness_stim = []
for congruent in [1,0]:
    for t in ToneStim:
        for o in Octaves:
            if congruent == 1:
                th = [Thick,Thin]
            else:
                th = [Thin,Thick]
            thickness_stim += [{
                "stimulus":"thickness",
                "congruent": congruent,
                "tone": t,
                "octave1": o[0],
                "octave2": o[1],
                "stim1": th[0],
                "stim2": th[1]}]      

stimuli = height_stim + size_stim + thickness_stim
random.shuffle(stimuli)

#### introduction #####

msg(intro1)
msg(intro2)
msg(intro3)

#### training trial ####

tone = sound.Sound("E", octave = 4, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Height.draw()
MarkerL.draw()
win.flip()
core.wait(0.8)

tone = sound.Sound("E", octave =6, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Height.draw()
MarkerH.draw()
win.flip()
core.wait(0.7)

msg(intro4)

tone = sound.Sound("G", octave =3, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Big.draw()
win.flip()
core.wait(0.8)

tone = sound.Sound("G", octave =5, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Small.draw()
win.flip()
core.wait(0.7)

msg(intro5)

tone = sound.Sound("C", octave =5, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Thick.draw()
win.flip()
core.wait(0.8)

tone = sound.Sound("C", octave =7, sampleRate=44100, secs=0.8, stereo=True)
tone.play()
Thin.draw()
win.flip()
core.wait(0.7)

msg(intro6)

msg(intro7)

for stim in stimuli:
    ShowTrial(stim,1)
    tone = sound.Sound(stim['tone'], octave=stim['octave1'], sampleRate=44100, secs=0.4, stereo=True)
    tone.play()
    win.flip()
    core.wait(0.5)
    ShowTrial(stim,2)
    tone = sound.Sound(stim['tone'], octave=stim['octave2'], sampleRate=44100, secs=0.4, stereo=True)
    tone.play()
    win.flip()
    core.wait(0.4)
    win.flip()
    stopwatch.reset()
    key = event.waitKeys(keyList = "right,left,escape")[0]
    reaction_time = stopwatch.getTime()
    
    if key == "escape":
        logfile.to_csv(logfilename)
        core.quit()
    elif (key == "right" and stim["congruent"] == 1) or (key == "left" and stim["congruent"] == 0):
        correct = 1
    else:
        correct = 0
    
    logfile = logfile.append({
        "timestamp": timestamp,
        "ID": ID, 
        "Language": Language, 
        "ToneDeaf": ToneDeaf, 
        "Stimulus": stim['stimulus'], 
        "Congruent": stim['congruent'],
        "Correct": correct,
        "ReactionTime": reaction_time}, ignore_index = True)
    
    core.wait(0.5)

logfile.to_csv(logfilename)
 
msg(outro)