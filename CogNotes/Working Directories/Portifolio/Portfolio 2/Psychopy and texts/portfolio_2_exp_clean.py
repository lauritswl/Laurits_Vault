### Portfolio 2 experiment ###

from psychopy import visual, core, event, data, gui
import pandas as pd 

box = gui.Dlg(title = "Choose condition")
box.addField("Condition", choices=["Control", "Salient"])
box.show()
if box.OK:
    Condition = box.data[0]
elif box.Cancel:
    core.quit()

box = gui.Dlg(title = "The reading experiment")
box.addField("Name: ") 
box.addField("Age: ") 
box.addField("Gender: ", choices=["Female", "Male", "Other" ])
box.show()
if box.OK:
    name = box.data[0]
    age = box.data[1]
    gender = box.data[2]
elif box.Cancel: 
    core.quit()

win = visual.Window(fullscr = True, color = "black")

stopwatch = core.Clock()

if Condition == "Control":
    f = open("control.txt")
else:
    f = open("salient.txt")

text = f.read()
f.close()

words = text.split()

columns = ['name', 'age', 'gender', 'reading_time', 'word', 'salience']
logfile = pd.DataFrame(columns=columns)

logfile_name = "logfiles/logfile_{}_{}.csv".format(name,Condition)

instruction = '''
Welcome to the Reading Experiment!

In a moment you will be presented with a short text, which you will read through one word at a time.
Press the space bar to move on to the next word. Read at your own pace.

Press any key to start the experiment 
'''

goodbye = '''
The experiment is done. Thank you for your participation!'''

def present_word(word):
    stimulus = visual.TextStim(win, word)
    stimulus.draw()
    stopwatch.reset()
    win.flip()
    keys = event.waitKeys(keyList = ["escape", "space"])
    reading_time = stopwatch.getTime()
    if keys == ["escape"]:
        core.quit()
    else:
        return reading_time

def salient(word):
    return word[0] == "*"

def msg(txt):
    message = visual.TextStim(win, text = txt, alignText = "left", height = 0.072)
    message.draw()
    win.flip()
    event.waitKeys()

msg(instruction)

for word in words:
    salience = salient(word)
    if salience:
        word = word[1:]    
    reading_time = present_word(word)
    
    logfile = logfile.append({
        'name': name,
        'age': age,
        'gender': gender,
        'word': word,
        'salience': salience,
        'reading_time': reading_time}, ignore_index = True)

    
logfile.to_csv(logfile_name)

msg(goodbye)