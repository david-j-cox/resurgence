#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Sun Jul 18 14:16:55 2021
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
expName = 'resurgence'  # from the Builder filename that created this script
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
    originPath='/Users/davidjcox/Dropbox (Personal)/Projects/Manuscripts In Progress/Empirical/Caldwell University/Resurgence/resurgence_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In the following phases, you will see three colored squares on the screen. Clicking on the squares may or may not result in points. Your point total will be shown in the upper right-hand corner of the screen. \n\nAt the end of the task, you will be awarded $0.01 per point earned. For example, if you earn 1000 points, you will receive $10.00. If you close the program, we will lose all data and your session will end. When you are ready to begin, press the space bar to begin this experiment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
exp_instr_resp = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
target_p = visual.Rect(
    win=win, name='target_p',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
alternative_p = visual.Rect(
    win=win, name='alternative_p',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1, 0.294117647058824, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
control_p = visual.Rect(
    win=win, name='control_p',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse_p = event.Mouse(win=win)
x, y = [None, None]
mouse_p.mouseClock = core.Clock()
ovr_bank = 0
mask_p = visual.Rect(
    win=win, name='mask_p',
    width=(10, 10)[0], height=(10, 10)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
consequence_p = visual.TextStim(win=win, name='consequence_p',
    text='+1 Point',
    font='Arial',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
bank_amount_p = visual.TextStim(win=win, name='bank_amount_p',
    text='default text',
    font='Arial',
    pos=(0.85, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
bank_text_p = visual.TextStim(win=win, name='bank_text_p',
    text='Current Bank: ',
    font='Arial',
    pos=(0.65, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
consume_p = visual.TextStim(win=win, name='consume_p',
    text='Click to collect. ',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "begin_ici"
begin_iciClock = core.Clock()
begin_text = visual.TextStim(win=win, name='begin_text',
    text='It looks like you’re getting the hang of this!\n\nPlease wait while Phase 1 loads. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
click_ph1 = visual.TextStim(win=win, name='click_ph1',
    text='Press the space bar to continue to Phase 1. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
begin_ph1 = keyboard.Keyboard()

# Initialize components for Routine "phase_1"
phase_1Clock = core.Clock()
target = visual.Rect(
    win=win, name='target',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
alternative = visual.Rect(
    win=win, name='alternative',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1, 0.294117647058824, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
control = visual.Rect(
    win=win, name='control',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
mask = visual.Rect(
    win=win, name='mask',
    width=(10, 10)[0], height=(10, 10)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
ovr_bank  = 0
consequence = visual.TextStim(win=win, name='consequence',
    text='+1 Point',
    font='Arial',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
bank_amount = visual.TextStim(win=win, name='bank_amount',
    text='default text',
    font='Arial',
    pos=(0.85, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
bank_text = visual.TextStim(win=win, name='bank_text',
    text='Phase 1 Bank: ',
    font='Arial',
    pos=(0.65, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
consume = visual.TextStim(win=win, name='consume',
    text='Click to collect. ',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "ici_1"
ici_1Clock = core.Clock()
ici_1_text = visual.TextStim(win=win, name='ici_1_text',
    text='Phase 1 has ended. \nPlease wait while Phase 2 loads.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
click_ph2 = visual.TextStim(win=win, name='click_ph2',
    text='Press the space bar to begin Phase 2. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
begin_ph2 = keyboard.Keyboard()

# Initialize components for Routine "phase_2"
phase_2Clock = core.Clock()
target_2 = visual.Rect(
    win=win, name='target_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, 1], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
alternative_2 = visual.Rect(
    win=win, name='alternative_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1, 0.294117647058824, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
control_2 = visual.Rect(
    win=win, name='control_2',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, -1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
mask_2 = visual.Rect(
    win=win, name='mask_2',
    width=(10, 10)[0], height=(10, 10)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor='grey', lineColorSpace='rgb',
    fillColor='grey', fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
consequence_2 = visual.TextStim(win=win, name='consequence_2',
    text='+1 Point',
    font='Arial',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
bank_amount_2 = visual.TextStim(win=win, name='bank_amount_2',
    text='default text',
    font='Arial',
    pos=(0.85, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
bank_text_2 = visual.TextStim(win=win, name='bank_text_2',
    text='Phase 2 Bank: ',
    font='Arial',
    pos=(0.65, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
consume_2 = visual.TextStim(win=win, name='consume_2',
    text='Click to collect. ',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "ici_2"
ici_2Clock = core.Clock()
ici_2_text = visual.TextStim(win=win, name='ici_2_text',
    text='Phase 2 has ended. \nPlease wait while Phase 3 loads.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
click_ph3 = visual.TextStim(win=win, name='click_ph3',
    text='Press the space bar to begin Phase 3. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
begin_ph3 = keyboard.Keyboard()

# Initialize components for Routine "phase_3"
phase_3Clock = core.Clock()
target_3 = visual.Rect(
    win=win, name='target_3',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, 1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
alternative_3 = visual.Rect(
    win=win, name='alternative_3',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1, 0.294117647058824, -1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
control_3 = visual.Rect(
    win=win, name='control_3',
    width=(0.20, 0.20)[0], height=(0.20, 0.20)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-1, -1, -1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
bank_amount_3 = visual.TextStim(win=win, name='bank_amount_3',
    text='default text',
    font='Arial',
    pos=(0.85, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
bank_text_3 = visual.TextStim(win=win, name='bank_text_3',
    text='Phase 3 Bank: ',
    font='Arial',
    pos=(0.65, .45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "end_text"
end_textClock = core.Clock()
end_text_ = visual.TextStim(win=win, name='end_text_',
    text='Thank you for participating! This experiment has ended. The total amount of points you earned was: ',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ovr_bank_amount = visual.TextStim(win=win, name='ovr_bank_amount',
    text='default text',
    font='Arial',
    pos=(0, -0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
exp_instr_resp.keys = []
exp_instr_resp.rt = []
_exp_instr_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [text, exp_instr_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *exp_instr_resp* updates
    waitOnFlip = False
    if exp_instr_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        exp_instr_resp.frameNStart = frameN  # exact frame index
        exp_instr_resp.tStart = t  # local t and not account for scr refresh
        exp_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_instr_resp, 'tStartRefresh')  # time at next scr refresh
        exp_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exp_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exp_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exp_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = exp_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _exp_instr_resp_allKeys.extend(theseKeys)
        if len(_exp_instr_resp_allKeys):
            exp_instr_resp.keys = _exp_instr_resp_allKeys[-1].name  # just the last key pressed
            exp_instr_resp.rt = _exp_instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if exp_instr_resp.keys in ['', [], None]:  # No response was made
    exp_instr_resp.keys = None
thisExp.addData('exp_instr_resp.keys',exp_instr_resp.keys)
if exp_instr_resp.keys != None:  # we had a response
    thisExp.addData('exp_instr_resp.rt', exp_instr_resp.rt)
thisExp.addData('exp_instr_resp.started', exp_instr_resp.tStartRefresh)
thisExp.addData('exp_instr_resp.stopped', exp_instr_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_p
    mouse_p.x = []
    mouse_p.y = []
    mouse_p.leftButton = []
    mouse_p.midButton = []
    mouse_p.rightButton = []
    mouse_p.time = []
    mouse_p.clicked_name = []
    mouse_p.clicked_pos = []
    gotValidClick = False  # until a click is received
    mouse_p.mouseClock.reset()
    # Function to play sound on click
    from psychopy.sound import Sound
    def play_sound():
        beep = sound.Sound('A', secs=.3) 
        beep.setVolume(1)
        beep.play()
        core.wait(.3)
    
    # Some clocks
    duration = core.Clock()
    timer = core.CountdownTimer(60)  # Phase timer
    
    # Store number of responses
    tar_count = 0
    alt_count = 0
    con_count = 0
    
    # Variables we'll update and display
    bank = 0
    curr_opacity=0
    mask_opacity=0
    consume_position = (10, 0)
    # keep track of which components have finished
    practiceComponents = [target_p, alternative_p, control_p, mouse_p, mask_p, consequence_p, bank_amount_p, bank_text_p, consume_p]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_p* updates
        if target_p.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            target_p.frameNStart = frameN  # exact frame index
            target_p.tStart = t  # local t and not account for scr refresh
            target_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_p, 'tStartRefresh')  # time at next scr refresh
            target_p.setAutoDraw(True)
        if target_p.status == STARTED:  # only update if drawing
            target_p.setOpacity(1)
            target_p.setPos((-cos(t*0.5)*0.75, cos(t*0.25)*0.4))
        
        # *alternative_p* updates
        if alternative_p.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            alternative_p.frameNStart = frameN  # exact frame index
            alternative_p.tStart = t  # local t and not account for scr refresh
            alternative_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative_p, 'tStartRefresh')  # time at next scr refresh
            alternative_p.setAutoDraw(True)
        if alternative_p.status == STARTED:  # only update if drawing
            alternative_p.setOpacity(1)
            alternative_p.setPos((cos(t*0.5)*0.75, (cos(t*-0.25+2.57)*-0.4)))
        
        # *control_p* updates
        if control_p.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            control_p.frameNStart = frameN  # exact frame index
            control_p.tStart = t  # local t and not account for scr refresh
            control_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(control_p, 'tStartRefresh')  # time at next scr refresh
            control_p.setAutoDraw(True)
        if control_p.status == STARTED:  # only update if drawing
            control_p.setOpacity(1)
            control_p.setPos((cos((t+2.57)*0.5)*0.75, cos(t*-0.25)*-0.4))
        # *mouse_p* updates
        if mouse_p.status == NOT_STARTED and t >= 0.50-frameTolerance:
            # keep track of start time/frame for later
            mouse_p.frameNStart = frameN  # exact frame index
            mouse_p.tStart = t  # local t and not account for scr refresh
            mouse_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_p, 'tStartRefresh')  # time at next scr refresh
            mouse_p.status = STARTED
            prevButtonState = mouse_p.getPressed()  # if button is down already this ISN'T a new click
        if mouse_p.status == STARTED:  # only update if started and not finished!
            buttons = mouse_p.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target, alternative, control]:
                        if obj.contains(mouse_p):
                            gotValidClick = True
                            mouse_p.clicked_name.append(obj.name)
                            mouse_p.clicked_pos.append(obj.pos)
                    x, y = mouse_p.getPos()
                    mouse_p.x.append(x)
                    mouse_p.y.append(y)
                    buttons = mouse_p.getPressed()
                    mouse_p.leftButton.append(buttons[0])
                    mouse_p.midButton.append(buttons[1])
                    mouse_p.rightButton.append(buttons[2])
                    mouse_p.time.append(mouse_p.mouseClock.getTime())
        if mouse.isPressedIn(target_p):
            consume_position=(0, 0)
            curr_opacity=1
            mask_opacity=1
            play_sound()
            tar_count +=1
        
        if mouse.isPressedIn(alternative_p):
            consume_position=(0, 0)
            curr_opacity=1
            mask_opacity=1
            play_sound()
            alt_count +=1
        
        if mouse.isPressedIn(consume_p):
            consume_position=(100, 0)
            curr_opacity=0
            mask_opacity=0
            bank+=1
            con_count +=1
        
        if timer.getTime() <=40:
            if tar_count > 8:
                if alt_count > 8:
                    if con_count > 8:
                        continueRoutine=False
        
        if timer.getTime()<=0:
            continueRoutine=False
        
        # *mask_p* updates
        if mask_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mask_p.frameNStart = frameN  # exact frame index
            mask_p.tStart = t  # local t and not account for scr refresh
            mask_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask_p, 'tStartRefresh')  # time at next scr refresh
            mask_p.setAutoDraw(True)
        if mask_p.status == STARTED:  # only update if drawing
            mask_p.setOpacity(mask_opacity)
        
        # *consequence_p* updates
        if consequence_p.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            consequence_p.frameNStart = frameN  # exact frame index
            consequence_p.tStart = t  # local t and not account for scr refresh
            consequence_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consequence_p, 'tStartRefresh')  # time at next scr refresh
            consequence_p.setAutoDraw(True)
        if consequence_p.status == STARTED:  # only update if drawing
            consequence_p.setOpacity(curr_opacity)
        
        # *bank_amount_p* updates
        if bank_amount_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_amount_p.frameNStart = frameN  # exact frame index
            bank_amount_p.tStart = t  # local t and not account for scr refresh
            bank_amount_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_amount_p, 'tStartRefresh')  # time at next scr refresh
            bank_amount_p.setAutoDraw(True)
        if bank_amount_p.status == STARTED:  # only update if drawing
            bank_amount_p.setText(bank)
        
        # *bank_text_p* updates
        if bank_text_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_text_p.frameNStart = frameN  # exact frame index
            bank_text_p.tStart = t  # local t and not account for scr refresh
            bank_text_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_text_p, 'tStartRefresh')  # time at next scr refresh
            bank_text_p.setAutoDraw(True)
        
        # *consume_p* updates
        if consume_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consume_p.frameNStart = frameN  # exact frame index
            consume_p.tStart = t  # local t and not account for scr refresh
            consume_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consume_p, 'tStartRefresh')  # time at next scr refresh
            consume_p.setAutoDraw(True)
        if consume_p.status == STARTED:  # only update if drawing
            consume_p.setOpacity(mask_opacity)
            consume_p.setPos(consume_position)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('target_p.started', target_p.tStartRefresh)
    practice_trials.addData('target_p.stopped', target_p.tStopRefresh)
    practice_trials.addData('alternative_p.started', alternative_p.tStartRefresh)
    practice_trials.addData('alternative_p.stopped', alternative_p.tStopRefresh)
    practice_trials.addData('control_p.started', control_p.tStartRefresh)
    practice_trials.addData('control_p.stopped', control_p.tStopRefresh)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('mouse_p.x', mouse_p.x)
    practice_trials.addData('mouse_p.y', mouse_p.y)
    practice_trials.addData('mouse_p.leftButton', mouse_p.leftButton)
    practice_trials.addData('mouse_p.midButton', mouse_p.midButton)
    practice_trials.addData('mouse_p.rightButton', mouse_p.rightButton)
    practice_trials.addData('mouse_p.time', mouse_p.time)
    practice_trials.addData('mouse_p.clicked_name', mouse_p.clicked_name)
    practice_trials.addData('mouse_p.clicked_pos', mouse_p.clicked_pos)
    practice_trials.addData('mouse_p.started', mouse_p.tStart)
    practice_trials.addData('mouse_p.stopped', mouse_p.tStop)
    practice_trials.addData('mask_p.started', mask_p.tStartRefresh)
    practice_trials.addData('mask_p.stopped', mask_p.tStopRefresh)
    practice_trials.addData('consequence_p.started', consequence_p.tStartRefresh)
    practice_trials.addData('consequence_p.stopped', consequence_p.tStopRefresh)
    practice_trials.addData('bank_amount_p.started', bank_amount_p.tStartRefresh)
    practice_trials.addData('bank_amount_p.stopped', bank_amount_p.tStopRefresh)
    practice_trials.addData('bank_text_p.started', bank_text_p.tStartRefresh)
    practice_trials.addData('bank_text_p.stopped', bank_text_p.tStopRefresh)
    practice_trials.addData('consume_p.started', consume_p.tStartRefresh)
    practice_trials.addData('consume_p.stopped', consume_p.tStopRefresh)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials'


# ------Prepare to start Routine "begin_ici"-------
continueRoutine = True
# update component parameters for each repeat
begin_ph1.keys = []
begin_ph1.rt = []
_begin_ph1_allKeys = []
# keep track of which components have finished
begin_iciComponents = [begin_text, click_ph1, begin_ph1]
for thisComponent in begin_iciComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
begin_iciClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin_ici"-------
while continueRoutine:
    # get current time
    t = begin_iciClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=begin_iciClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_text* updates
    if begin_text.status == NOT_STARTED and tThisFlip >= 0.50-frameTolerance:
        # keep track of start time/frame for later
        begin_text.frameNStart = frameN  # exact frame index
        begin_text.tStart = t  # local t and not account for scr refresh
        begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_text, 'tStartRefresh')  # time at next scr refresh
        begin_text.setAutoDraw(True)
    if begin_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > begin_text.tStartRefresh + 5.00-frameTolerance:
            # keep track of stop time/frame for later
            begin_text.tStop = t  # not accounting for scr refresh
            begin_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(begin_text, 'tStopRefresh')  # time at next scr refresh
            begin_text.setAutoDraw(False)
    
    # *click_ph1* updates
    if click_ph1.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        click_ph1.frameNStart = frameN  # exact frame index
        click_ph1.tStart = t  # local t and not account for scr refresh
        click_ph1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click_ph1, 'tStartRefresh')  # time at next scr refresh
        click_ph1.setAutoDraw(True)
    
    # *begin_ph1* updates
    waitOnFlip = False
    if begin_ph1.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        begin_ph1.frameNStart = frameN  # exact frame index
        begin_ph1.tStart = t  # local t and not account for scr refresh
        begin_ph1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_ph1, 'tStartRefresh')  # time at next scr refresh
        begin_ph1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_ph1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_ph1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_ph1.status == STARTED and not waitOnFlip:
        theseKeys = begin_ph1.getKeys(keyList=['space'], waitRelease=False)
        _begin_ph1_allKeys.extend(theseKeys)
        if len(_begin_ph1_allKeys):
            begin_ph1.keys = _begin_ph1_allKeys[-1].name  # just the last key pressed
            begin_ph1.rt = _begin_ph1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_iciComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin_ici"-------
for thisComponent in begin_iciComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin_text.started', begin_text.tStartRefresh)
thisExp.addData('begin_text.stopped', begin_text.tStopRefresh)
thisExp.addData('click_ph1.started', click_ph1.tStartRefresh)
thisExp.addData('click_ph1.stopped', click_ph1.tStopRefresh)
# check responses
if begin_ph1.keys in ['', [], None]:  # No response was made
    begin_ph1.keys = None
thisExp.addData('begin_ph1.keys',begin_ph1.keys)
if begin_ph1.keys != None:  # we had a response
    thisExp.addData('begin_ph1.rt', begin_ph1.rt)
thisExp.addData('begin_ph1.started', begin_ph1.tStartRefresh)
thisExp.addData('begin_ph1.stopped', begin_ph1.tStopRefresh)
thisExp.nextEntry()
# the Routine "begin_ici" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ph_1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file.csv'),
    seed=None, name='ph_1_trials')
thisExp.addLoop(ph_1_trials)  # add the loop to the experiment
thisPh_1_trial = ph_1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPh_1_trial.rgb)
if thisPh_1_trial != None:
    for paramName in thisPh_1_trial:
        exec('{} = thisPh_1_trial[paramName]'.format(paramName))

for thisPh_1_trial in ph_1_trials:
    currentLoop = ph_1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPh_1_trial.rgb)
    if thisPh_1_trial != None:
        for paramName in thisPh_1_trial:
            exec('{} = thisPh_1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    mouse.clicked_pos = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # Sound function
    from psychopy.sound import Sound
    def play_sound():
        beep = sound.Sound('A', secs=.3)  
        beep.setVolume(1)
        beep.play()
        core.wait(.3)
    
    # Timers
    timer = core.CountdownTimer(20)
    duration = core.Clock()
    
    # Variables to save
    bank = 0
    curr_opacity=0
    mask_opacity=0
    consume_position = (10, 0)
    
    # Counts of responses for stability calculations
    #tar_count = 0
    #alt_count = 0
    #con_count = 0
    #all_count = 0
    
    ### DEAD CODE TRYING TO CALCULATE STABILITY
    #def splice_list(list, t_1, t_2):
    #    temp_count = 0
    #    for i in list:
    #        if i >= t_1:
    #            if i <= t_2:
    #                temp_count = temp_count +1
    #
    #def calc_stability(response_list):
    #    cur_time = duration.getTime() # Get current time
    #    # Get times for thee comparison bins
    #    three_start = cur_time - 30
    #    three_end = cur_time - 20
    #    two_end = cur_time - 10
    #    # Get number of responses per time bin
    #    temp_3 = splice_list(response_list , three_start, three_end)
    #    temp_2 = splice_list(response_list , three_end, two_end)
    #    temp_1 = splice_list(response_list , two_end, cur_time)
    #    y = [temp_3, temp_2, temp_1]
    #    # Calculate if responding meets stability criteria
    #    if (max(y) - min(y)) <=6:
    #        change_y = y[2] - y[0]
    #        change_x = 25-5
    #        temp_slope = change_y / change_x
    #        if temp_slope <= 0.15*max(y):
    #            return True
    #        else:
    #            return False
    
    # keep track of which components have finished
    phase_1Components = [target, alternative, control, mouse, mask, consequence, bank_amount, bank_text, consume]
    for thisComponent in phase_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase_1"-------
    while continueRoutine:
        # get current time
        t = phase_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:  # only update if drawing
            target.setOpacity(1)
            target.setPos((-cos(t*0.5)*0.75, cos(t*0.25)*0.4))
        
        # *alternative* updates
        if alternative.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            alternative.frameNStart = frameN  # exact frame index
            alternative.tStart = t  # local t and not account for scr refresh
            alternative.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative, 'tStartRefresh')  # time at next scr refresh
            alternative.setAutoDraw(True)
        if alternative.status == STARTED:  # only update if drawing
            alternative.setOpacity(1)
            alternative.setPos((cos(t*0.5)*0.75, (cos(t*-0.25+2.57)*-0.4)))
        
        # *control* updates
        if control.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            control.frameNStart = frameN  # exact frame index
            control.tStart = t  # local t and not account for scr refresh
            control.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(control, 'tStartRefresh')  # time at next scr refresh
            control.setAutoDraw(True)
        if control.status == STARTED:  # only update if drawing
            control.setOpacity(1)
            control.setPos((cos((t+2.57)*0.5)*0.75, cos(t*-0.25)*-0.4))
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.50-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target, alternative, control]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                            mouse.clicked_pos.append(obj.pos)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        
        # *mask* updates
        if mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mask.frameNStart = frameN  # exact frame index
            mask.tStart = t  # local t and not account for scr refresh
            mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask, 'tStartRefresh')  # time at next scr refresh
            mask.setAutoDraw(True)
        if mask.status == STARTED:  # only update if drawing
            mask.setOpacity(mask_opacity)
        # Present SR+ following target response
        if mouse.isPressedIn(target):
        #    tar_count +=1
        #    all_count +=1
            consume_position=(0, 0)
            curr_opacity=1
            mask_opacity=1
            play_sound()
        
        # No consequence for alternative or control responses
        #if mouse.isPressedIn(alternative):
        #    alt_count +=1
        #    all_count +=1
        
        #if mouse.isPressedIn(control):
        #    con_count +=1
        #    all_count +=1
        
        # Consummatory response
        if mouse.isPressedIn(consume):
            consume_position=(10, 0)
            curr_opacity=0
            mask_opacity=0
            bank+=1
            ovr_bank+=1
        
        # Max condition duration of 10 mins
        if timer.getTime()<=0:
            continueRoutine=False
        
        # Calculate whether responding is stable
        #if duration.getTime() >= 30:
        #    if duration.getTime() % 30 == 0:
        #        # Determine if target stable
        #        tar_stable = calc_stability(tar_times)
        #        if tar_stable == True:
        #            # Determine if alt stable
        #            alt_stable = calc_stability(alt_times)
        #            if alt_stable == True:
        #                # Determine if control stable
        #                con_stable = calc_stability(con_times)
        #                if con_stable==True:
        #                    continueRoutine=False
        #                else:
        #                    continue
        #            else:
        #                continue
        #        else:
        #            continue
        #    else:
        #        continue
        #else:
        #    continue
        
        # *consequence* updates
        if consequence.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            consequence.frameNStart = frameN  # exact frame index
            consequence.tStart = t  # local t and not account for scr refresh
            consequence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consequence, 'tStartRefresh')  # time at next scr refresh
            consequence.setAutoDraw(True)
        if consequence.status == STARTED:  # only update if drawing
            consequence.setOpacity(curr_opacity)
        
        # *bank_amount* updates
        if bank_amount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_amount.frameNStart = frameN  # exact frame index
            bank_amount.tStart = t  # local t and not account for scr refresh
            bank_amount.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_amount, 'tStartRefresh')  # time at next scr refresh
            bank_amount.setAutoDraw(True)
        if bank_amount.status == STARTED:  # only update if drawing
            bank_amount.setText(bank)
        
        # *bank_text* updates
        if bank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_text.frameNStart = frameN  # exact frame index
            bank_text.tStart = t  # local t and not account for scr refresh
            bank_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_text, 'tStartRefresh')  # time at next scr refresh
            bank_text.setAutoDraw(True)
        
        # *consume* updates
        if consume.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consume.frameNStart = frameN  # exact frame index
            consume.tStart = t  # local t and not account for scr refresh
            consume.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consume, 'tStartRefresh')  # time at next scr refresh
            consume.setAutoDraw(True)
        if consume.status == STARTED:  # only update if drawing
            consume.setOpacity(mask_opacity)
            consume.setPos(consume_position)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase_1"-------
    for thisComponent in phase_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ph_1_trials.addData('target.started', target.tStartRefresh)
    ph_1_trials.addData('target.stopped', target.tStopRefresh)
    ph_1_trials.addData('alternative.started', alternative.tStartRefresh)
    ph_1_trials.addData('alternative.stopped', alternative.tStopRefresh)
    ph_1_trials.addData('control.started', control.tStartRefresh)
    ph_1_trials.addData('control.stopped', control.tStopRefresh)
    # store data for ph_1_trials (TrialHandler)
    ph_1_trials.addData('mouse.x', mouse.x)
    ph_1_trials.addData('mouse.y', mouse.y)
    ph_1_trials.addData('mouse.leftButton', mouse.leftButton)
    ph_1_trials.addData('mouse.midButton', mouse.midButton)
    ph_1_trials.addData('mouse.rightButton', mouse.rightButton)
    ph_1_trials.addData('mouse.time', mouse.time)
    ph_1_trials.addData('mouse.clicked_name', mouse.clicked_name)
    ph_1_trials.addData('mouse.clicked_pos', mouse.clicked_pos)
    ph_1_trials.addData('mouse.started', mouse.tStart)
    ph_1_trials.addData('mouse.stopped', mouse.tStop)
    ph_1_trials.addData('mask.started', mask.tStartRefresh)
    ph_1_trials.addData('mask.stopped', mask.tStopRefresh)
    ph_1_trials.addData('consequence.started', consequence.tStartRefresh)
    ph_1_trials.addData('consequence.stopped', consequence.tStopRefresh)
    ph_1_trials.addData('bank_amount.started', bank_amount.tStartRefresh)
    ph_1_trials.addData('bank_amount.stopped', bank_amount.tStopRefresh)
    ph_1_trials.addData('bank_text.started', bank_text.tStartRefresh)
    ph_1_trials.addData('bank_text.stopped', bank_text.tStopRefresh)
    ph_1_trials.addData('consume.started', consume.tStartRefresh)
    ph_1_trials.addData('consume.stopped', consume.tStopRefresh)
    # the Routine "phase_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'ph_1_trials'


# ------Prepare to start Routine "ici_1"-------
continueRoutine = True
# update component parameters for each repeat
begin_ph2.keys = []
begin_ph2.rt = []
_begin_ph2_allKeys = []
# keep track of which components have finished
ici_1Components = [ici_1_text, click_ph2, begin_ph2]
for thisComponent in ici_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ici_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ici_1"-------
while continueRoutine:
    # get current time
    t = ici_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ici_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ici_1_text* updates
    if ici_1_text.status == NOT_STARTED and tThisFlip >= 0.50-frameTolerance:
        # keep track of start time/frame for later
        ici_1_text.frameNStart = frameN  # exact frame index
        ici_1_text.tStart = t  # local t and not account for scr refresh
        ici_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ici_1_text, 'tStartRefresh')  # time at next scr refresh
        ici_1_text.setAutoDraw(True)
    if ici_1_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ici_1_text.tStartRefresh + 5.00-frameTolerance:
            # keep track of stop time/frame for later
            ici_1_text.tStop = t  # not accounting for scr refresh
            ici_1_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ici_1_text, 'tStopRefresh')  # time at next scr refresh
            ici_1_text.setAutoDraw(False)
    
    # *click_ph2* updates
    if click_ph2.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        click_ph2.frameNStart = frameN  # exact frame index
        click_ph2.tStart = t  # local t and not account for scr refresh
        click_ph2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click_ph2, 'tStartRefresh')  # time at next scr refresh
        click_ph2.setAutoDraw(True)
    
    # *begin_ph2* updates
    waitOnFlip = False
    if begin_ph2.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        begin_ph2.frameNStart = frameN  # exact frame index
        begin_ph2.tStart = t  # local t and not account for scr refresh
        begin_ph2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_ph2, 'tStartRefresh')  # time at next scr refresh
        begin_ph2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_ph2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_ph2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_ph2.status == STARTED and not waitOnFlip:
        theseKeys = begin_ph2.getKeys(keyList=['space'], waitRelease=False)
        _begin_ph2_allKeys.extend(theseKeys)
        if len(_begin_ph2_allKeys):
            begin_ph2.keys = _begin_ph2_allKeys[-1].name  # just the last key pressed
            begin_ph2.rt = _begin_ph2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ici_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ici_1"-------
for thisComponent in ici_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ici_1_text.started', ici_1_text.tStartRefresh)
thisExp.addData('ici_1_text.stopped', ici_1_text.tStopRefresh)
thisExp.addData('click_ph2.started', click_ph2.tStartRefresh)
thisExp.addData('click_ph2.stopped', click_ph2.tStopRefresh)
# check responses
if begin_ph2.keys in ['', [], None]:  # No response was made
    begin_ph2.keys = None
thisExp.addData('begin_ph2.keys',begin_ph2.keys)
if begin_ph2.keys != None:  # we had a response
    thisExp.addData('begin_ph2.rt', begin_ph2.rt)
thisExp.addData('begin_ph2.started', begin_ph2.tStartRefresh)
thisExp.addData('begin_ph2.stopped', begin_ph2.tStopRefresh)
thisExp.nextEntry()
# the Routine "ici_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ph_2_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file.csv'),
    seed=None, name='ph_2_trials')
thisExp.addLoop(ph_2_trials)  # add the loop to the experiment
thisPh_2_trial = ph_2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPh_2_trial.rgb)
if thisPh_2_trial != None:
    for paramName in thisPh_2_trial:
        exec('{} = thisPh_2_trial[paramName]'.format(paramName))

for thisPh_2_trial in ph_2_trials:
    currentLoop = ph_2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPh_2_trial.rgb)
    if thisPh_2_trial != None:
        for paramName in thisPh_2_trial:
            exec('{} = thisPh_2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    mouse_2.clicked_name = []
    mouse_2.clicked_pos = []
    gotValidClick = False  # until a click is received
    mouse_2.mouseClock.reset()
    # Sound function
    from psychopy.sound import Sound
    def play_sound():
        beep = sound.Sound('A', secs=.3)  
        beep.setVolume(1)
        beep.play()
        core.wait(.3)
    
    # Timer
    timer = core.CountdownTimer(20)
    
    # Some variables we'll need
    bank = 0
    curr_opacity=0
    mask_opacity=0
    consume_position = (10, 0)
    
    # Saving data for stability calculations
    #tar_count = 0
    #alt_count=0
    #con_count=0
    #all_count=0
    # keep track of which components have finished
    phase_2Components = [target_2, alternative_2, control_2, mouse_2, mask_2, consequence_2, bank_amount_2, bank_text_2, consume_2]
    for thisComponent in phase_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase_2"-------
    while continueRoutine:
        # get current time
        t = phase_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_2* updates
        if target_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            target_2.setAutoDraw(True)
        if target_2.status == STARTED:  # only update if drawing
            target_2.setOpacity(1)
            target_2.setPos((-cos(t*0.5)*0.75, cos(t*0.25)*0.4))
        
        # *alternative_2* updates
        if alternative_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            alternative_2.frameNStart = frameN  # exact frame index
            alternative_2.tStart = t  # local t and not account for scr refresh
            alternative_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative_2, 'tStartRefresh')  # time at next scr refresh
            alternative_2.setAutoDraw(True)
        if alternative_2.status == STARTED:  # only update if drawing
            alternative_2.setOpacity(1)
            alternative_2.setPos((cos(t*0.5)*0.75, (cos(t*-0.25+2.57)*-0.4)))
        
        # *control_2* updates
        if control_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            control_2.frameNStart = frameN  # exact frame index
            control_2.tStart = t  # local t and not account for scr refresh
            control_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(control_2, 'tStartRefresh')  # time at next scr refresh
            control_2.setAutoDraw(True)
        if control_2.status == STARTED:  # only update if drawing
            control_2.setOpacity(1)
            control_2.setPos((cos((t+2.57)*0.5)*0.75, cos(t*-0.25)*-0.4))
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.50-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target, alternative, control]:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                            mouse_2.clicked_pos.append(obj.pos)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
        
        # *mask_2* updates
        if mask_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mask_2.frameNStart = frameN  # exact frame index
            mask_2.tStart = t  # local t and not account for scr refresh
            mask_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask_2, 'tStartRefresh')  # time at next scr refresh
            mask_2.setAutoDraw(True)
        if mask_2.status == STARTED:  # only update if drawing
            mask_2.setOpacity(mask_opacity)
        #if mouse.isPressedIn(target_2):
        #    tar_count+=1
        #    all_count +=1
        
        if mouse.isPressedIn(alternative_2):
            consume_position=(0, 0)
            curr_opacity=1
            mask_opacity=1
        #    alt_count+=1
        #    all_count+=1
            play_sound()
        
        #if mouse.isPressedIn(control_2):
        #    con_count+=1
        #    all_count+=1
        
        if mouse.isPressedIn(consume_2):
            consume_position=(10, 0)
            curr_opacity=0
            mask_opacity=0
            bank+=1
            ovr_bank+=1
          
        if timer.getTime()<=0:
            continueRoutine=False
        
        # *consequence_2* updates
        if consequence_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            consequence_2.frameNStart = frameN  # exact frame index
            consequence_2.tStart = t  # local t and not account for scr refresh
            consequence_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consequence_2, 'tStartRefresh')  # time at next scr refresh
            consequence_2.setAutoDraw(True)
        if consequence_2.status == STARTED:  # only update if drawing
            consequence_2.setOpacity(curr_opacity)
        
        # *bank_amount_2* updates
        if bank_amount_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_amount_2.frameNStart = frameN  # exact frame index
            bank_amount_2.tStart = t  # local t and not account for scr refresh
            bank_amount_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_amount_2, 'tStartRefresh')  # time at next scr refresh
            bank_amount_2.setAutoDraw(True)
        if bank_amount_2.status == STARTED:  # only update if drawing
            bank_amount_2.setText(bank)
        
        # *bank_text_2* updates
        if bank_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_text_2.frameNStart = frameN  # exact frame index
            bank_text_2.tStart = t  # local t and not account for scr refresh
            bank_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_text_2, 'tStartRefresh')  # time at next scr refresh
            bank_text_2.setAutoDraw(True)
        
        # *consume_2* updates
        if consume_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consume_2.frameNStart = frameN  # exact frame index
            consume_2.tStart = t  # local t and not account for scr refresh
            consume_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consume_2, 'tStartRefresh')  # time at next scr refresh
            consume_2.setAutoDraw(True)
        if consume_2.status == STARTED:  # only update if drawing
            consume_2.setOpacity(mask_opacity)
            consume_2.setPos(consume_position)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase_2"-------
    for thisComponent in phase_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ph_2_trials.addData('target_2.started', target_2.tStartRefresh)
    ph_2_trials.addData('target_2.stopped', target_2.tStopRefresh)
    ph_2_trials.addData('alternative_2.started', alternative_2.tStartRefresh)
    ph_2_trials.addData('alternative_2.stopped', alternative_2.tStopRefresh)
    ph_2_trials.addData('control_2.started', control_2.tStartRefresh)
    ph_2_trials.addData('control_2.stopped', control_2.tStopRefresh)
    # store data for ph_2_trials (TrialHandler)
    ph_2_trials.addData('mouse_2.x', mouse_2.x)
    ph_2_trials.addData('mouse_2.y', mouse_2.y)
    ph_2_trials.addData('mouse_2.leftButton', mouse_2.leftButton)
    ph_2_trials.addData('mouse_2.midButton', mouse_2.midButton)
    ph_2_trials.addData('mouse_2.rightButton', mouse_2.rightButton)
    ph_2_trials.addData('mouse_2.time', mouse_2.time)
    ph_2_trials.addData('mouse_2.clicked_name', mouse_2.clicked_name)
    ph_2_trials.addData('mouse_2.clicked_pos', mouse_2.clicked_pos)
    ph_2_trials.addData('mouse_2.started', mouse_2.tStart)
    ph_2_trials.addData('mouse_2.stopped', mouse_2.tStop)
    ph_2_trials.addData('mask_2.started', mask_2.tStartRefresh)
    ph_2_trials.addData('mask_2.stopped', mask_2.tStopRefresh)
    ph_2_trials.addData('consequence_2.started', consequence_2.tStartRefresh)
    ph_2_trials.addData('consequence_2.stopped', consequence_2.tStopRefresh)
    ph_2_trials.addData('bank_amount_2.started', bank_amount_2.tStartRefresh)
    ph_2_trials.addData('bank_amount_2.stopped', bank_amount_2.tStopRefresh)
    ph_2_trials.addData('bank_text_2.started', bank_text_2.tStartRefresh)
    ph_2_trials.addData('bank_text_2.stopped', bank_text_2.tStopRefresh)
    ph_2_trials.addData('consume_2.started', consume_2.tStartRefresh)
    ph_2_trials.addData('consume_2.stopped', consume_2.tStopRefresh)
    # the Routine "phase_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'ph_2_trials'


# ------Prepare to start Routine "ici_2"-------
continueRoutine = True
# update component parameters for each repeat
begin_ph3.keys = []
begin_ph3.rt = []
_begin_ph3_allKeys = []
# keep track of which components have finished
ici_2Components = [ici_2_text, click_ph3, begin_ph3]
for thisComponent in ici_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ici_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ici_2"-------
while continueRoutine:
    # get current time
    t = ici_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ici_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ici_2_text* updates
    if ici_2_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ici_2_text.frameNStart = frameN  # exact frame index
        ici_2_text.tStart = t  # local t and not account for scr refresh
        ici_2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ici_2_text, 'tStartRefresh')  # time at next scr refresh
        ici_2_text.setAutoDraw(True)
    if ici_2_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ici_2_text.tStartRefresh + 5.00-frameTolerance:
            # keep track of stop time/frame for later
            ici_2_text.tStop = t  # not accounting for scr refresh
            ici_2_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ici_2_text, 'tStopRefresh')  # time at next scr refresh
            ici_2_text.setAutoDraw(False)
    
    # *click_ph3* updates
    if click_ph3.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        click_ph3.frameNStart = frameN  # exact frame index
        click_ph3.tStart = t  # local t and not account for scr refresh
        click_ph3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(click_ph3, 'tStartRefresh')  # time at next scr refresh
        click_ph3.setAutoDraw(True)
    
    # *begin_ph3* updates
    waitOnFlip = False
    if begin_ph3.status == NOT_STARTED and tThisFlip >= 6.00-frameTolerance:
        # keep track of start time/frame for later
        begin_ph3.frameNStart = frameN  # exact frame index
        begin_ph3.tStart = t  # local t and not account for scr refresh
        begin_ph3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_ph3, 'tStartRefresh')  # time at next scr refresh
        begin_ph3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_ph3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_ph3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_ph3.status == STARTED and not waitOnFlip:
        theseKeys = begin_ph3.getKeys(keyList=['space'], waitRelease=False)
        _begin_ph3_allKeys.extend(theseKeys)
        if len(_begin_ph3_allKeys):
            begin_ph3.keys = _begin_ph3_allKeys[-1].name  # just the last key pressed
            begin_ph3.rt = _begin_ph3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ici_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ici_2"-------
for thisComponent in ici_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ici_2_text.started', ici_2_text.tStartRefresh)
thisExp.addData('ici_2_text.stopped', ici_2_text.tStopRefresh)
thisExp.addData('click_ph3.started', click_ph3.tStartRefresh)
thisExp.addData('click_ph3.stopped', click_ph3.tStopRefresh)
# check responses
if begin_ph3.keys in ['', [], None]:  # No response was made
    begin_ph3.keys = None
thisExp.addData('begin_ph3.keys',begin_ph3.keys)
if begin_ph3.keys != None:  # we had a response
    thisExp.addData('begin_ph3.rt', begin_ph3.rt)
thisExp.addData('begin_ph3.started', begin_ph3.tStartRefresh)
thisExp.addData('begin_ph3.stopped', begin_ph3.tStopRefresh)
thisExp.nextEntry()
# the Routine "ici_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ph_3_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_file.csv'),
    seed=None, name='ph_3_trials')
thisExp.addLoop(ph_3_trials)  # add the loop to the experiment
thisPh_3_trial = ph_3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPh_3_trial.rgb)
if thisPh_3_trial != None:
    for paramName in thisPh_3_trial:
        exec('{} = thisPh_3_trial[paramName]'.format(paramName))

for thisPh_3_trial in ph_3_trials:
    currentLoop = ph_3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPh_3_trial.rgb)
    if thisPh_3_trial != None:
        for paramName in thisPh_3_trial:
            exec('{} = thisPh_3_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phase_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    mouse_3.clicked_name = []
    mouse_3.clicked_pos = []
    gotValidClick = False  # until a click is received
    mouse_3.mouseClock.reset()
    timer = core.CountdownTimer(5)
    bank = 0
    curr_opacity=0
    mask_opacity=0
    consume_position = (10, 0)
    #
    #target_count = 0
    #alt_count=0
    #control_count=0
    # keep track of which components have finished
    phase_3Components = [target_3, alternative_3, control_3, mouse_3, bank_amount_3, bank_text_3]
    for thisComponent in phase_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phase_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phase_3"-------
    while continueRoutine:
        # get current time
        t = phase_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phase_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_3* updates
        if target_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            target_3.frameNStart = frameN  # exact frame index
            target_3.tStart = t  # local t and not account for scr refresh
            target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_3, 'tStartRefresh')  # time at next scr refresh
            target_3.setAutoDraw(True)
        if target_3.status == STARTED:  # only update if drawing
            target_3.setPos((-cos(t*0.5)*0.75, cos(t*0.25)*0.4))
        
        # *alternative_3* updates
        if alternative_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            alternative_3.frameNStart = frameN  # exact frame index
            alternative_3.tStart = t  # local t and not account for scr refresh
            alternative_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative_3, 'tStartRefresh')  # time at next scr refresh
            alternative_3.setAutoDraw(True)
        if alternative_3.status == STARTED:  # only update if drawing
            alternative_3.setPos((cos(t*0.5)*0.75, (cos(t*-0.25+2.57)*-0.4)))
        
        # *control_3* updates
        if control_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            control_3.frameNStart = frameN  # exact frame index
            control_3.tStart = t  # local t and not account for scr refresh
            control_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(control_3, 'tStartRefresh')  # time at next scr refresh
            control_3.setAutoDraw(True)
        if control_3.status == STARTED:  # only update if drawing
            control_3.setPos((cos((t+2.57)*0.5)*0.75, cos(t*-0.25)*-0.4))
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.50-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target, alternative, control]:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                            mouse_3.clicked_pos.append(obj.pos)
                    x, y = mouse_3.getPos()
                    mouse_3.x.append(x)
                    mouse_3.y.append(y)
                    buttons = mouse_3.getPressed()
                    mouse_3.leftButton.append(buttons[0])
                    mouse_3.midButton.append(buttons[1])
                    mouse_3.rightButton.append(buttons[2])
                    mouse_3.time.append(mouse_3.mouseClock.getTime())
        #if mouse.isPressedIn(target_3):
        #    target_count+=1
        #    control_count
        #
        #if mouse.isPressedIn(alternative_3):
        #    alt_count+=1
        #
        #if mouse.isPressedIn(control_3):
        #    control_count+=1
        
        if timer.getTime()<=0:
            continueRoutine=False
        
        # *bank_amount_3* updates
        if bank_amount_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_amount_3.frameNStart = frameN  # exact frame index
            bank_amount_3.tStart = t  # local t and not account for scr refresh
            bank_amount_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_amount_3, 'tStartRefresh')  # time at next scr refresh
            bank_amount_3.setAutoDraw(True)
        if bank_amount_3.status == STARTED:  # only update if drawing
            bank_amount_3.setText(bank)
        
        # *bank_text_3* updates
        if bank_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bank_text_3.frameNStart = frameN  # exact frame index
            bank_text_3.tStart = t  # local t and not account for scr refresh
            bank_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bank_text_3, 'tStartRefresh')  # time at next scr refresh
            bank_text_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phase_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phase_3"-------
    for thisComponent in phase_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ph_3_trials.addData('target_3.started', target_3.tStartRefresh)
    ph_3_trials.addData('target_3.stopped', target_3.tStopRefresh)
    ph_3_trials.addData('alternative_3.started', alternative_3.tStartRefresh)
    ph_3_trials.addData('alternative_3.stopped', alternative_3.tStopRefresh)
    ph_3_trials.addData('control_3.started', control_3.tStartRefresh)
    ph_3_trials.addData('control_3.stopped', control_3.tStopRefresh)
    # store data for ph_3_trials (TrialHandler)
    ph_3_trials.addData('mouse_3.x', mouse_3.x)
    ph_3_trials.addData('mouse_3.y', mouse_3.y)
    ph_3_trials.addData('mouse_3.leftButton', mouse_3.leftButton)
    ph_3_trials.addData('mouse_3.midButton', mouse_3.midButton)
    ph_3_trials.addData('mouse_3.rightButton', mouse_3.rightButton)
    ph_3_trials.addData('mouse_3.time', mouse_3.time)
    ph_3_trials.addData('mouse_3.clicked_name', mouse_3.clicked_name)
    ph_3_trials.addData('mouse_3.clicked_pos', mouse_3.clicked_pos)
    ph_3_trials.addData('mouse_3.started', mouse_3.tStart)
    ph_3_trials.addData('mouse_3.stopped', mouse_3.tStop)
    ph_3_trials.addData('bank_amount_3.started', bank_amount_3.tStartRefresh)
    ph_3_trials.addData('bank_amount_3.stopped', bank_amount_3.tStopRefresh)
    ph_3_trials.addData('bank_text_3.started', bank_text_3.tStartRefresh)
    ph_3_trials.addData('bank_text_3.stopped', bank_text_3.tStopRefresh)
    # the Routine "phase_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'ph_3_trials'


# ------Prepare to start Routine "end_text"-------
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
end_textComponents = [end_text_, ovr_bank_amount]
for thisComponent in end_textComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_text"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_textClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_textClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text_* updates
    if end_text_.status == NOT_STARTED and tThisFlip >= 0.50-frameTolerance:
        # keep track of start time/frame for later
        end_text_.frameNStart = frameN  # exact frame index
        end_text_.tStart = t  # local t and not account for scr refresh
        end_text_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text_, 'tStartRefresh')  # time at next scr refresh
        end_text_.setAutoDraw(True)
    if end_text_.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text_.tStartRefresh + 5.00-frameTolerance:
            # keep track of stop time/frame for later
            end_text_.tStop = t  # not accounting for scr refresh
            end_text_.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text_, 'tStopRefresh')  # time at next scr refresh
            end_text_.setAutoDraw(False)
    
    # *ovr_bank_amount* updates
    if ovr_bank_amount.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ovr_bank_amount.frameNStart = frameN  # exact frame index
        ovr_bank_amount.tStart = t  # local t and not account for scr refresh
        ovr_bank_amount.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ovr_bank_amount, 'tStartRefresh')  # time at next scr refresh
        ovr_bank_amount.setAutoDraw(True)
    if ovr_bank_amount.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ovr_bank_amount.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            ovr_bank_amount.tStop = t  # not accounting for scr refresh
            ovr_bank_amount.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ovr_bank_amount, 'tStopRefresh')  # time at next scr refresh
            ovr_bank_amount.setAutoDraw(False)
    if ovr_bank_amount.status == STARTED:  # only update if drawing
        ovr_bank_amount.setText(ovr_bank
)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_textComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_text"-------
for thisComponent in end_textComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text_.started', end_text_.tStartRefresh)
thisExp.addData('end_text_.stopped', end_text_.tStopRefresh)
thisExp.addData('ovr_bank_amount.started', ovr_bank_amount.tStartRefresh)
thisExp.addData('ovr_bank_amount.stopped', ovr_bank_amount.tStopRefresh)

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
