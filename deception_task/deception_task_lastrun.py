#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Mon Mar 22 12:56:29 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'deception_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jiarong/Dropbox/FYP_Jia Rong/Deception Task/psychopy/deception_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
back1 = visual.Rect(
    win=win, name='back1',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Deception Task!\n\nPress “space” to begin!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keywelcome = keyboard.Keyboard()

# Initialize components for Routine "ID_Entry"
ID_EntryClock = core.Clock()
back2 = visual.Rect(
    win=win, name='back2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textID = visual.TextStim(win=win, name='textID',
    text='Please enter your subject ID below:\n\n(Press “space” to continue)',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
IDRESPONSE = visual.TextBox2(
     win, text='ID', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='black', borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='IDRESPONSE',
     autoLog=True,
)
key_respID = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
back3 = visual.Rect(
    win=win, name='back3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textinstructions = visual.TextStim(win=win, name='textinstructions',
    text='In this task, you will be answering questions created using information from the Autobiographical Memory Questionnaire you completed earlier.\n\nThe task consists of 2 conditions in total, and each condition will require you to answer a total of 40 items. There will be a short break between the 2 conditions.\n\n(Press “space” to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_instruct = keyboard.Keyboard()

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
back19 = visual.Rect(
    win=win, name='back19',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textinstruct2 = visual.TextStim(win=win, name='textinstruct2',
    text='For each item, you will be presented with a question. You will see instructions on screen to either tell the truth or lie to it, and you will have to respond to the question verbally in the screen following that.\n\nPlease reply to the questions in complete sentences. When you are done replying, press “space” to continue to the next question.\n\nThe next screen will show you some examples.\n\n(Press “space” to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
back4 = visual.Rect(
    win=win, name='back4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textexample = visual.TextStim(win=win, name='textexample',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textexample1 = visual.TextStim(win=win, name='textexample1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
buttonexample = visual.Rect(
    win=win, name='buttonexample',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textans = visual.TextStim(win=win, name='textans',
    text='Press “space” to begin answering',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ExampleResponse"
ExampleResponseClock = core.Clock()
back12 = visual.Rect(
    win=win, name='back12',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
videotest = visual.Rect(
    win=win, name='videotest',units='norm', 
    width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
    ori=0, pos=(0, 0.08),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
buttontest = visual.Rect(
    win=win, name='buttontest',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
text_button = visual.TextStim(win=win, name='text_button',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Trials"
TrialsClock = core.Clock()
back20 = visual.Rect(
    win=win, name='back20',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_trial = visual.TextStim(win=win, name='text_trial',
    text='In the next few slides, we will present to you the same example questions you saw previously. \n\nHowever, it is now your turn to try answering them to get the hang of it!\n\n(Press “space” to begin!)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resptrial = keyboard.Keyboard()

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
back4 = visual.Rect(
    win=win, name='back4',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textexample = visual.TextStim(win=win, name='textexample',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textexample1 = visual.TextStim(win=win, name='textexample1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
buttonexample = visual.Rect(
    win=win, name='buttonexample',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textans = visual.TextStim(win=win, name='textans',
    text='Press “space” to begin answering',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Trials_Response"
Trials_ResponseClock = core.Clock()
back21 = visual.Rect(
    win=win, name='back21',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
videotrial = visual.Rect(
    win=win, name='videotrial',units='norm', 
    width=(1.5, 1.5)[0], height=(1.5, 1.5)[1],
    ori=0, pos=(0, 0.08),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
buttontrial = visual.Rect(
    win=win, name='buttontrial',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
texttrialcontinue = visual.TextStim(win=win, name='texttrialcontinue',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_trialresp = visual.TextStim(win=win, name='text_trialresp',
    text='(How would you respond?)',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_trial = keyboard.Keyboard()

# Initialize components for Routine "Social_Condition"
Social_ConditionClock = core.Clock()
back5 = visual.Rect(
    win=win, name='back5',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textsocial = visual.TextStim(win=win, name='textsocial',
    text='SOCIAL CONDITION\n\nDuring this condition, an examiner will be observing you through a live video chat. He will be rating your response as you reply verbally to determine if you are telling the truth or lying. \n\n(Press “space” to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_ressoc = keyboard.Keyboard()

# Initialize components for Routine "SocialInstruct2"
SocialInstruct2Clock = core.Clock()
back18 = visual.Rect(
    win=win, name='back18',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textsocioal2 = visual.TextStim(win=win, name='textsocioal2',
    text='Please respond to each item in complete sentences.\n\nYou have a maximum of 10 seconds to give your response for each item. If you complete it earlier, you can press “space” to continue.\n\n(Press “space” to begin!)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_ressoc2 = keyboard.Keyboard()

# Initialize components for Routine "Social"
SocialClock = core.Clock()
back6 = visual.Rect(
    win=win, name='back6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
truth1_text = visual.TextStim(win=win, name='truth1_text',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
truth1_instruction = visual.TextStim(win=win, name='truth1_instruction',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
buttoncon = visual.Rect(
    win=win, name='buttoncon',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textanswer = visual.TextStim(win=win, name='textanswer',
    text='Press “space” to begin answering',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
sensor2 = visual.Rect(
    win=win, name='sensor2',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
keysocial = keyboard.Keyboard()

# Initialize components for Routine "Connecting"
ConnectingClock = core.Clock()
back9 = visual.Rect(
    win=win, name='back9',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textconnecting = visual.TextStim(win=win, name='textconnecting',
    text='Waiting for interviewer …',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sensor3 = visual.Rect(
    win=win, name='sensor3',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "Response_S"
Response_SClock = core.Clock()
back7 = visual.Rect(
    win=win, name='back7',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
button = visual.Rect(
    win=win, name='button',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
textbutton = visual.TextStim(win=win, name='textbutton',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textvideo = visual.TextStim(win=win, name='textvideo',
    text='Live Video Chat',
    font='Arial',
    pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
sensor = visual.Rect(
    win=win, name='sensor',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
key_response = keyboard.Keyboard()

# Initialize components for Routine "Disconnecting"
DisconnectingClock = core.Clock()
back10 = visual.Rect(
    win=win, name='back10',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textdisconnecting = visual.TextStim(win=win, name='textdisconnecting',
    text='Interviewer is rating your answer …',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sensor4 = visual.Rect(
    win=win, name='sensor4',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "SubjectiveR"
SubjectiveRClock = core.Clock()
back22 = visual.Rect(
    win=win, name='back22',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textsubjresp = visual.TextStim(win=win, name='textsubjresp',
    text='How do you think your response was rated?',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyrespsubj = keyboard.Keyboard()
SubjectiveResponse = visual.Slider(win=win, name='SubjectiveResponse',
    size=(1, 0.03), pos=(0, 0), units=None,
    labels=["Lie", "Truth"], ticks=(0, 1),
    granularity=0, style=['rating', 'triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-3)
textsubjcon = visual.TextStim(win=win, name='textsubjcon',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
back8 = visual.Rect(
    win=win, name='back8',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textbreak = visual.TextStim(win=win, name='textbreak',
    text='\n\nYou have completed the Social Condition!\n\n\nPlease inform the experimenter NOW. \n\n\nYou can now take a break before continuing to the Polygraph Condition.\n\n\n\n\n\n\n\n\n(Press “space” when you are instructed to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_respbreak = keyboard.Keyboard()

# Initialize components for Routine "Polygraph_Condition"
Polygraph_ConditionClock = core.Clock()
back13 = visual.Rect(
    win=win, name='back13',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='POLYGRAPH CONDITION\n\nDuring this condition, you will not be observed by an examiner. Instead, a bio-device will rate your physiological responses to determine whether you told a truth or a lie. \n\n(Press “space” to continue)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resppoly = keyboard.Keyboard()

# Initialize components for Routine "PolyInstruct2"
PolyInstruct2Clock = core.Clock()
back17 = visual.Rect(
    win=win, name='back17',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textpolyinstruct = visual.TextStim(win=win, name='textpolyinstruct',
    text='For this condition, you will be viewing your own physiological signals instead of a live video chat.\n\nPlease respond to each item in complete sentences.\n\nYou have a maximum of 10 seconds to give your response for each item. If you complete it earlier, you can press “space” to continue.\n\n(Press “space” to begin!)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resppoly2 = keyboard.Keyboard()

# Initialize components for Routine "Social"
SocialClock = core.Clock()
back6 = visual.Rect(
    win=win, name='back6',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
truth1_text = visual.TextStim(win=win, name='truth1_text',
    text='default text',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
truth1_instruction = visual.TextStim(win=win, name='truth1_instruction',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
buttoncon = visual.Rect(
    win=win, name='buttoncon',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textanswer = visual.TextStim(win=win, name='textanswer',
    text='Press “space” to begin answering',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
sensor2 = visual.Rect(
    win=win, name='sensor2',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
keysocial = keyboard.Keyboard()

# Initialize components for Routine "BioConnect"
BioConnectClock = core.Clock()
back15 = visual.Rect(
    win=win, name='back15',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textbioconnect = visual.TextStim(win=win, name='textbioconnect',
    text='Bio-device is connecting …',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sensor5 = visual.Rect(
    win=win, name='sensor5',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "Response_P"
Response_PClock = core.Clock()
back14 = visual.Rect(
    win=win, name='back14',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
button1 = visual.Rect(
    win=win, name='button1',
    width=(0.6, 0.05)[0], height=(0.6, 0.05)[1],
    ori=0, pos=(0, -0.42),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
buttont = visual.TextStim(win=win, name='buttont',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.42), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sensor1 = visual.Rect(
    win=win, name='sensor1',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
textpoly = visual.TextStim(win=win, name='textpoly',
    text='Bio-Device',
    font='Arial',
    pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resresp = keyboard.Keyboard()

# Initialize components for Routine "BioDisConnect"
BioDisConnectClock = core.Clock()
back16 = visual.Rect(
    win=win, name='back16',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
textbiodisconnect = visual.TextStim(win=win, name='textbiodisconnect',
    text='Bio-device is rating your scores …',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sensor6 = visual.Rect(
    win=win, name='sensor6',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.77, -0.47),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "SubjectiveR"
SubjectiveRClock = core.Clock()
back22 = visual.Rect(
    win=win, name='back22',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textsubjresp = visual.TextStim(win=win, name='textsubjresp',
    text='How do you think your response was rated?',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
keyrespsubj = keyboard.Keyboard()
SubjectiveResponse = visual.Slider(win=win, name='SubjectiveResponse',
    size=(1, 0.03), pos=(0, 0), units=None,
    labels=["Lie", "Truth"], ticks=(0, 1),
    granularity=0, style=['rating', 'triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-3)
textsubjcon = visual.TextStim(win=win, name='textsubjcon',
    text='Press “space” to continue',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
back11 = visual.Rect(
    win=win, name='back11',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
textend = visual.TextStim(win=win, name='textend',
    text='Congrats! You have completed the Polygraph Condition!\n\nThis concludes the behavioural test on the Deception Task.\n\nPlease inform the experimenter NOW.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
keywelcome.keys = []
keywelcome.rt = []
_keywelcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [back1, text, keywelcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back1* updates
    if back1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back1.frameNStart = frameN  # exact frame index
        back1.tStart = t  # local t and not account for scr refresh
        back1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back1, 'tStartRefresh')  # time at next scr refresh
        back1.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *keywelcome* updates
    waitOnFlip = False
    if keywelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keywelcome.frameNStart = frameN  # exact frame index
        keywelcome.tStart = t  # local t and not account for scr refresh
        keywelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keywelcome, 'tStartRefresh')  # time at next scr refresh
        keywelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keywelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keywelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keywelcome.status == STARTED and not waitOnFlip:
        theseKeys = keywelcome.getKeys(keyList=['space'], waitRelease=False)
        _keywelcome_allKeys.extend(theseKeys)
        if len(_keywelcome_allKeys):
            keywelcome.keys = _keywelcome_allKeys[-1].name  # just the last key pressed
            keywelcome.rt = _keywelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ID_Entry"-------
continueRoutine = True
# update component parameters for each repeat
key_respID.keys = []
key_respID.rt = []
_key_respID_allKeys = []
# keep track of which components have finished
ID_EntryComponents = [back2, textID, IDRESPONSE, key_respID]
for thisComponent in ID_EntryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ID_EntryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ID_Entry"-------
while continueRoutine:
    # get current time
    t = ID_EntryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ID_EntryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back2* updates
    if back2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back2.frameNStart = frameN  # exact frame index
        back2.tStart = t  # local t and not account for scr refresh
        back2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back2, 'tStartRefresh')  # time at next scr refresh
        back2.setAutoDraw(True)
    
    # *textID* updates
    if textID.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textID.frameNStart = frameN  # exact frame index
        textID.tStart = t  # local t and not account for scr refresh
        textID.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textID, 'tStartRefresh')  # time at next scr refresh
        textID.setAutoDraw(True)
    
    # *IDRESPONSE* updates
    if IDRESPONSE.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IDRESPONSE.frameNStart = frameN  # exact frame index
        IDRESPONSE.tStart = t  # local t and not account for scr refresh
        IDRESPONSE.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IDRESPONSE, 'tStartRefresh')  # time at next scr refresh
        IDRESPONSE.setAutoDraw(True)
    
    # *key_respID* updates
    waitOnFlip = False
    if key_respID.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_respID.frameNStart = frameN  # exact frame index
        key_respID.tStart = t  # local t and not account for scr refresh
        key_respID.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_respID, 'tStartRefresh')  # time at next scr refresh
        key_respID.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_respID.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_respID.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_respID.status == STARTED and not waitOnFlip:
        theseKeys = key_respID.getKeys(keyList=['space'], waitRelease=False)
        _key_respID_allKeys.extend(theseKeys)
        if len(_key_respID_allKeys):
            key_respID.keys = _key_respID_allKeys[-1].name  # just the last key pressed
            key_respID.rt = _key_respID_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ID_EntryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ID_Entry"-------
for thisComponent in ID_EntryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IDRESPONSE.text',IDRESPONSE.text)
IDRESPONSE.reset()
# the Routine "ID_Entry" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_instruct.keys = []
key_instruct.rt = []
_key_instruct_allKeys = []
# keep track of which components have finished
InstructionsComponents = [back3, textinstructions, key_instruct]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back3* updates
    if back3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back3.frameNStart = frameN  # exact frame index
        back3.tStart = t  # local t and not account for scr refresh
        back3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back3, 'tStartRefresh')  # time at next scr refresh
        back3.setAutoDraw(True)
    
    # *textinstructions* updates
    if textinstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textinstructions.frameNStart = frameN  # exact frame index
        textinstructions.tStart = t  # local t and not account for scr refresh
        textinstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textinstructions, 'tStartRefresh')  # time at next scr refresh
        textinstructions.setAutoDraw(True)
    
    # *key_instruct* updates
    waitOnFlip = False
    if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruct.frameNStart = frameN  # exact frame index
        key_instruct.tStart = t  # local t and not account for scr refresh
        key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
        key_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_instruct_allKeys.extend(theseKeys)
        if len(_key_instruct_allKeys):
            key_instruct.keys = _key_instruct_allKeys[-1].name  # just the last key pressed
            key_instruct.rt = _key_instruct_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instructions2Components = [back19, textinstruct2, key_resp_3]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back19* updates
    if back19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back19.frameNStart = frameN  # exact frame index
        back19.tStart = t  # local t and not account for scr refresh
        back19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back19, 'tStartRefresh')  # time at next scr refresh
        back19.setAutoDraw(True)
    
    # *textinstruct2* updates
    if textinstruct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textinstruct2.frameNStart = frameN  # exact frame index
        textinstruct2.tStart = t  # local t and not account for scr refresh
        textinstruct2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textinstruct2, 'tStartRefresh')  # time at next scr refresh
        textinstruct2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sample.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Example"-------
    continueRoutine = True
    # update component parameters for each repeat
    textexample.setText(question)
    textexample1.setText(condition)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ExampleComponents = [back4, textexample, textexample1, buttonexample, textans, key_resp]
    for thisComponent in ExampleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Example"-------
    while continueRoutine:
        # get current time
        t = ExampleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back4* updates
        if back4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back4.frameNStart = frameN  # exact frame index
            back4.tStart = t  # local t and not account for scr refresh
            back4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back4, 'tStartRefresh')  # time at next scr refresh
            back4.setAutoDraw(True)
        
        # *textexample* updates
        if textexample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textexample.frameNStart = frameN  # exact frame index
            textexample.tStart = t  # local t and not account for scr refresh
            textexample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textexample, 'tStartRefresh')  # time at next scr refresh
            textexample.setAutoDraw(True)
        
        # *textexample1* updates
        if textexample1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textexample1.frameNStart = frameN  # exact frame index
            textexample1.tStart = t  # local t and not account for scr refresh
            textexample1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textexample1, 'tStartRefresh')  # time at next scr refresh
            textexample1.setAutoDraw(True)
        
        # *buttonexample* updates
        if buttonexample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonexample.frameNStart = frameN  # exact frame index
            buttonexample.tStart = t  # local t and not account for scr refresh
            buttonexample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonexample, 'tStartRefresh')  # time at next scr refresh
            buttonexample.setAutoDraw(True)
        
        # *textans* updates
        if textans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textans.frameNStart = frameN  # exact frame index
            textans.tStart = t  # local t and not account for scr refresh
            textans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textans, 'tStartRefresh')  # time at next scr refresh
            textans.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Example"-------
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ExampleResponse"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    text_4.setText(respond)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    ExampleResponseComponents = [back12, videotest, buttontest, text_button, text_4, key_resp_2]
    for thisComponent in ExampleResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExampleResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ExampleResponse"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ExampleResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExampleResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back12* updates
        if back12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back12.frameNStart = frameN  # exact frame index
            back12.tStart = t  # local t and not account for scr refresh
            back12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back12, 'tStartRefresh')  # time at next scr refresh
            back12.setAutoDraw(True)
        if back12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back12.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                back12.tStop = t  # not accounting for scr refresh
                back12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back12, 'tStopRefresh')  # time at next scr refresh
                back12.setAutoDraw(False)
        
        # *videotest* updates
        if videotest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            videotest.frameNStart = frameN  # exact frame index
            videotest.tStart = t  # local t and not account for scr refresh
            videotest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(videotest, 'tStartRefresh')  # time at next scr refresh
            videotest.setAutoDraw(True)
        if videotest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > videotest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                videotest.tStop = t  # not accounting for scr refresh
                videotest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(videotest, 'tStopRefresh')  # time at next scr refresh
                videotest.setAutoDraw(False)
        
        # *buttontest* updates
        if buttontest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttontest.frameNStart = frameN  # exact frame index
            buttontest.tStart = t  # local t and not account for scr refresh
            buttontest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttontest, 'tStartRefresh')  # time at next scr refresh
            buttontest.setAutoDraw(True)
        if buttontest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buttontest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                buttontest.tStop = t  # not accounting for scr refresh
                buttontest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttontest, 'tStopRefresh')  # time at next scr refresh
                buttontest.setAutoDraw(False)
        
        # *text_button* updates
        if text_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_button.frameNStart = frameN  # exact frame index
            text_button.tStart = t  # local t and not account for scr refresh
            text_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_button, 'tStartRefresh')  # time at next scr refresh
            text_button.setAutoDraw(True)
        if text_button.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_button.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_button.tStop = t  # not accounting for scr refresh
                text_button.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_button, 'tStopRefresh')  # time at next scr refresh
                text_button.setAutoDraw(False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExampleResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ExampleResponse"-------
    for thisComponent in ExampleResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_3'


# ------Prepare to start Routine "Trials"-------
continueRoutine = True
# update component parameters for each repeat
key_resptrial.keys = []
key_resptrial.rt = []
_key_resptrial_allKeys = []
# keep track of which components have finished
TrialsComponents = [back20, text_trial, key_resptrial]
for thisComponent in TrialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Trials"-------
while continueRoutine:
    # get current time
    t = TrialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back20* updates
    if back20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back20.frameNStart = frameN  # exact frame index
        back20.tStart = t  # local t and not account for scr refresh
        back20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back20, 'tStartRefresh')  # time at next scr refresh
        back20.setAutoDraw(True)
    
    # *text_trial* updates
    if text_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_trial.frameNStart = frameN  # exact frame index
        text_trial.tStart = t  # local t and not account for scr refresh
        text_trial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_trial, 'tStartRefresh')  # time at next scr refresh
        text_trial.setAutoDraw(True)
    
    # *key_resptrial* updates
    waitOnFlip = False
    if key_resptrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resptrial.frameNStart = frameN  # exact frame index
        key_resptrial.tStart = t  # local t and not account for scr refresh
        key_resptrial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resptrial, 'tStartRefresh')  # time at next scr refresh
        key_resptrial.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resptrial.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resptrial.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resptrial.status == STARTED and not waitOnFlip:
        theseKeys = key_resptrial.getKeys(keyList=['space'], waitRelease=False)
        _key_resptrial_allKeys.extend(theseKeys)
        if len(_key_resptrial_allKeys):
            key_resptrial.keys = _key_resptrial_allKeys[-1].name  # just the last key pressed
            key_resptrial.rt = _key_resptrial_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trials"-------
for thisComponent in TrialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Trials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trialsloop = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sample.xlsx'),
    seed=None, name='Trialsloop')
thisExp.addLoop(Trialsloop)  # add the loop to the experiment
thisTrialsloop = Trialsloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsloop.rgb)
if thisTrialsloop != None:
    for paramName in thisTrialsloop:
        exec('{} = thisTrialsloop[paramName]'.format(paramName))

for thisTrialsloop in Trialsloop:
    currentLoop = Trialsloop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsloop.rgb)
    if thisTrialsloop != None:
        for paramName in thisTrialsloop:
            exec('{} = thisTrialsloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Example"-------
    continueRoutine = True
    # update component parameters for each repeat
    textexample.setText(question)
    textexample1.setText(condition)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ExampleComponents = [back4, textexample, textexample1, buttonexample, textans, key_resp]
    for thisComponent in ExampleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Example"-------
    while continueRoutine:
        # get current time
        t = ExampleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back4* updates
        if back4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back4.frameNStart = frameN  # exact frame index
            back4.tStart = t  # local t and not account for scr refresh
            back4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back4, 'tStartRefresh')  # time at next scr refresh
            back4.setAutoDraw(True)
        
        # *textexample* updates
        if textexample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textexample.frameNStart = frameN  # exact frame index
            textexample.tStart = t  # local t and not account for scr refresh
            textexample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textexample, 'tStartRefresh')  # time at next scr refresh
            textexample.setAutoDraw(True)
        
        # *textexample1* updates
        if textexample1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textexample1.frameNStart = frameN  # exact frame index
            textexample1.tStart = t  # local t and not account for scr refresh
            textexample1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textexample1, 'tStartRefresh')  # time at next scr refresh
            textexample1.setAutoDraw(True)
        
        # *buttonexample* updates
        if buttonexample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttonexample.frameNStart = frameN  # exact frame index
            buttonexample.tStart = t  # local t and not account for scr refresh
            buttonexample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttonexample, 'tStartRefresh')  # time at next scr refresh
            buttonexample.setAutoDraw(True)
        
        # *textans* updates
        if textans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textans.frameNStart = frameN  # exact frame index
            textans.tStart = t  # local t and not account for scr refresh
            textans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textans, 'tStartRefresh')  # time at next scr refresh
            textans.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Example"-------
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trials_Response"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    key_trial.keys = []
    key_trial.rt = []
    _key_trial_allKeys = []
    # keep track of which components have finished
    Trials_ResponseComponents = [back21, videotrial, buttontrial, texttrialcontinue, text_trialresp, key_trial]
    for thisComponent in Trials_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trials_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trials_Response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Trials_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trials_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back21* updates
        if back21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back21.frameNStart = frameN  # exact frame index
            back21.tStart = t  # local t and not account for scr refresh
            back21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back21, 'tStartRefresh')  # time at next scr refresh
            back21.setAutoDraw(True)
        if back21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back21.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                back21.tStop = t  # not accounting for scr refresh
                back21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back21, 'tStopRefresh')  # time at next scr refresh
                back21.setAutoDraw(False)
        
        # *videotrial* updates
        if videotrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            videotrial.frameNStart = frameN  # exact frame index
            videotrial.tStart = t  # local t and not account for scr refresh
            videotrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(videotrial, 'tStartRefresh')  # time at next scr refresh
            videotrial.setAutoDraw(True)
        if videotrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > videotrial.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                videotrial.tStop = t  # not accounting for scr refresh
                videotrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(videotrial, 'tStopRefresh')  # time at next scr refresh
                videotrial.setAutoDraw(False)
        
        # *buttontrial* updates
        if buttontrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttontrial.frameNStart = frameN  # exact frame index
            buttontrial.tStart = t  # local t and not account for scr refresh
            buttontrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttontrial, 'tStartRefresh')  # time at next scr refresh
            buttontrial.setAutoDraw(True)
        if buttontrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buttontrial.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                buttontrial.tStop = t  # not accounting for scr refresh
                buttontrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttontrial, 'tStopRefresh')  # time at next scr refresh
                buttontrial.setAutoDraw(False)
        
        # *texttrialcontinue* updates
        if texttrialcontinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texttrialcontinue.frameNStart = frameN  # exact frame index
            texttrialcontinue.tStart = t  # local t and not account for scr refresh
            texttrialcontinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texttrialcontinue, 'tStartRefresh')  # time at next scr refresh
            texttrialcontinue.setAutoDraw(True)
        if texttrialcontinue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > texttrialcontinue.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                texttrialcontinue.tStop = t  # not accounting for scr refresh
                texttrialcontinue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(texttrialcontinue, 'tStopRefresh')  # time at next scr refresh
                texttrialcontinue.setAutoDraw(False)
        
        # *text_trialresp* updates
        if text_trialresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_trialresp.frameNStart = frameN  # exact frame index
            text_trialresp.tStart = t  # local t and not account for scr refresh
            text_trialresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_trialresp, 'tStartRefresh')  # time at next scr refresh
            text_trialresp.setAutoDraw(True)
        if text_trialresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_trialresp.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_trialresp.tStop = t  # not accounting for scr refresh
                text_trialresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_trialresp, 'tStopRefresh')  # time at next scr refresh
                text_trialresp.setAutoDraw(False)
        
        # *key_trial* updates
        waitOnFlip = False
        if key_trial.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_trial.frameNStart = frameN  # exact frame index
            key_trial.tStart = t  # local t and not account for scr refresh
            key_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_trial, 'tStartRefresh')  # time at next scr refresh
            key_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_trial.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                key_trial.tStop = t  # not accounting for scr refresh
                key_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_trial, 'tStopRefresh')  # time at next scr refresh
                key_trial.status = FINISHED
        if key_trial.status == STARTED and not waitOnFlip:
            theseKeys = key_trial.getKeys(keyList=['space'], waitRelease=False)
            _key_trial_allKeys.extend(theseKeys)
            if len(_key_trial_allKeys):
                key_trial.keys = _key_trial_allKeys[-1].name  # just the last key pressed
                key_trial.rt = _key_trial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trials_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trials_Response"-------
    for thisComponent in Trials_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 0 repeats of 'Trialsloop'


# ------Prepare to start Routine "Social_Condition"-------
continueRoutine = True
# update component parameters for each repeat
key_ressoc.keys = []
key_ressoc.rt = []
_key_ressoc_allKeys = []
# keep track of which components have finished
Social_ConditionComponents = [back5, textsocial, key_ressoc]
for thisComponent in Social_ConditionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Social_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Social_Condition"-------
while continueRoutine:
    # get current time
    t = Social_ConditionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Social_ConditionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back5* updates
    if back5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back5.frameNStart = frameN  # exact frame index
        back5.tStart = t  # local t and not account for scr refresh
        back5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back5, 'tStartRefresh')  # time at next scr refresh
        back5.setAutoDraw(True)
    
    # *textsocial* updates
    if textsocial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textsocial.frameNStart = frameN  # exact frame index
        textsocial.tStart = t  # local t and not account for scr refresh
        textsocial.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textsocial, 'tStartRefresh')  # time at next scr refresh
        textsocial.setAutoDraw(True)
    
    # *key_ressoc* updates
    waitOnFlip = False
    if key_ressoc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ressoc.frameNStart = frameN  # exact frame index
        key_ressoc.tStart = t  # local t and not account for scr refresh
        key_ressoc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ressoc, 'tStartRefresh')  # time at next scr refresh
        key_ressoc.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ressoc.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ressoc.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ressoc.status == STARTED and not waitOnFlip:
        theseKeys = key_ressoc.getKeys(keyList=['space'], waitRelease=False)
        _key_ressoc_allKeys.extend(theseKeys)
        if len(_key_ressoc_allKeys):
            key_ressoc.keys = _key_ressoc_allKeys[-1].name  # just the last key pressed
            key_ressoc.rt = _key_ressoc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Social_ConditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Social_Condition"-------
for thisComponent in Social_ConditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Social_Condition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SocialInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
key_ressoc2.keys = []
key_ressoc2.rt = []
_key_ressoc2_allKeys = []
# keep track of which components have finished
SocialInstruct2Components = [back18, textsocioal2, key_ressoc2]
for thisComponent in SocialInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SocialInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SocialInstruct2"-------
while continueRoutine:
    # get current time
    t = SocialInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SocialInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back18* updates
    if back18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back18.frameNStart = frameN  # exact frame index
        back18.tStart = t  # local t and not account for scr refresh
        back18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back18, 'tStartRefresh')  # time at next scr refresh
        back18.setAutoDraw(True)
    
    # *textsocioal2* updates
    if textsocioal2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textsocioal2.frameNStart = frameN  # exact frame index
        textsocioal2.tStart = t  # local t and not account for scr refresh
        textsocioal2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textsocioal2, 'tStartRefresh')  # time at next scr refresh
        textsocioal2.setAutoDraw(True)
    
    # *key_ressoc2* updates
    waitOnFlip = False
    if key_ressoc2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_ressoc2.frameNStart = frameN  # exact frame index
        key_ressoc2.tStart = t  # local t and not account for scr refresh
        key_ressoc2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_ressoc2, 'tStartRefresh')  # time at next scr refresh
        key_ressoc2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_ressoc2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_ressoc2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_ressoc2.status == STARTED and not waitOnFlip:
        theseKeys = key_ressoc2.getKeys(keyList=['space'], waitRelease=False)
        _key_ressoc2_allKeys.extend(theseKeys)
        if len(_key_ressoc2_allKeys):
            key_ressoc2.keys = _key_ressoc2_allKeys[-1].name  # just the last key pressed
            key_ressoc2.rt = _key_ressoc2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SocialInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SocialInstruct2"-------
for thisComponent in SocialInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "SocialInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo["participant"] + '_social_questions.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Social"-------
    continueRoutine = True
    # update component parameters for each repeat
    truth1_text.setText(question
)
    truth1_instruction.setText(condition)
    keysocial.keys = []
    keysocial.rt = []
    _keysocial_allKeys = []
    # keep track of which components have finished
    SocialComponents = [back6, truth1_text, truth1_instruction, buttoncon, textanswer, sensor2, keysocial]
    for thisComponent in SocialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SocialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Social"-------
    while continueRoutine:
        # get current time
        t = SocialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SocialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back6* updates
        if back6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back6.frameNStart = frameN  # exact frame index
            back6.tStart = t  # local t and not account for scr refresh
            back6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back6, 'tStartRefresh')  # time at next scr refresh
            back6.setAutoDraw(True)
        
        # *truth1_text* updates
        if truth1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            truth1_text.frameNStart = frameN  # exact frame index
            truth1_text.tStart = t  # local t and not account for scr refresh
            truth1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(truth1_text, 'tStartRefresh')  # time at next scr refresh
            truth1_text.setAutoDraw(True)
        
        # *truth1_instruction* updates
        if truth1_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            truth1_instruction.frameNStart = frameN  # exact frame index
            truth1_instruction.tStart = t  # local t and not account for scr refresh
            truth1_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(truth1_instruction, 'tStartRefresh')  # time at next scr refresh
            truth1_instruction.setAutoDraw(True)
        
        # *buttoncon* updates
        if buttoncon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttoncon.frameNStart = frameN  # exact frame index
            buttoncon.tStart = t  # local t and not account for scr refresh
            buttoncon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttoncon, 'tStartRefresh')  # time at next scr refresh
            buttoncon.setAutoDraw(True)
        
        # *textanswer* updates
        if textanswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textanswer.frameNStart = frameN  # exact frame index
            textanswer.tStart = t  # local t and not account for scr refresh
            textanswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textanswer, 'tStartRefresh')  # time at next scr refresh
            textanswer.setAutoDraw(True)
        
        # *sensor2* updates
        if sensor2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor2.frameNStart = frameN  # exact frame index
            sensor2.tStart = t  # local t and not account for scr refresh
            sensor2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor2, 'tStartRefresh')  # time at next scr refresh
            sensor2.setAutoDraw(True)
        if sensor2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor2.tStop = t  # not accounting for scr refresh
                sensor2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor2, 'tStopRefresh')  # time at next scr refresh
                sensor2.setAutoDraw(False)
        
        # *keysocial* updates
        waitOnFlip = False
        if keysocial.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            keysocial.frameNStart = frameN  # exact frame index
            keysocial.tStart = t  # local t and not account for scr refresh
            keysocial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keysocial, 'tStartRefresh')  # time at next scr refresh
            keysocial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keysocial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keysocial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keysocial.status == STARTED and not waitOnFlip:
            theseKeys = keysocial.getKeys(keyList=['space'], waitRelease=False)
            _keysocial_allKeys.extend(theseKeys)
            if len(_keysocial_allKeys):
                keysocial.keys = _keysocial_allKeys[-1].name  # just the last key pressed
                keysocial.rt = _keysocial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SocialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Social"-------
    for thisComponent in SocialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('sensor2.started', sensor2.tStartRefresh)
    trials_2.addData('sensor2.stopped', sensor2.tStopRefresh)
    # the Routine "Social" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Connecting"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter_connecting = np.random.uniform(0.7, 1.5, 1)
    
    # keep track of which components have finished
    ConnectingComponents = [back9, textconnecting, sensor3]
    for thisComponent in ConnectingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ConnectingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Connecting"-------
    while continueRoutine:
        # get current time
        t = ConnectingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ConnectingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back9* updates
        if back9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back9.frameNStart = frameN  # exact frame index
            back9.tStart = t  # local t and not account for scr refresh
            back9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back9, 'tStartRefresh')  # time at next scr refresh
            back9.setAutoDraw(True)
        if back9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back9.tStartRefresh + jitter_connecting-frameTolerance:
                # keep track of stop time/frame for later
                back9.tStop = t  # not accounting for scr refresh
                back9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back9, 'tStopRefresh')  # time at next scr refresh
                back9.setAutoDraw(False)
        
        # *textconnecting* updates
        if textconnecting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textconnecting.frameNStart = frameN  # exact frame index
            textconnecting.tStart = t  # local t and not account for scr refresh
            textconnecting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textconnecting, 'tStartRefresh')  # time at next scr refresh
            textconnecting.setAutoDraw(True)
        if textconnecting.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textconnecting.tStartRefresh + jitter_connecting-frameTolerance:
                # keep track of stop time/frame for later
                textconnecting.tStop = t  # not accounting for scr refresh
                textconnecting.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textconnecting, 'tStopRefresh')  # time at next scr refresh
                textconnecting.setAutoDraw(False)
        
        # *sensor3* updates
        if sensor3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor3.frameNStart = frameN  # exact frame index
            sensor3.tStart = t  # local t and not account for scr refresh
            sensor3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor3, 'tStartRefresh')  # time at next scr refresh
            sensor3.setAutoDraw(True)
        if sensor3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor3.tStop = t  # not accounting for scr refresh
                sensor3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor3, 'tStopRefresh')  # time at next scr refresh
                sensor3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ConnectingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Connecting"-------
    for thisComponent in ConnectingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('sensor3.started', sensor3.tStartRefresh)
    trials_2.addData('sensor3.stopped', sensor3.tStopRefresh)
    # the Routine "Connecting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response_S"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    videoresponse = visual.MovieStim3(
        win=win, name='videoresponse',units='norm', 
        noAudio = False,
        filename=video,
        ori=0, pos=(0, 0.08), opacity=1,
        loop=False,
        size=(1.6, 1.5),
        depth=-1.0,
        )
    key_response.keys = []
    key_response.rt = []
    _key_response_allKeys = []
    # keep track of which components have finished
    Response_SComponents = [back7, videoresponse, button, textbutton, textvideo, sensor, key_response]
    for thisComponent in Response_SComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response_SClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response_S"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Response_SClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response_SClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back7* updates
        if back7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back7.frameNStart = frameN  # exact frame index
            back7.tStart = t  # local t and not account for scr refresh
            back7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back7, 'tStartRefresh')  # time at next scr refresh
            back7.setAutoDraw(True)
        if back7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                back7.tStop = t  # not accounting for scr refresh
                back7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back7, 'tStopRefresh')  # time at next scr refresh
                back7.setAutoDraw(False)
        
        # *videoresponse* updates
        if videoresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            videoresponse.frameNStart = frameN  # exact frame index
            videoresponse.tStart = t  # local t and not account for scr refresh
            videoresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(videoresponse, 'tStartRefresh')  # time at next scr refresh
            videoresponse.setAutoDraw(True)
        if videoresponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > videoresponse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                videoresponse.tStop = t  # not accounting for scr refresh
                videoresponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(videoresponse, 'tStopRefresh')  # time at next scr refresh
                videoresponse.setAutoDraw(False)
        
        # *button* updates
        if button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            button.setAutoDraw(True)
        if button.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                button.tStop = t  # not accounting for scr refresh
                button.frameNStop = frameN  # exact frame index
                win.timeOnFlip(button, 'tStopRefresh')  # time at next scr refresh
                button.setAutoDraw(False)
        
        # *textbutton* updates
        if textbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbutton.frameNStart = frameN  # exact frame index
            textbutton.tStart = t  # local t and not account for scr refresh
            textbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbutton, 'tStartRefresh')  # time at next scr refresh
            textbutton.setAutoDraw(True)
        if textbutton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbutton.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textbutton.tStop = t  # not accounting for scr refresh
                textbutton.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbutton, 'tStopRefresh')  # time at next scr refresh
                textbutton.setAutoDraw(False)
        
        # *textvideo* updates
        if textvideo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textvideo.frameNStart = frameN  # exact frame index
            textvideo.tStart = t  # local t and not account for scr refresh
            textvideo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textvideo, 'tStartRefresh')  # time at next scr refresh
            textvideo.setAutoDraw(True)
        if textvideo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textvideo.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textvideo.tStop = t  # not accounting for scr refresh
                textvideo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textvideo, 'tStopRefresh')  # time at next scr refresh
                textvideo.setAutoDraw(False)
        
        # *sensor* updates
        if sensor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor.frameNStart = frameN  # exact frame index
            sensor.tStart = t  # local t and not account for scr refresh
            sensor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor, 'tStartRefresh')  # time at next scr refresh
            sensor.setAutoDraw(True)
        if sensor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor.tStop = t  # not accounting for scr refresh
                sensor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor, 'tStopRefresh')  # time at next scr refresh
                sensor.setAutoDraw(False)
        
        # *key_response* updates
        waitOnFlip = False
        if key_response.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_response.frameNStart = frameN  # exact frame index
            key_response.tStart = t  # local t and not account for scr refresh
            key_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_response.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                key_response.tStop = t  # not accounting for scr refresh
                key_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
                key_response.status = FINISHED
        if key_response.status == STARTED and not waitOnFlip:
            theseKeys = key_response.getKeys(keyList=['space'], waitRelease=False)
            _key_response_allKeys.extend(theseKeys)
            if len(_key_response_allKeys):
                key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                key_response.rt = _key_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response_SComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response_S"-------
    for thisComponent in Response_SComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    videoresponse.stop()
    trials_2.addData('sensor.started', sensor.tStartRefresh)
    trials_2.addData('sensor.stopped', sensor.tStopRefresh)
    
    # ------Prepare to start Routine "Disconnecting"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter_disconnecting = np.random.uniform(1.5, 2.5, 1)
    
    # keep track of which components have finished
    DisconnectingComponents = [back10, textdisconnecting, sensor4]
    for thisComponent in DisconnectingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    DisconnectingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Disconnecting"-------
    while continueRoutine:
        # get current time
        t = DisconnectingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=DisconnectingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back10* updates
        if back10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back10.frameNStart = frameN  # exact frame index
            back10.tStart = t  # local t and not account for scr refresh
            back10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back10, 'tStartRefresh')  # time at next scr refresh
            back10.setAutoDraw(True)
        if back10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back10.tStartRefresh + jitter_disconnecting-frameTolerance:
                # keep track of stop time/frame for later
                back10.tStop = t  # not accounting for scr refresh
                back10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back10, 'tStopRefresh')  # time at next scr refresh
                back10.setAutoDraw(False)
        
        # *textdisconnecting* updates
        if textdisconnecting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textdisconnecting.frameNStart = frameN  # exact frame index
            textdisconnecting.tStart = t  # local t and not account for scr refresh
            textdisconnecting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textdisconnecting, 'tStartRefresh')  # time at next scr refresh
            textdisconnecting.setAutoDraw(True)
        if textdisconnecting.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textdisconnecting.tStartRefresh + jitter_disconnecting-frameTolerance:
                # keep track of stop time/frame for later
                textdisconnecting.tStop = t  # not accounting for scr refresh
                textdisconnecting.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textdisconnecting, 'tStopRefresh')  # time at next scr refresh
                textdisconnecting.setAutoDraw(False)
        
        # *sensor4* updates
        if sensor4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor4.frameNStart = frameN  # exact frame index
            sensor4.tStart = t  # local t and not account for scr refresh
            sensor4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor4, 'tStartRefresh')  # time at next scr refresh
            sensor4.setAutoDraw(True)
        if sensor4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor4.tStop = t  # not accounting for scr refresh
                sensor4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor4, 'tStopRefresh')  # time at next scr refresh
                sensor4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DisconnectingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Disconnecting"-------
    for thisComponent in DisconnectingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('sensor4.started', sensor4.tStartRefresh)
    trials_2.addData('sensor4.stopped', sensor4.tStopRefresh)
    # the Routine "Disconnecting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SubjectiveR"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyrespsubj.keys = []
    keyrespsubj.rt = []
    _keyrespsubj_allKeys = []
    SubjectiveResponse.reset()
    # keep track of which components have finished
    SubjectiveRComponents = [back22, textsubjresp, keyrespsubj, SubjectiveResponse, textsubjcon]
    for thisComponent in SubjectiveRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SubjectiveRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SubjectiveR"-------
    while continueRoutine:
        # get current time
        t = SubjectiveRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SubjectiveRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back22* updates
        if back22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back22.frameNStart = frameN  # exact frame index
            back22.tStart = t  # local t and not account for scr refresh
            back22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back22, 'tStartRefresh')  # time at next scr refresh
            back22.setAutoDraw(True)
        
        # *textsubjresp* updates
        if textsubjresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textsubjresp.frameNStart = frameN  # exact frame index
            textsubjresp.tStart = t  # local t and not account for scr refresh
            textsubjresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textsubjresp, 'tStartRefresh')  # time at next scr refresh
            textsubjresp.setAutoDraw(True)
        
        # *keyrespsubj* updates
        waitOnFlip = False
        if keyrespsubj.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            keyrespsubj.frameNStart = frameN  # exact frame index
            keyrespsubj.tStart = t  # local t and not account for scr refresh
            keyrespsubj.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyrespsubj, 'tStartRefresh')  # time at next scr refresh
            keyrespsubj.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyrespsubj.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyrespsubj.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyrespsubj.status == STARTED and not waitOnFlip:
            theseKeys = keyrespsubj.getKeys(keyList=['space'], waitRelease=False)
            _keyrespsubj_allKeys.extend(theseKeys)
            if len(_keyrespsubj_allKeys):
                keyrespsubj.keys = _keyrespsubj_allKeys[-1].name  # just the last key pressed
                keyrespsubj.rt = _keyrespsubj_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *SubjectiveResponse* updates
        if SubjectiveResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SubjectiveResponse.frameNStart = frameN  # exact frame index
            SubjectiveResponse.tStart = t  # local t and not account for scr refresh
            SubjectiveResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubjectiveResponse, 'tStartRefresh')  # time at next scr refresh
            SubjectiveResponse.setAutoDraw(True)
        
        # *textsubjcon* updates
        if textsubjcon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textsubjcon.frameNStart = frameN  # exact frame index
            textsubjcon.tStart = t  # local t and not account for scr refresh
            textsubjcon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textsubjcon, 'tStartRefresh')  # time at next scr refresh
            textsubjcon.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubjectiveRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SubjectiveR"-------
    for thisComponent in SubjectiveRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('textsubjresp.started', textsubjresp.tStartRefresh)
    trials_2.addData('textsubjresp.stopped', textsubjresp.tStopRefresh)
    trials_2.addData('SubjectiveResponse.response', SubjectiveResponse.getRating())
    trials_2.addData('SubjectiveResponse.rt', SubjectiveResponse.getRT())
    trials_2.addData('SubjectiveResponse.started', SubjectiveResponse.tStartRefresh)
    trials_2.addData('SubjectiveResponse.stopped', SubjectiveResponse.tStopRefresh)
    trials_2.addData('textsubjcon.started', textsubjcon.tStartRefresh)
    trials_2.addData('textsubjcon.stopped', textsubjcon.tStopRefresh)
    # the Routine "SubjectiveR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_respbreak.keys = []
key_respbreak.rt = []
_key_respbreak_allKeys = []
# keep track of which components have finished
BreakComponents = [back8, textbreak, key_respbreak]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back8* updates
    if back8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back8.frameNStart = frameN  # exact frame index
        back8.tStart = t  # local t and not account for scr refresh
        back8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back8, 'tStartRefresh')  # time at next scr refresh
        back8.setAutoDraw(True)
    
    # *textbreak* updates
    if textbreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbreak.frameNStart = frameN  # exact frame index
        textbreak.tStart = t  # local t and not account for scr refresh
        textbreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbreak, 'tStartRefresh')  # time at next scr refresh
        textbreak.setAutoDraw(True)
    
    # *key_respbreak* updates
    waitOnFlip = False
    if key_respbreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_respbreak.frameNStart = frameN  # exact frame index
        key_respbreak.tStart = t  # local t and not account for scr refresh
        key_respbreak.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_respbreak, 'tStartRefresh')  # time at next scr refresh
        key_respbreak.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_respbreak.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_respbreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_respbreak.status == STARTED and not waitOnFlip:
        theseKeys = key_respbreak.getKeys(keyList=['space'], waitRelease=False)
        _key_respbreak_allKeys.extend(theseKeys)
        if len(_key_respbreak_allKeys):
            key_respbreak.keys = _key_respbreak_allKeys[-1].name  # just the last key pressed
            key_respbreak.rt = _key_respbreak_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Polygraph_Condition"-------
