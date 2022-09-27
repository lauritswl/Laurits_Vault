from psychopy import visual, event, core, gui, data
import glob
import random
import pandas as pd
from datetime import datetime
import os 


clock = core.Clock()
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'æ', u'ø', u'å']

if not os.path.exists("logfiles"):
    os.makedirs("logfiles")

def personalData():
    introGui = gui.Dlg(title = "Sexperiment ;")
    introGui.addField("Participant ID:")
    introGui.addField("Age:")
    introGui.addField("Gender:", choices = ["Female", "Male", "Other"])
    introGui.addField("Condition:", choices = ["1", "2", "3"])
    introGui.show()
    if introGui.OK:
        [ID, age, gender, condition] = introGui.data
    else:
        core.quit()
    return ID, age, gender, condition
    
def textInput(win):
    text = ''
    while(True):
        stimulus = visual.TextStim(win, text = text)
        stimulus.draw()
        win.flip()
        keys = event.waitKeys()
        if keys == ["return"]:
            return text
        elif keys == ["backspace"]:
            text = text[:-1]
        elif keys == ["escape"]:
            core.quit()
        elif keys[0] in chars:
            text += keys[0]

def getWords(win):
    words = []
    clock.reset()
    while clock.getTime() < 20:
        words.append(textInput(win))
    return words

def presentTask(win, condition):
    prime_1 = ["flower", "tree"]
    prime_2 = ["carrot", "tomato"]
    
    word = "Garden"
    if condition == "1":
        hint = ""
    elif condition == "2":
        hint = "e.g. {}, {}...".format(prime_1[0], prime_1[1])
    elif condition == "3":
        hint = "e.g. {}, {}...".format(prime_2[0], prime_2[1])
    
    task = """
Please write words that you associate with the following word:
{}
{}
    """.format(word, hint)
    task_stim = visual.TextStim(win, text = task)
    task_stim.draw()
    win.flip()
    core.wait(5)

def intro(win):
    text = """Welcome to the Word Association Experiment. 
Your task is to list as many words as possible that you associate with the word that will be presented to you. Please try to spell the words correctly.
You will have 20 seconds to write as many words as you can. You can press enter to begin a new word.
Press the any key when you are ready to proceed."""
    stim = visual.TextStim(win, text = text)
    stim.draw()
    win.flip()
    event.waitKeys()
    

def byeBitch(win):
    text = "Thank you for your participation"
    stim = visual.TextStim(win, text = text)
    stim.draw()
    win.flip()
    core.wait(3)

ID, age, gender, condition = personalData()
win = visual.Window(fullscr = True, color = [0,0,0])
intro(win)
presentTask(win, condition)
words = getWords(win)
df = pd.DataFrame(columns = ["id", "age", "gender", "condition", "word"])
for word in words:
    df = df.append({
        "id" : ID,
        "age": age,
        "gender" : gender,
        "condition" : condition,
        "word" : word
    }, ignore_index = True)
df.to_csv("logfiles/res_{}.csv".format(ID), encoding='utf-8')
byeBitch(win)

