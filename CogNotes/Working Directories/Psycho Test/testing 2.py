from psychopy import visual, event, core, gui, data
import glob
import random
import pandas as pd
from datetime import datetime
import os #to use os. fucntions 


instruction = psychopy.visual.TextStim(myWindow,color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['space', 'return']
keyboardKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = ''

def textbox


win = visual.Window(fullscr = True, color = [0,0,0])
fixcross(win)




txt2 = visual.TextStim(win, text = "Skriv den sætning du hørte og tryk 'enter'...", pos = [0, -0.5], height=.05)