continueRoutine = True
# update component parameters for each repeat
key_resppoly.keys = []
key_resppoly.rt = []
_key_resppoly_allKeys = []
# keep track of which components have finished
Polygraph_ConditionComponents = [back13, text_3, key_resppoly]
for thisComponent in Polygraph_ConditionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Polygraph_ConditionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Polygraph_Condition"-------
while continueRoutine:
    # get current time
    t = Polygraph_ConditionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Polygraph_ConditionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back13* updates
    if back13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back13.frameNStart = frameN  # exact frame index
        back13.tStart = t  # local t and not account for scr refresh
        back13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back13, 'tStartRefresh')  # time at next scr refresh
        back13.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resppoly* updates
    waitOnFlip = False
    if key_resppoly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resppoly.frameNStart = frameN  # exact frame index
        key_resppoly.tStart = t  # local t and not account for scr refresh
        key_resppoly.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resppoly, 'tStartRefresh')  # time at next scr refresh
        key_resppoly.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resppoly.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resppoly.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resppoly.status == STARTED and not waitOnFlip:
        theseKeys = key_resppoly.getKeys(keyList=['space'], waitRelease=False)
        _key_resppoly_allKeys.extend(theseKeys)
        if len(_key_resppoly_allKeys):
            key_resppoly.keys = _key_resppoly_allKeys[-1].name  # just the last key pressed
            key_resppoly.rt = _key_resppoly_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Polygraph_ConditionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Polygraph_Condition"-------
