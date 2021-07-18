#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Sat Jul 17 09:13:14 2021
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
expInfo = {'Participant ID': '', 'Session': '001'}
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
    originPath='/Users/davidjcox/Dropbox (Personal)/Projects/Manuscripts In Progress/Empirical/Caldwell University/Resurgence/resurgence.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[3200, 1800], fullscr=True, screen=0, 
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
exposure_instructions = visual.TextStim(win=win, name='exposure_instructions',
    text='demo text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
phase_1_instr = visual.TextStim(win=win, name='phase_1_instr',
    text='phase 1 starting',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
exp_inst = visual.TextStim(win=win, name='exp_inst',
    text='< Initial experiment instructions > ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
start_exp_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
start_exp_resp.keys = []
start_exp_resp.rt = []
_start_exp_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [exposure_instructions, phase_1_instr, exp_inst, start_exp_resp, text]
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
    
    # *exposure_instructions* updates
    if exposure_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exposure_instructions.frameNStart = frameN  # exact frame index
        exposure_instructions.tStart = t  # local t and not account for scr refresh
        exposure_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exposure_instructions, 'tStartRefresh')  # time at next scr refresh
        exposure_instructions.setAutoDraw(True)
    
    # *phase_1_instr* updates
    if phase_1_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        phase_1_instr.frameNStart = frameN  # exact frame index
        phase_1_instr.tStart = t  # local t and not account for scr refresh
        phase_1_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(phase_1_instr, 'tStartRefresh')  # time at next scr refresh
        phase_1_instr.setAutoDraw(True)
    if phase_1_instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > phase_1_instr.tStartRefresh + 10.00-frameTolerance:
            # keep track of stop time/frame for later
            phase_1_instr.tStop = t  # not accounting for scr refresh
            phase_1_instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(phase_1_instr, 'tStopRefresh')  # time at next scr refresh
            phase_1_instr.setAutoDraw(False)
    
    # *exp_inst* updates
    if exp_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exp_inst.frameNStart = frameN  # exact frame index
        exp_inst.tStart = t  # local t and not account for scr refresh
        exp_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_inst, 'tStartRefresh')  # time at next scr refresh
        exp_inst.setAutoDraw(True)
    
    # *start_exp_resp* updates
    waitOnFlip = False
    if start_exp_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_exp_resp.frameNStart = frameN  # exact frame index
        start_exp_resp.tStart = t  # local t and not account for scr refresh
        start_exp_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_exp_resp, 'tStartRefresh')  # time at next scr refresh
        start_exp_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_exp_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_exp_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_exp_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_exp_resp.getKeys(keyList=['return'], waitRelease=False)
        _start_exp_resp_allKeys.extend(theseKeys)
        if len(_start_exp_resp_allKeys):
            start_exp_resp.keys = _start_exp_resp_allKeys[-1].name  # just the last key pressed
            start_exp_resp.rt = _start_exp_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
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
thisExp.addData('exposure_instructions.started', exposure_instructions.tStartRefresh)
thisExp.addData('exposure_instructions.stopped', exposure_instructions.tStopRefresh)
thisExp.addData('phase_1_instr.started', phase_1_instr.tStartRefresh)
thisExp.addData('phase_1_instr.stopped', phase_1_instr.tStopRefresh)
thisExp.addData('exp_inst.started', exp_inst.tStartRefresh)
thisExp.addData('exp_inst.stopped', exp_inst.tStopRefresh)
# check responses
if start_exp_resp.keys in ['', [], None]:  # No response was made
    start_exp_resp.keys = None
thisExp.addData('start_exp_resp.keys',start_exp_resp.keys)
if start_exp_resp.keys != None:  # we had a response
    thisExp.addData('start_exp_resp.rt', start_exp_resp.rt)
thisExp.addData('start_exp_resp.started', start_exp_resp.tStartRefresh)
thisExp.addData('start_exp_resp.stopped', start_exp_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
