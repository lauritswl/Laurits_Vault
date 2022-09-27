from psychopy import visual, event, core, gui, data
import glob
import random
import pandas as pd
from datetime import datetime
import os #to use os. fucntions

wd = os.getcwd()


def getVideo(win, location):
    stim = visual.MovieStim(win, location)
    stim.draw()
    win.flip
    event.waitKeys()

def video2(win,loc):
    globalClock = core.Clock()
    stim = visual.MovieStim(win, location)
    while globalClock.getTime()<(mov.duration+0.5):
        stim.draw()
        win.flip()



def fix():
    fixation.draw()
    win.flip()
    core.wait(2)

def intro(win):
    text = """ikke crash"""
    stim = visual.TextStim(win, text = wd)
    stim.draw()
    win.flip()
    event.waitKeys()

#getVideo(win,"test.mp4")


mywin = visual.Window([800,600], monitor="testMonitor", units="deg")
intro(win)