for thisComponent in Polygraph_ConditionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Polygraph_Condition" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PolyInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
key_resppoly2.keys = []
key_resppoly2.rt = []
_key_resppoly2_allKeys = []
# keep track of which components have finished
PolyInstruct2Components = [back17, textpolyinstruct, key_resppoly2]
for thisComponent in PolyInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PolyInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PolyInstruct2"-------
while continueRoutine:
    # get current time
    t = PolyInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PolyInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back17* updates
    if back17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back17.frameNStart = frameN  # exact frame index
        back17.tStart = t  # local t and not account for scr refresh
        back17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back17, 'tStartRefresh')  # time at next scr refresh
        back17.setAutoDraw(True)
    
    # *textpolyinstruct* updates
    if textpolyinstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textpolyinstruct.frameNStart = frameN  # exact frame index
        textpolyinstruct.tStart = t  # local t and not account for scr refresh
        textpolyinstruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textpolyinstruct, 'tStartRefresh')  # time at next scr refresh
        textpolyinstruct.setAutoDraw(True)
    
    # *key_resppoly2* updates
    waitOnFlip = False
    if key_resppoly2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resppoly2.frameNStart = frameN  # exact frame index
        key_resppoly2.tStart = t  # local t and not account for scr refresh
        key_resppoly2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resppoly2, 'tStartRefresh')  # time at next scr refresh
        key_resppoly2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resppoly2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resppoly2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resppoly2.status == STARTED and not waitOnFlip:
        theseKeys = key_resppoly2.getKeys(keyList=['space'], waitRelease=False)
        _key_resppoly2_allKeys.extend(theseKeys)
        if len(_key_resppoly2_allKeys):
            key_resppoly2.keys = _key_resppoly2_allKeys[-1].name  # just the last key pressed
            key_resppoly2.rt = _key_resppoly2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PolyInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PolyInstruct2"-------
for thisComponent in PolyInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "PolyInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo["participant"] + '_poly_questions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Social"-------
    continueRoutine = True
    # update component parameters for each repeat
    truth1_text.setText(question
)
    truth1_instruction.setText(condition)
    keysocial.keys = []
    keysocial.rt = []
    _keysocial_allKeys = []
    # keep track of which components have finished
    SocialComponents = [back6, truth1_text, truth1_instruction, buttoncon, textanswer, sensor2, keysocial]
    for thisComponent in SocialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SocialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Social"-------
    while continueRoutine:
        # get current time
        t = SocialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SocialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back6* updates
        if back6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back6.frameNStart = frameN  # exact frame index
            back6.tStart = t  # local t and not account for scr refresh
            back6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back6, 'tStartRefresh')  # time at next scr refresh
            back6.setAutoDraw(True)
        
        # *truth1_text* updates
        if truth1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            truth1_text.frameNStart = frameN  # exact frame index
            truth1_text.tStart = t  # local t and not account for scr refresh
            truth1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(truth1_text, 'tStartRefresh')  # time at next scr refresh
            truth1_text.setAutoDraw(True)
        
        # *truth1_instruction* updates
        if truth1_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            truth1_instruction.frameNStart = frameN  # exact frame index
            truth1_instruction.tStart = t  # local t and not account for scr refresh
            truth1_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(truth1_instruction, 'tStartRefresh')  # time at next scr refresh
            truth1_instruction.setAutoDraw(True)
        
        # *buttoncon* updates
        if buttoncon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttoncon.frameNStart = frameN  # exact frame index
            buttoncon.tStart = t  # local t and not account for scr refresh
            buttoncon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttoncon, 'tStartRefresh')  # time at next scr refresh
            buttoncon.setAutoDraw(True)
        
        # *textanswer* updates
        if textanswer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textanswer.frameNStart = frameN  # exact frame index
            textanswer.tStart = t  # local t and not account for scr refresh
            textanswer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textanswer, 'tStartRefresh')  # time at next scr refresh
            textanswer.setAutoDraw(True)
        
        # *sensor2* updates
        if sensor2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor2.frameNStart = frameN  # exact frame index
            sensor2.tStart = t  # local t and not account for scr refresh
            sensor2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor2, 'tStartRefresh')  # time at next scr refresh
            sensor2.setAutoDraw(True)
        if sensor2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor2.tStop = t  # not accounting for scr refresh
                sensor2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor2, 'tStopRefresh')  # time at next scr refresh
                sensor2.setAutoDraw(False)
        
        # *keysocial* updates
        waitOnFlip = False
        if keysocial.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            keysocial.frameNStart = frameN  # exact frame index
            keysocial.tStart = t  # local t and not account for scr refresh
            keysocial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keysocial, 'tStartRefresh')  # time at next scr refresh
            keysocial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keysocial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keysocial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keysocial.status == STARTED and not waitOnFlip:
            theseKeys = keysocial.getKeys(keyList=['space'], waitRelease=False)
            _keysocial_allKeys.extend(theseKeys)
            if len(_keysocial_allKeys):
                keysocial.keys = _keysocial_allKeys[-1].name  # just the last key pressed
                keysocial.rt = _keysocial_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SocialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Social"-------
    for thisComponent in SocialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sensor2.started', sensor2.tStartRefresh)
    trials.addData('sensor2.stopped', sensor2.tStopRefresh)
    # the Routine "Social" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "BioConnect"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter_bioconnect = np.random.uniform(0.7, 1.5, 1)
    
    # keep track of which components have finished
    BioConnectComponents = [back15, textbioconnect, sensor5]
    for thisComponent in BioConnectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BioConnectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BioConnect"-------
    while continueRoutine:
        # get current time
        t = BioConnectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BioConnectClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back15* updates
        if back15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back15.frameNStart = frameN  # exact frame index
            back15.tStart = t  # local t and not account for scr refresh
            back15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back15, 'tStartRefresh')  # time at next scr refresh
            back15.setAutoDraw(True)
        if back15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back15.tStartRefresh + jitter_bioconnect-frameTolerance:
                # keep track of stop time/frame for later
                back15.tStop = t  # not accounting for scr refresh
                back15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back15, 'tStopRefresh')  # time at next scr refresh
                back15.setAutoDraw(False)
        
        # *textbioconnect* updates
        if textbioconnect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbioconnect.frameNStart = frameN  # exact frame index
            textbioconnect.tStart = t  # local t and not account for scr refresh
            textbioconnect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbioconnect, 'tStartRefresh')  # time at next scr refresh
            textbioconnect.setAutoDraw(True)
        if textbioconnect.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbioconnect.tStartRefresh + jitter_bioconnect-frameTolerance:
                # keep track of stop time/frame for later
                textbioconnect.tStop = t  # not accounting for scr refresh
                textbioconnect.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbioconnect, 'tStopRefresh')  # time at next scr refresh
                textbioconnect.setAutoDraw(False)
        
        # *sensor5* updates
        if sensor5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor5.frameNStart = frameN  # exact frame index
            sensor5.tStart = t  # local t and not account for scr refresh
            sensor5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor5, 'tStartRefresh')  # time at next scr refresh
            sensor5.setAutoDraw(True)
        if sensor5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor5.tStop = t  # not accounting for scr refresh
                sensor5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor5, 'tStopRefresh')  # time at next scr refresh
                sensor5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BioConnectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BioConnect"-------
    for thisComponent in BioConnectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sensor5.started', sensor5.tStartRefresh)
    trials.addData('sensor5.stopped', sensor5.tStopRefresh)
    # the Routine "BioConnect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Response_P"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    bitalinovid = visual.MovieStim3(
        win=win, name='bitalinovid',units='norm', 
        noAudio = False,
        filename=bitalino,
        ori=0, pos=(0, 0.08), opacity=1,
        loop=False,
        size=(1.8, 1.5),
        depth=-5.0,
        )
    key_resresp.keys = []
    key_resresp.rt = []
    _key_resresp_allKeys = []
    # keep track of which components have finished
    Response_PComponents = [back14, button1, buttont, sensor1, textpoly, bitalinovid, key_resresp]
    for thisComponent in Response_PComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Response_PClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Response_P"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Response_PClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Response_PClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back14* updates
        if back14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back14.frameNStart = frameN  # exact frame index
            back14.tStart = t  # local t and not account for scr refresh
            back14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back14, 'tStartRefresh')  # time at next scr refresh
            back14.setAutoDraw(True)
        if back14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back14.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                back14.tStop = t  # not accounting for scr refresh
                back14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back14, 'tStopRefresh')  # time at next scr refresh
                back14.setAutoDraw(False)
        
        # *button1* updates
        if button1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button1.frameNStart = frameN  # exact frame index
            button1.tStart = t  # local t and not account for scr refresh
            button1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
            button1.setAutoDraw(True)
        if button1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button1.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                button1.tStop = t  # not accounting for scr refresh
                button1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(button1, 'tStopRefresh')  # time at next scr refresh
                button1.setAutoDraw(False)
        
        # *buttont* updates
        if buttont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buttont.frameNStart = frameN  # exact frame index
            buttont.tStart = t  # local t and not account for scr refresh
            buttont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buttont, 'tStartRefresh')  # time at next scr refresh
            buttont.setAutoDraw(True)
        if buttont.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buttont.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                buttont.tStop = t  # not accounting for scr refresh
                buttont.frameNStop = frameN  # exact frame index
                win.timeOnFlip(buttont, 'tStopRefresh')  # time at next scr refresh
                buttont.setAutoDraw(False)
        
        # *sensor1* updates
        if sensor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor1.frameNStart = frameN  # exact frame index
            sensor1.tStart = t  # local t and not account for scr refresh
            sensor1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor1, 'tStartRefresh')  # time at next scr refresh
            sensor1.setAutoDraw(True)
        if sensor1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor1.tStop = t  # not accounting for scr refresh
                sensor1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor1, 'tStopRefresh')  # time at next scr refresh
                sensor1.setAutoDraw(False)
        
        # *textpoly* updates
        if textpoly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textpoly.frameNStart = frameN  # exact frame index
            textpoly.tStart = t  # local t and not account for scr refresh
            textpoly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textpoly, 'tStartRefresh')  # time at next scr refresh
            textpoly.setAutoDraw(True)
        if textpoly.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textpoly.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textpoly.tStop = t  # not accounting for scr refresh
                textpoly.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textpoly, 'tStopRefresh')  # time at next scr refresh
                textpoly.setAutoDraw(False)
        
        # *bitalinovid* updates
        if bitalinovid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bitalinovid.frameNStart = frameN  # exact frame index
            bitalinovid.tStart = t  # local t and not account for scr refresh
            bitalinovid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bitalinovid, 'tStartRefresh')  # time at next scr refresh
            bitalinovid.setAutoDraw(True)
        if bitalinovid.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bitalinovid.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                bitalinovid.tStop = t  # not accounting for scr refresh
                bitalinovid.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bitalinovid, 'tStopRefresh')  # time at next scr refresh
                bitalinovid.setAutoDraw(False)
        
        # *key_resresp* updates
        waitOnFlip = False
        if key_resresp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resresp.frameNStart = frameN  # exact frame index
            key_resresp.tStart = t  # local t and not account for scr refresh
            key_resresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resresp, 'tStartRefresh')  # time at next scr refresh
            key_resresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resresp.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                key_resresp.tStop = t  # not accounting for scr refresh
                key_resresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resresp, 'tStopRefresh')  # time at next scr refresh
                key_resresp.status = FINISHED
        if key_resresp.status == STARTED and not waitOnFlip:
            theseKeys = key_resresp.getKeys(keyList=['space'], waitRelease=False)
            _key_resresp_allKeys.extend(theseKeys)
            if len(_key_resresp_allKeys):
                key_resresp.keys = _key_resresp_allKeys[-1].name  # just the last key pressed
                key_resresp.rt = _key_resresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Response_PComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Response_P"-------
    for thisComponent in Response_PComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sensor1.started', sensor1.tStartRefresh)
    trials.addData('sensor1.stopped', sensor1.tStopRefresh)
    bitalinovid.stop()
    
    # ------Prepare to start Routine "BioDisConnect"-------
    continueRoutine = True
    # update component parameters for each repeat
    jitter_biodisconnect = np.random.uniform(1.5, 2.5, 1)
    
    # keep track of which components have finished
    BioDisConnectComponents = [back16, textbiodisconnect, sensor6]
    for thisComponent in BioDisConnectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BioDisConnectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BioDisConnect"-------
    while continueRoutine:
        # get current time
        t = BioDisConnectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BioDisConnectClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back16* updates
        if back16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back16.frameNStart = frameN  # exact frame index
            back16.tStart = t  # local t and not account for scr refresh
            back16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back16, 'tStartRefresh')  # time at next scr refresh
            back16.setAutoDraw(True)
        if back16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > back16.tStartRefresh + jitter_biodisconnect-frameTolerance:
                # keep track of stop time/frame for later
                back16.tStop = t  # not accounting for scr refresh
                back16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(back16, 'tStopRefresh')  # time at next scr refresh
                back16.setAutoDraw(False)
        
        # *textbiodisconnect* updates
        if textbiodisconnect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbiodisconnect.frameNStart = frameN  # exact frame index
            textbiodisconnect.tStart = t  # local t and not account for scr refresh
            textbiodisconnect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbiodisconnect, 'tStartRefresh')  # time at next scr refresh
            textbiodisconnect.setAutoDraw(True)
        if textbiodisconnect.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbiodisconnect.tStartRefresh + jitter_biodisconnect-frameTolerance:
                # keep track of stop time/frame for later
                textbiodisconnect.tStop = t  # not accounting for scr refresh
                textbiodisconnect.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbiodisconnect, 'tStopRefresh')  # time at next scr refresh
                textbiodisconnect.setAutoDraw(False)
        
        # *sensor6* updates
        if sensor6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sensor6.frameNStart = frameN  # exact frame index
            sensor6.tStart = t  # local t and not account for scr refresh
            sensor6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sensor6, 'tStartRefresh')  # time at next scr refresh
            sensor6.setAutoDraw(True)
        if sensor6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sensor6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sensor6.tStop = t  # not accounting for scr refresh
                sensor6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sensor6, 'tStopRefresh')  # time at next scr refresh
                sensor6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BioDisConnectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BioDisConnect"-------
    for thisComponent in BioDisConnectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('sensor6.started', sensor6.tStartRefresh)
    trials.addData('sensor6.stopped', sensor6.tStopRefresh)
    # the Routine "BioDisConnect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SubjectiveR"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyrespsubj.keys = []
    keyrespsubj.rt = []
    _keyrespsubj_allKeys = []
    SubjectiveResponse.reset()
    # keep track of which components have finished
    SubjectiveRComponents = [back22, textsubjresp, keyrespsubj, SubjectiveResponse, textsubjcon]
    for thisComponent in SubjectiveRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SubjectiveRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SubjectiveR"-------
    while continueRoutine:
        # get current time
        t = SubjectiveRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SubjectiveRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back22* updates
        if back22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back22.frameNStart = frameN  # exact frame index
            back22.tStart = t  # local t and not account for scr refresh
            back22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back22, 'tStartRefresh')  # time at next scr refresh
            back22.setAutoDraw(True)
        
        # *textsubjresp* updates
        if textsubjresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textsubjresp.frameNStart = frameN  # exact frame index
            textsubjresp.tStart = t  # local t and not account for scr refresh
            textsubjresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textsubjresp, 'tStartRefresh')  # time at next scr refresh
            textsubjresp.setAutoDraw(True)
        
        # *keyrespsubj* updates
        waitOnFlip = False
        if keyrespsubj.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            keyrespsubj.frameNStart = frameN  # exact frame index
            keyrespsubj.tStart = t  # local t and not account for scr refresh
            keyrespsubj.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyrespsubj, 'tStartRefresh')  # time at next scr refresh
            keyrespsubj.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyrespsubj.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyrespsubj.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyrespsubj.status == STARTED and not waitOnFlip:
            theseKeys = keyrespsubj.getKeys(keyList=['space'], waitRelease=False)
            _keyrespsubj_allKeys.extend(theseKeys)
            if len(_keyrespsubj_allKeys):
                keyrespsubj.keys = _keyrespsubj_allKeys[-1].name  # just the last key pressed
                keyrespsubj.rt = _keyrespsubj_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *SubjectiveResponse* updates
        if SubjectiveResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SubjectiveResponse.frameNStart = frameN  # exact frame index
            SubjectiveResponse.tStart = t  # local t and not account for scr refresh
            SubjectiveResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubjectiveResponse, 'tStartRefresh')  # time at next scr refresh
            SubjectiveResponse.setAutoDraw(True)
        
        # *textsubjcon* updates
        if textsubjcon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textsubjcon.frameNStart = frameN  # exact frame index
            textsubjcon.tStart = t  # local t and not account for scr refresh
            textsubjcon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textsubjcon, 'tStartRefresh')  # time at next scr refresh
            textsubjcon.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubjectiveRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SubjectiveR"-------
    for thisComponent in SubjectiveRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textsubjresp.started', textsubjresp.tStartRefresh)
    trials.addData('textsubjresp.stopped', textsubjresp.tStopRefresh)
    trials.addData('SubjectiveResponse.response', SubjectiveResponse.getRating())
    trials.addData('SubjectiveResponse.rt', SubjectiveResponse.getRT())
    trials.addData('SubjectiveResponse.started', SubjectiveResponse.tStartRefresh)
    trials.addData('SubjectiveResponse.stopped', SubjectiveResponse.tStopRefresh)
    trials.addData('textsubjcon.started', textsubjcon.tStartRefresh)
    trials.addData('textsubjcon.stopped', textsubjcon.tStopRefresh)
    # the Routine "SubjectiveR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
EndComponents = [back11, textend, key_resp_4]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *back11* updates
    if back11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back11.frameNStart = frameN  # exact frame index
        back11.tStart = t  # local t and not account for scr refresh
        back11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back11, 'tStartRefresh')  # time at next scr refresh
        back11.setAutoDraw(True)
    if back11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back11.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            back11.tStop = t  # not accounting for scr refresh
            back11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back11, 'tStopRefresh')  # time at next scr refresh
            back11.setAutoDraw(False)
    
    # *textend* updates
    if textend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textend.frameNStart = frameN  # exact frame index
        textend.tStart = t  # local t and not account for scr refresh
        textend.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textend, 'tStartRefresh')  # time at next scr refresh
        textend.setAutoDraw(True)
    if textend.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textend.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            textend.tStop = t  # not accounting for scr refresh
            textend.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textend, 'tStopRefresh')  # time at next scr refresh
            textend.setAutoDraw(False)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_4.tStop = t  # not accounting for scr refresh
            key_resp_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
            key_resp_4.status = FINISHED
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
