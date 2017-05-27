#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue May  9 16:09:49 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'context'  # from the Builder filename that created this script
expInfo = {u'mriMode': u'scan', u'session': u'001', u'participant': u'con000'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/memsql/Dropbox/Research/context/fmri-context-task/fmri.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
win.setColor('black')

sickPressInstr = "with your index finger"
notsickPressInstr = "with your middle finger"

instruction ='''Imagine that you are a health inspector trying to determine the cause of illness in different restaurants.''' \
+ ''' On each trial you will see the name of the restaurant and a particular food.''' \
+ ''' Your job is to predict whether a customer will get sick from eating the food.''' \
+ ''' The outcome may or may not depend on the particular restaurant the customer is in (you have to figure that out).''' \
+ ''' In some cases you will make predictions about the same food in different restaurants.

The experiment consists of 9 rounds. In each round, you will make 24 predictions about a different set of restaurants and foods.''' \
+ ''' After each prediction (except the last 4), you will receive feedback about whether or not the customer got sick.

Press %s if you believe the customer will get sick from eating the food.

Press %s if you believe the customer will NOT get sick.

You will have 3 seconds to press on each trial.''' % (sickPressInstr, notsickPressInstr)
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=instruction
,    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "new_run"
new_runClock = core.Clock()
import os

subjectFilename = os.path.join('itis', 'csv', expInfo['participant'] + '.csv')
print 'Loading from ', subjectFilename
runInstr = visual.TextStim(win=win, ori=0, name='runInstr',
    text='the text is set manually\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "waitForTrigger"
waitForTriggerClock = core.Clock()
fmriClock = core.Clock() # clock for syncing with fMRI scanner
# definitely log it!

#trigger = 'parallel'
trigger = 'usb'
if trigger == 'parallel':
    from psychopy import parallel 
elif trigger == 'usb':
    from psychopy.hardware.emulator import launchScan    

    # settings for launchScan:
    MR_settings = { 
        'TR': 2.5, # duration (sec) per volume
        'volumes': 141, # number of whole-brain 3D volumes / frames
        'sync': 'equal', # character to use as the sync timing event; assumed to come at start of a volume
        'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
        }


# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixationCross = visual.TextStim(win=win, ori=0, name='fixationCross',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import time

# constants
#
sickButton = '1' # index finger
notsickButton = '2' # middle finger

# log wall time
#
expInfo['expStartWallTime'] = time.ctime()

# psychopy only writes the data at the very end
# we want data with intermediate results
# so we have this thing that dumps to a .wtf-tile
# as the experiment is going on
#
streamingFilename = thisExp.dataFileName + '.wtf'
streamingFile = open(streamingFilename, 'a')
streamingDelim = ','

# get names of data columns
#
def getExpDataNames():
    names = thisExp._getAllParamNames()
    names.extend(thisExp.dataNames)
    # names from the extraInfo dictionary
    names.extend(thisExp._getExtraInfo()[0])
    return names

# write a header lines
#
def writeHeadersToStreamingFile():
    for heading in getExpDataNames():
        streamingFile.write(u'%s%s' % (heading, streamingDelim))
    streamingFile.write('\n')
    streamingFile.flush()

def flushEntryToStreamingFile(entry):
    for name in getExpDataNames():
        entry.keys()
        if name in entry.keys():
            ename = unicode(entry[name])
            if ',' in ename or '\n' in ename:
                fmt = u'"%s"%s'
            else:
                fmt = u'%s%s'
            streamingFile.write(fmt % (entry[name], streamingDelim))
        else:
            streamingFile.write(streamingDelim)
    streamingFile.write('\n')
    streamingFile.flush()

nextEntryToFlush = 0

# write entries that we haven't flushed yet
# this writes both to the .wtf file and to the mysql db
#
def flushEntries():
    global nextEntryToFlush

    # don't write anything during the initial run
    # that's b/c the number of columns can change
    #
    if runs.thisN == 0:
        return

    # if we're after the initial run, flush everything
    # that we haven't flushed yet
    #
    while nextEntryToFlush < len(thisExp.entries):
        flushEntryToStreamingFile(thisExp.entries[nextEntryToFlush])
        nextEntryToFlush += 1


trialInstrText = visual.TextStim(win=win, ori=0, name='trialInstrText',
    text='Predict whether the customer will get sick from this food.',    font='Arial',
    pos=[0, 0.8], height=0.075, wrapWidth=20,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
restaurantText = visual.TextStim(win=win, ori=0, name='restaurantText',
    text='default text',    font='Arial Bold',
    pos=[0, +0.35], height=0.1, wrapWidth=None,
    color='pink', colorSpace='rgb', opacity=1,
    depth=-4.0)
foodImg = visual.ImageStim(win=win, name='foodImg',
    image='sin', mask=None,
    ori=0, pos=[0, 0.0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sickImg = visual.ImageStim(win=win, name='sickImg',
    image=os.path.join('images', 'sick.png'), mask=None,
    ori=0, pos=[-0.6, -0.6], size=[0.3, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
notsickImg = visual.ImageStim(win=win, name='notsickImg',
    image=os.path.join('images', 'smiley.png'), mask=None,
    ori=0, pos=[+0.6, -0.6], size=[0.3, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
ITI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI')
sickHighlight = visual.TextStim(win=win, ori=0, name='sickHighlight',
    text='_',    font='Arial',
    pos=[-0.6, -0.35], height=1.0, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
notsickHighlight = visual.TextStim(win=win, ori=0, name='notsickHighlight',
    text='_',    font='Arial',
    pos=[0.6, -0.35], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)
correctText = visual.TextStim(win=win, ori=0, name='correctText',
    text='CORRECT',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-11.0)
wrongText = visual.TextStim(win=win, ori=0, name='wrongText',
    text='WRONG',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-12.0)
timeoutText = visual.TextStim(win=win, ori=0, name='timeoutText',
    text='TIMEOUT',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-13.0)
gotSickText = visual.TextStim(win=win, ori=0, name='gotSickText',
    text='The customer got sick!',    font='Arial',
    pos=[0, -0.55], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0)
didntGetSickText = visual.TextStim(win=win, ori=0, name='didntGetSickText',
    text="The customer didn't get sick!",    font='Arial',
    pos=[0, -0.55], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixationITIText = visual.TextStim(win=win, ori=0, name='fixationITIText',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0)

# Initialize components for Routine "test_warning"
test_warningClock = core.Clock()
testTrialsHeadsUp = visual.TextStim(win=win, ori=0, name='testTrialsHeadsUp',
    text='Beginning test phase.\n\nYou will not receive feedback on the following 4 trials.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import time

# constants
#
sickButton = '1' # index finger
notsickButton = '2' # middle finger

# log wall time
#
expInfo['expStartWallTime'] = time.ctime()

# psychopy only writes the data at the very end
# we want data with intermediate results
# so we have this thing that dumps to a .wtf-tile
# as the experiment is going on
#
streamingFilename = thisExp.dataFileName + '.wtf'
streamingFile = open(streamingFilename, 'a')
streamingDelim = ','

# get names of data columns
#
def getExpDataNames():
    names = thisExp._getAllParamNames()
    names.extend(thisExp.dataNames)
    # names from the extraInfo dictionary
    names.extend(thisExp._getExtraInfo()[0])
    return names

# write a header lines
#
def writeHeadersToStreamingFile():
    for heading in getExpDataNames():
        streamingFile.write(u'%s%s' % (heading, streamingDelim))
    streamingFile.write('\n')
    streamingFile.flush()

def flushEntryToStreamingFile(entry):
    for name in getExpDataNames():
        entry.keys()
        if name in entry.keys():
            ename = unicode(entry[name])
            if ',' in ename or '\n' in ename:
                fmt = u'"%s"%s'
            else:
                fmt = u'%s%s'
            streamingFile.write(fmt % (entry[name], streamingDelim))
        else:
            streamingFile.write(streamingDelim)
    streamingFile.write('\n')
    streamingFile.flush()

nextEntryToFlush = 0

# write entries that we haven't flushed yet
# this writes both to the .wtf file and to the mysql db
#
def flushEntries():
    global nextEntryToFlush

    # don't write anything during the initial run
    # that's b/c the number of columns can change
    #
    if runs.thisN == 0:
        return

    # if we're after the initial run, flush everything
    # that we haven't flushed yet
    #
    while nextEntryToFlush < len(thisExp.entries):
        flushEntryToStreamingFile(thisExp.entries[nextEntryToFlush])
        nextEntryToFlush += 1


trialInstrText = visual.TextStim(win=win, ori=0, name='trialInstrText',
    text='Predict whether the customer will get sick from this food.',    font='Arial',
    pos=[0, 0.8], height=0.075, wrapWidth=20,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
restaurantText = visual.TextStim(win=win, ori=0, name='restaurantText',
    text='default text',    font='Arial Bold',
    pos=[0, +0.35], height=0.1, wrapWidth=None,
    color='pink', colorSpace='rgb', opacity=1,
    depth=-4.0)
foodImg = visual.ImageStim(win=win, name='foodImg',
    image='sin', mask=None,
    ori=0, pos=[0, 0.0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sickImg = visual.ImageStim(win=win, name='sickImg',
    image=os.path.join('images', 'sick.png'), mask=None,
    ori=0, pos=[-0.6, -0.6], size=[0.3, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
notsickImg = visual.ImageStim(win=win, name='notsickImg',
    image=os.path.join('images', 'smiley.png'), mask=None,
    ori=0, pos=[+0.6, -0.6], size=[0.3, 0.45],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
ITI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI')
sickHighlight = visual.TextStim(win=win, ori=0, name='sickHighlight',
    text='_',    font='Arial',
    pos=[-0.6, -0.35], height=1.0, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)
notsickHighlight = visual.TextStim(win=win, ori=0, name='notsickHighlight',
    text='_',    font='Arial',
    pos=[0.6, -0.35], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)
correctText = visual.TextStim(win=win, ori=0, name='correctText',
    text='CORRECT',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-11.0)
wrongText = visual.TextStim(win=win, ori=0, name='wrongText',
    text='WRONG',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-12.0)
timeoutText = visual.TextStim(win=win, ori=0, name='timeoutText',
    text='TIMEOUT',    font='Arial Bold',
    pos=[0, -0.4], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-13.0)
gotSickText = visual.TextStim(win=win, ori=0, name='gotSickText',
    text='The customer got sick!',    font='Arial',
    pos=[0, -0.55], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0)
didntGetSickText = visual.TextStim(win=win, ori=0, name='didntGetSickText',
    text="The customer didn't get sick!",    font='Arial',
    pos=[0, -0.55], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixationITIText = visual.TextStim(win=win, ori=0, name='fixationITIText',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0)

# Initialize components for Routine "Fixation_2"
Fixation_2Clock = core.Clock()
fixationCross_2 = visual.TextStim(win=win, ori=0, name='fixationCross_2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "thankyou"
thankyouClock = core.Clock()
if expInfo['mriMode'] != 'off': # we're scanning!
    assert expInfo['mriMode'] == 'scan'
    thankYouMsg = "You have completed the experiment. Please wait for the researcher."
else: # not scanning => behavioral
    thankYouMsg = "You have completed the experiment. Please open the door and wait for your researcher."


thankYouText = visual.TextStim(win=win, ori=0, name='thankYouText',
    text=thankYouMsg,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

startExpResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
startExpResp.status = NOT_STARTED
# keep track of which components have finished
instrComponents = []
instrComponents.append(instrText)
instrComponents.append(startExpResp)
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *startExpResp* updates
    if t >= 0 and startExpResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        startExpResp.tStart = t  # underestimates by a little under one frame
        startExpResp.frameNStart = frameN  # exact frame index
        startExpResp.status = STARTED
        # keyboard checking is just starting
        startExpResp.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if startExpResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            startExpResp.keys = theseKeys[-1]  # just the last key pressed
            startExpResp.rt = startExpResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if startExpResp.keys in ['', [], None]:  # No response was made
   startExpResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('startExpResp.keys',startExpResp.keys)
if startExpResp.keys != None:  # we had a response
    thisExp.addData('startExpResp.rt', startExpResp.rt)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/memsql/Dropbox/Research/context/fmri-context-task/fmri.psyexp',
    trialList=data.importConditions(subjectFilename),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    #------Prepare to start Routine "new_run"-------
    t = 0
    new_runClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    runInstr.setText("Beginning round #" + str(runs.thisN + 1))
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    new_runComponents = []
    new_runComponents.append(runInstr)
    new_runComponents.append(key_resp_3)
    for thisComponent in new_runComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "new_run"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = new_runClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *runInstr* updates
        if t >= 0.0 and runInstr.status == NOT_STARTED:
            # keep track of start time/frame for later
            runInstr.tStart = t  # underestimates by a little under one frame
            runInstr.frameNStart = frameN  # exact frame index
            runInstr.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in new_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "new_run"-------
    for thisComponent in new_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for runs (TrialHandler)
    runs.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        runs.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "new_run" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "waitForTrigger"-------
    t = 0
    waitForTriggerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if expInfo['mriMode'] != 'off': # or 'scan' !
        assert expInfo['mriMode'] == 'scan'
    
        if trigger == 'usb':
            vol = launchScan(win, MR_settings, 
                  globalClock=fmriClock, # <-- how you know the time! 
                  mode=expInfo['mriMode']) # <-- mode passed in
        elif trigger == 'parallel':
            parallel.setPortAddress(0x378)
            pin = 10; wait_msg = "Waiting for scanner..."
            pinStatus = parallel.readPin(pin)
            waitMsgStim = visual.TextStim(win, color='DarkGray', text=wait_msg)
            waitMsgStim.draw()
            win.flip()
            while True:
                if pinStatus != parallel.readPin(pin) or len(event.getKeys('esc')):
                   break
                   # start exp when pin values change
            globalClock.reset()
            logging.defaultClock.reset()
            logging.exp('parallel trigger: start of scan')
            win.flip()  # blank the screen on first sync pulse received
    else:
        fmriClock.reset()
    
    expInfo['triggerWallTime'] = time.ctime()
    core.wait(1)
    # keep track of which components have finished
    waitForTriggerComponents = []
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "waitForTrigger"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = waitForTriggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitForTriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "waitForTrigger"-------
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    routineTimer.reset()
    # the Routine "waitForTrigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Fixation"-------
    t = 0
    FixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = []
    FixationComponents.append(fixationCross)
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationCross* updates
        if t >= 0.0 and fixationCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross.tStart = t  # underestimates by a little under one frame
            fixationCross.frameNStart = frameN  # exact frame index
            fixationCross.setAutoDraw(True)
        if fixationCross.status == STARTED and t >= (0.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixationCross.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Fixation"-------
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    train_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=u'/Users/memsql/Dropbox/Research/context/fmri-context-task/fmri.psyexp',
        trialList=data.importConditions(runFilename, selection='range(0, 20)'),
        seed=None, name='train_trials')
    thisExp.addLoop(train_trials)  # add the loop to the experiment
    thisTrain_trial = train_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrain_trial.rgb)
    if thisTrain_trial != None:
        for paramName in thisTrain_trial.keys():
            exec(paramName + '= thisTrain_trial.' + paramName)
    
    for thisTrain_trial in train_trials:
        currentLoop = train_trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_trial.rgb)
        if thisTrain_trial != None:
            for paramName in thisTrain_trial.keys():
                exec(paramName + '= thisTrain_trial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # log some times
        #
        train_trials.addData('trialStartWallTime', time.ctime())
        train_trials.addData('actualChoiceOnset', fmriClock.getTime())
        
        #
        # ------------------ Feedback code -------------------
        #
        
        # clear the feedback
        #
        isFeedbackShown = False
        correctText.setOpacity(0)
        wrongText.setOpacity(0)
        timeoutText.setOpacity(0)
        gotSickText.setOpacity(0)
        didntGetSickText.setOpacity(0)
        
        # hack to re-render the feedback texts with new opacity
        #
        correctText.setText(correctText.text)
        wrongText.setText(wrongText.text)
        timeoutText.setText(timeoutText.text)
        gotSickText.setText(gotSickText.text)
        didntGetSickText.setText(didntGetSickText.text)
        
        #
        # ------------ Choice Highlight Code ----------------
        #
        
        # don't highlight the choices initially
        #
        sickHighlight.setOpacity(0)
        notsickHighlight.setOpacity(0)
        
        # hack to re-render the highlight underscores with new opacity
        sickHighlight.setText(sickHighlight.text)
        notsickHighlight.setText(notsickHighlight.text)
        
        # track whether subject has responded so we can record response time
        # also initialize the response time by 3 (== timeout)
        # respTime is also used to terminate the relevant elements in the GUI
        # also used for feedback timing
        #
        respTime = choiceDuration # by default it's timeout
        
        # calculate the ITI, assuming trial will timeout.
        # we later change it to the actual ITI when the subject responds
        # note that we need to adjust for psychopy drift
        #
        timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
        actualItiDuration = timeLeftUntilItiOffset - (choiceDuration + isiDuration + feedbackDuration)
        print '   now = ', fmriClock.getTime()
        print '   itiOffset = ', itiOffset
        print '   expected iti duration = ', itiDuration
        print '   initial actual ITI duration = ', actualItiDuration
        itiDriftAdjustment = actualItiDuration - itiDuration
        print '           adjustment = ', itiDriftAdjustment 
        if actualItiDuration < 0:
            actualItiDuration = 0 # worst case scenario... if we've drifted too far
        
        
        hasResponded = False
        lastReponseKey = None
        
        responseKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseKey.status = NOT_STARTED
        restaurantText.setText(restaurant)
        foodImg.setImage(os.path.join('foods', food))
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(responseKey)
        trialComponents.append(trialInstrText)
        trialComponents.append(restaurantText)
        trialComponents.append(foodImg)
        trialComponents.append(sickImg)
        trialComponents.append(notsickImg)
        trialComponents.append(ITI)
        trialComponents.append(sickHighlight)
        trialComponents.append(notsickHighlight)
        trialComponents.append(correctText)
        trialComponents.append(wrongText)
        trialComponents.append(timeoutText)
        trialComponents.append(gotSickText)
        trialComponents.append(didntGetSickText)
        trialComponents.append(ISI)
        trialComponents.append(fixationITIText)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # highlight subject's response and log the response time
            #
            if responseKey.keys and not hasResponded:
                hasResponded = True
            
                # only terminate early in training mode
                #
                if not isTest:
                    # set respTime to terminate the relevant elements in the GUI
                    #
                    respTime = responseKey.rt
            
                    # see how much time we have left for the ITI
                    #
                    timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
                    actualItiDuration = timeLeftUntilItiOffset - (isiDuration + feedbackDuration)
                    print '      final ITI = ', actualItiDuration
                    itiDriftAdjustment = actualItiDuration - (choiceDuration - respTime) - itiDuration
                    print '           adjustment = ', itiDriftAdjustment 
                    if actualItiDuration < 0:
                        actualItiDuration = 0 # worst case scenario... if we've drifted too far
            
                # log some stuffs
                #
                train_trials.addData('actualChoiceOffset', fmriClock.getTime())
                train_trials.addData('actualIsiOnset', fmriClock.getTime())
                train_trials.addData('responseTime', respTime)
                train_trials.addData('actualItiDuration', actualItiDuration)
                train_trials.addData('itiDriftAdjustment', itiDriftAdjustment)
            
                # highlight choice
                #
                if responseKey.keys == sickButton: # sick
                    sickHighlight.opacity = 1
                    notsickHighlight.opacity = 0
                elif responseKey.keys == notsickButton: # not sick
                    sickHighlight.opacity = 0
                    notsickHighlight.opacity = 1
                else:
                    assert False, 'Can only have one response, sick or not sick'
                
                # save last response so we don't re-render
                # deprecated -- we only remember the last choice
                #
                lastReponseKey = responseKey.keys
            
                # hack to re-render the text with new opacity
                #
                sickHighlight.setText(sickHighlight.text)
                notsickHighlight.setText(notsickHighlight.text)
            
            
            
            # show user some feedback, and log the ISI / feedback times
            #
            if t >= respTime + isiDuration and not isFeedbackShown:
                isFeedbackShown = True
                print '      Feedback time: ', t
            
                # log some times
                #
                train_trials.addData('actualIsiOffset', fmriClock.getTime())
                train_trials.addData('actualFeedbackOnset', fmriClock.getTime())
                train_trials.addData('actualFeedbackOffset', fmriClock.getTime() + feedbackDuration)
                train_trials.addData('actualItiOnset', fmriClock.getTime() + feedbackDuration)
            
                if not responseKey.keys:
                    # no response was made => timeout
                    #
                    timeoutText.setOpacity(1)
                    timeoutText.setText(timeoutText.text)
                else:
                    # response was made => give feedback
                    #
                    if responseKey.corr == 1:
                        correctText.setOpacity(1)
                        wrongText.setOpacity(0)
                    elif responseKey.corr == 0:
                        correctText.setOpacity(0)
                        wrongText.setOpacity(1)
                    else:
                        print responseKey.corr
                        assert False, "responseKey.corr = 0 or 1"
            
                    if isSick == 'True':
                        gotSickText.setOpacity(1)
                        didntGetSickText.setOpacity(0)
                    elif isSick == 'False':
                        gotSickText.setOpacity(0)
                        didntGetSickText.setOpacity(1)
                    else:
                        assert isTest
             
                    # hack to redraw the texts with new opacity
                    #
                    correctText.setText(correctText.text)
                    wrongText.setText(wrongText.text)
                    gotSickText.setText(gotSickText.text)
                    didntGetSickText.setText(didntGetSickText.text)
            
            
            
            # *responseKey* updates
            if t >= 0 and responseKey.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseKey.tStart = t  # underestimates by a little under one frame
                responseKey.frameNStart = frameN  # exact frame index
                responseKey.status = STARTED
                # keyboard checking is just starting
                responseKey.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseKey.status == STARTED and t >= (0 + (respTime-win.monitorFramePeriod*0.75)): #most of one frame period left
                responseKey.status = STOPPED
            if responseKey.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseKey.keys == []:  # then this was the first keypress
                        responseKey.keys = theseKeys[0]  # just the first key pressed
                        responseKey.rt = responseKey.clock.getTime()
                        # was this 'correct'?
                        if (responseKey.keys == str(corrButton)) or (responseKey.keys == corrButton):
                            responseKey.corr = 1
                        else:
                            responseKey.corr = 0
            
            # *trialInstrText* updates
            if t >= 0 and trialInstrText.status == NOT_STARTED:
                # keep track of start time/frame for later
                trialInstrText.tStart = t  # underestimates by a little under one frame
                trialInstrText.frameNStart = frameN  # exact frame index
                trialInstrText.setAutoDraw(True)
            if trialInstrText.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                trialInstrText.setAutoDraw(False)
            
            # *restaurantText* updates
            if t >= 0 and restaurantText.status == NOT_STARTED:
                # keep track of start time/frame for later
                restaurantText.tStart = t  # underestimates by a little under one frame
                restaurantText.frameNStart = frameN  # exact frame index
                restaurantText.setAutoDraw(True)
            if restaurantText.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                restaurantText.setAutoDraw(False)
            
            # *foodImg* updates
            if t >= 0 and foodImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                foodImg.tStart = t  # underestimates by a little under one frame
                foodImg.frameNStart = frameN  # exact frame index
                foodImg.setAutoDraw(True)
            if foodImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                foodImg.setAutoDraw(False)
            
            # *sickImg* updates
            if t >= 0 and sickImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                sickImg.tStart = t  # underestimates by a little under one frame
                sickImg.frameNStart = frameN  # exact frame index
                sickImg.setAutoDraw(True)
            if sickImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                sickImg.setAutoDraw(False)
            
            # *notsickImg* updates
            if t >= 0 and notsickImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                notsickImg.tStart = t  # underestimates by a little under one frame
                notsickImg.frameNStart = frameN  # exact frame index
                notsickImg.setAutoDraw(True)
            if notsickImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                notsickImg.setAutoDraw(False)
            
            # *sickHighlight* updates
            if t >= 0 and sickHighlight.status == NOT_STARTED:
                # keep track of start time/frame for later
                sickHighlight.tStart = t  # underestimates by a little under one frame
                sickHighlight.frameNStart = frameN  # exact frame index
                sickHighlight.setAutoDraw(True)
            if sickHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                sickHighlight.setAutoDraw(False)
            
            # *notsickHighlight* updates
            if t >= 0 and notsickHighlight.status == NOT_STARTED:
                # keep track of start time/frame for later
                notsickHighlight.tStart = t  # underestimates by a little under one frame
                notsickHighlight.frameNStart = frameN  # exact frame index
                notsickHighlight.setAutoDraw(True)
            if notsickHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                notsickHighlight.setAutoDraw(False)
            
            # *correctText* updates
            if t >= respTime + isiDuration and correctText.status == NOT_STARTED:
                # keep track of start time/frame for later
                correctText.tStart = t  # underestimates by a little under one frame
                correctText.frameNStart = frameN  # exact frame index
                correctText.setAutoDraw(True)
            if correctText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                correctText.setAutoDraw(False)
            
            # *wrongText* updates
            if t >= respTime + isiDuration and wrongText.status == NOT_STARTED:
                # keep track of start time/frame for later
                wrongText.tStart = t  # underestimates by a little under one frame
                wrongText.frameNStart = frameN  # exact frame index
                wrongText.setAutoDraw(True)
            if wrongText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                wrongText.setAutoDraw(False)
            
            # *timeoutText* updates
            if t >= respTime + isiDuration and timeoutText.status == NOT_STARTED:
                # keep track of start time/frame for later
                timeoutText.tStart = t  # underestimates by a little under one frame
                timeoutText.frameNStart = frameN  # exact frame index
                timeoutText.setAutoDraw(True)
            if timeoutText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                timeoutText.setAutoDraw(False)
            
            # *gotSickText* updates
            if t >= respTime + isiDuration and gotSickText.status == NOT_STARTED:
                # keep track of start time/frame for later
                gotSickText.tStart = t  # underestimates by a little under one frame
                gotSickText.frameNStart = frameN  # exact frame index
                gotSickText.setAutoDraw(True)
            if gotSickText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                gotSickText.setAutoDraw(False)
            
            # *didntGetSickText* updates
            if t >= respTime + isiDuration and didntGetSickText.status == NOT_STARTED:
                # keep track of start time/frame for later
                didntGetSickText.tStart = t  # underestimates by a little under one frame
                didntGetSickText.frameNStart = frameN  # exact frame index
                didntGetSickText.setAutoDraw(True)
            if didntGetSickText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                didntGetSickText.setAutoDraw(False)
            
            # *fixationITIText* updates
            if t >= respTime + isiDuration + feedbackDuration and fixationITIText.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationITIText.tStart = t  # underestimates by a little under one frame
                fixationITIText.frameNStart = frameN  # exact frame index
                fixationITIText.setAutoDraw(True)
            if fixationITIText.status == STARTED and t >= (respTime + isiDuration + feedbackDuration + (actualItiDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixationITIText.setAutoDraw(False)
            # *ITI* period
            if t >= respTime + isiDuration + feedbackDuration and ITI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ITI.tStart = t  # underestimates by a little under one frame
                ITI.frameNStart = frameN  # exact frame index
                ITI.start(actualItiDuration)
            elif ITI.status == STARTED: #one frame should pass before updating params and completing
                ITI.complete() #finish the static period
            # *ISI* period
            if t >= respTime and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(isiDuration)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # log some times
        #
        train_trials.addData('trialEndWallTime', time.ctime())
        train_trials.addData('actualItiOffset', fmriClock.getTime())
        flushEntries()
        # check responses
        if responseKey.keys in ['', [], None]:  # No response was made
           responseKey.keys=None
           # was no response the correct answer?!
           if str(corrButton).lower() == 'none': responseKey.corr = 1  # correct non-response
           else: responseKey.corr = 0  # failed to respond (incorrectly)
        # store data for train_trials (TrialHandler)
        train_trials.addData('responseKey.keys',responseKey.keys)
        train_trials.addData('responseKey.corr', responseKey.corr)
        if responseKey.keys != None:  # we had a response
            train_trials.addData('responseKey.rt', responseKey.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'train_trials'
    
    
    #------Prepare to start Routine "test_warning"-------
    t = 0
    test_warningClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    test_warningComponents = []
    test_warningComponents.append(testTrialsHeadsUp)
    for thisComponent in test_warningComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test_warning"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test_warningClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testTrialsHeadsUp* updates
        if t >= 0.0 and testTrialsHeadsUp.status == NOT_STARTED:
            # keep track of start time/frame for later
            testTrialsHeadsUp.tStart = t  # underestimates by a little under one frame
            testTrialsHeadsUp.frameNStart = frameN  # exact frame index
            testTrialsHeadsUp.setAutoDraw(True)
        if testTrialsHeadsUp.status == STARTED and t >= (0.0 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            testTrialsHeadsUp.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_warningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test_warning"-------
    for thisComponent in test_warningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    test_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=u'/Users/memsql/Dropbox/Research/context/fmri-context-task/fmri.psyexp',
        trialList=data.importConditions(runFilename, selection='range(20, 24)'),
        seed=None, name='test_trials')
    thisExp.addLoop(test_trials)  # add the loop to the experiment
    thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial.keys():
            exec(paramName + '= thisTest_trial.' + paramName)
    
    for thisTest_trial in test_trials:
        currentLoop = test_trials
        # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
        if thisTest_trial != None:
            for paramName in thisTest_trial.keys():
                exec(paramName + '= thisTest_trial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # log some times
        #
        train_trials.addData('trialStartWallTime', time.ctime())
        train_trials.addData('actualChoiceOnset', fmriClock.getTime())
        
        #
        # ------------------ Feedback code -------------------
        #
        
        # clear the feedback
        #
        isFeedbackShown = False
        correctText.setOpacity(0)
        wrongText.setOpacity(0)
        timeoutText.setOpacity(0)
        gotSickText.setOpacity(0)
        didntGetSickText.setOpacity(0)
        
        # hack to re-render the feedback texts with new opacity
        #
        correctText.setText(correctText.text)
        wrongText.setText(wrongText.text)
        timeoutText.setText(timeoutText.text)
        gotSickText.setText(gotSickText.text)
        didntGetSickText.setText(didntGetSickText.text)
        
        #
        # ------------ Choice Highlight Code ----------------
        #
        
        # don't highlight the choices initially
        #
        sickHighlight.setOpacity(0)
        notsickHighlight.setOpacity(0)
        
        # hack to re-render the highlight underscores with new opacity
        sickHighlight.setText(sickHighlight.text)
        notsickHighlight.setText(notsickHighlight.text)
        
        # track whether subject has responded so we can record response time
        # also initialize the response time by 3 (== timeout)
        # respTime is also used to terminate the relevant elements in the GUI
        # also used for feedback timing
        #
        respTime = choiceDuration # by default it's timeout
        
        # calculate the ITI, assuming trial will timeout.
        # we later change it to the actual ITI when the subject responds
        # note that we need to adjust for psychopy drift
        #
        timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
        actualItiDuration = timeLeftUntilItiOffset - (choiceDuration + isiDuration + feedbackDuration)
        print '   now = ', fmriClock.getTime()
        print '   itiOffset = ', itiOffset
        print '   expected iti duration = ', itiDuration
        print '   initial actual ITI duration = ', actualItiDuration
        itiDriftAdjustment = actualItiDuration - itiDuration
        print '           adjustment = ', itiDriftAdjustment 
        if actualItiDuration < 0:
            actualItiDuration = 0 # worst case scenario... if we've drifted too far
        
        
        hasResponded = False
        lastReponseKey = None
        
        responseKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseKey.status = NOT_STARTED
        restaurantText.setText(restaurant)
        foodImg.setImage(os.path.join('foods', food))
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(responseKey)
        trialComponents.append(trialInstrText)
        trialComponents.append(restaurantText)
        trialComponents.append(foodImg)
        trialComponents.append(sickImg)
        trialComponents.append(notsickImg)
        trialComponents.append(ITI)
        trialComponents.append(sickHighlight)
        trialComponents.append(notsickHighlight)
        trialComponents.append(correctText)
        trialComponents.append(wrongText)
        trialComponents.append(timeoutText)
        trialComponents.append(gotSickText)
        trialComponents.append(didntGetSickText)
        trialComponents.append(ISI)
        trialComponents.append(fixationITIText)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # highlight subject's response and log the response time
            #
            if responseKey.keys and not hasResponded:
                hasResponded = True
            
                # only terminate early in training mode
                #
                if not isTest:
                    # set respTime to terminate the relevant elements in the GUI
                    #
                    respTime = responseKey.rt
            
                    # see how much time we have left for the ITI
                    #
                    timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
                    actualItiDuration = timeLeftUntilItiOffset - (isiDuration + feedbackDuration)
                    print '      final ITI = ', actualItiDuration
                    itiDriftAdjustment = actualItiDuration - (choiceDuration - respTime) - itiDuration
                    print '           adjustment = ', itiDriftAdjustment 
                    if actualItiDuration < 0:
                        actualItiDuration = 0 # worst case scenario... if we've drifted too far
            
                # log some stuffs
                #
                train_trials.addData('actualChoiceOffset', fmriClock.getTime())
                train_trials.addData('actualIsiOnset', fmriClock.getTime())
                train_trials.addData('responseTime', respTime)
                train_trials.addData('actualItiDuration', actualItiDuration)
                train_trials.addData('itiDriftAdjustment', itiDriftAdjustment)
            
                # highlight choice
                #
                if responseKey.keys == sickButton: # sick
                    sickHighlight.opacity = 1
                    notsickHighlight.opacity = 0
                elif responseKey.keys == notsickButton: # not sick
                    sickHighlight.opacity = 0
                    notsickHighlight.opacity = 1
                else:
                    assert False, 'Can only have one response, sick or not sick'
                
                # save last response so we don't re-render
                # deprecated -- we only remember the last choice
                #
                lastReponseKey = responseKey.keys
            
                # hack to re-render the text with new opacity
                #
                sickHighlight.setText(sickHighlight.text)
                notsickHighlight.setText(notsickHighlight.text)
            
            
            
            # show user some feedback, and log the ISI / feedback times
            #
            if t >= respTime + isiDuration and not isFeedbackShown:
                isFeedbackShown = True
                print '      Feedback time: ', t
            
                # log some times
                #
                train_trials.addData('actualIsiOffset', fmriClock.getTime())
                train_trials.addData('actualFeedbackOnset', fmriClock.getTime())
                train_trials.addData('actualFeedbackOffset', fmriClock.getTime() + feedbackDuration)
                train_trials.addData('actualItiOnset', fmriClock.getTime() + feedbackDuration)
            
                if not responseKey.keys:
                    # no response was made => timeout
                    #
                    timeoutText.setOpacity(1)
                    timeoutText.setText(timeoutText.text)
                else:
                    # response was made => give feedback
                    #
                    if responseKey.corr == 1:
                        correctText.setOpacity(1)
                        wrongText.setOpacity(0)
                    elif responseKey.corr == 0:
                        correctText.setOpacity(0)
                        wrongText.setOpacity(1)
                    else:
                        print responseKey.corr
                        assert False, "responseKey.corr = 0 or 1"
            
                    if isSick == 'True':
                        gotSickText.setOpacity(1)
                        didntGetSickText.setOpacity(0)
                    elif isSick == 'False':
                        gotSickText.setOpacity(0)
                        didntGetSickText.setOpacity(1)
                    else:
                        assert isTest
             
                    # hack to redraw the texts with new opacity
                    #
                    correctText.setText(correctText.text)
                    wrongText.setText(wrongText.text)
                    gotSickText.setText(gotSickText.text)
                    didntGetSickText.setText(didntGetSickText.text)
            
            
            
            # *responseKey* updates
            if t >= 0 and responseKey.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseKey.tStart = t  # underestimates by a little under one frame
                responseKey.frameNStart = frameN  # exact frame index
                responseKey.status = STARTED
                # keyboard checking is just starting
                responseKey.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseKey.status == STARTED and t >= (0 + (respTime-win.monitorFramePeriod*0.75)): #most of one frame period left
                responseKey.status = STOPPED
            if responseKey.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseKey.keys == []:  # then this was the first keypress
                        responseKey.keys = theseKeys[0]  # just the first key pressed
                        responseKey.rt = responseKey.clock.getTime()
                        # was this 'correct'?
                        if (responseKey.keys == str(corrButton)) or (responseKey.keys == corrButton):
                            responseKey.corr = 1
                        else:
                            responseKey.corr = 0
            
            # *trialInstrText* updates
            if t >= 0 and trialInstrText.status == NOT_STARTED:
                # keep track of start time/frame for later
                trialInstrText.tStart = t  # underestimates by a little under one frame
                trialInstrText.frameNStart = frameN  # exact frame index
                trialInstrText.setAutoDraw(True)
            if trialInstrText.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                trialInstrText.setAutoDraw(False)
            
            # *restaurantText* updates
            if t >= 0 and restaurantText.status == NOT_STARTED:
                # keep track of start time/frame for later
                restaurantText.tStart = t  # underestimates by a little under one frame
                restaurantText.frameNStart = frameN  # exact frame index
                restaurantText.setAutoDraw(True)
            if restaurantText.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                restaurantText.setAutoDraw(False)
            
            # *foodImg* updates
            if t >= 0 and foodImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                foodImg.tStart = t  # underestimates by a little under one frame
                foodImg.frameNStart = frameN  # exact frame index
                foodImg.setAutoDraw(True)
            if foodImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                foodImg.setAutoDraw(False)
            
            # *sickImg* updates
            if t >= 0 and sickImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                sickImg.tStart = t  # underestimates by a little under one frame
                sickImg.frameNStart = frameN  # exact frame index
                sickImg.setAutoDraw(True)
            if sickImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                sickImg.setAutoDraw(False)
            
            # *notsickImg* updates
            if t >= 0 and notsickImg.status == NOT_STARTED:
                # keep track of start time/frame for later
                notsickImg.tStart = t  # underestimates by a little under one frame
                notsickImg.frameNStart = frameN  # exact frame index
                notsickImg.setAutoDraw(True)
            if notsickImg.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                notsickImg.setAutoDraw(False)
            
            # *sickHighlight* updates
            if t >= 0 and sickHighlight.status == NOT_STARTED:
                # keep track of start time/frame for later
                sickHighlight.tStart = t  # underestimates by a little under one frame
                sickHighlight.frameNStart = frameN  # exact frame index
                sickHighlight.setAutoDraw(True)
            if sickHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                sickHighlight.setAutoDraw(False)
            
            # *notsickHighlight* updates
            if t >= 0 and notsickHighlight.status == NOT_STARTED:
                # keep track of start time/frame for later
                notsickHighlight.tStart = t  # underestimates by a little under one frame
                notsickHighlight.frameNStart = frameN  # exact frame index
                notsickHighlight.setAutoDraw(True)
            if notsickHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                notsickHighlight.setAutoDraw(False)
            
            # *correctText* updates
            if t >= respTime + isiDuration and correctText.status == NOT_STARTED:
                # keep track of start time/frame for later
                correctText.tStart = t  # underestimates by a little under one frame
                correctText.frameNStart = frameN  # exact frame index
                correctText.setAutoDraw(True)
            if correctText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                correctText.setAutoDraw(False)
            
            # *wrongText* updates
            if t >= respTime + isiDuration and wrongText.status == NOT_STARTED:
                # keep track of start time/frame for later
                wrongText.tStart = t  # underestimates by a little under one frame
                wrongText.frameNStart = frameN  # exact frame index
                wrongText.setAutoDraw(True)
            if wrongText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                wrongText.setAutoDraw(False)
            
            # *timeoutText* updates
            if t >= respTime + isiDuration and timeoutText.status == NOT_STARTED:
                # keep track of start time/frame for later
                timeoutText.tStart = t  # underestimates by a little under one frame
                timeoutText.frameNStart = frameN  # exact frame index
                timeoutText.setAutoDraw(True)
            if timeoutText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                timeoutText.setAutoDraw(False)
            
            # *gotSickText* updates
            if t >= respTime + isiDuration and gotSickText.status == NOT_STARTED:
                # keep track of start time/frame for later
                gotSickText.tStart = t  # underestimates by a little under one frame
                gotSickText.frameNStart = frameN  # exact frame index
                gotSickText.setAutoDraw(True)
            if gotSickText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                gotSickText.setAutoDraw(False)
            
            # *didntGetSickText* updates
            if t >= respTime + isiDuration and didntGetSickText.status == NOT_STARTED:
                # keep track of start time/frame for later
                didntGetSickText.tStart = t  # underestimates by a little under one frame
                didntGetSickText.frameNStart = frameN  # exact frame index
                didntGetSickText.setAutoDraw(True)
            if didntGetSickText.status == STARTED and t >= (respTime + isiDuration + (feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                didntGetSickText.setAutoDraw(False)
            
            # *fixationITIText* updates
            if t >= respTime + isiDuration + feedbackDuration and fixationITIText.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationITIText.tStart = t  # underestimates by a little under one frame
                fixationITIText.frameNStart = frameN  # exact frame index
                fixationITIText.setAutoDraw(True)
            if fixationITIText.status == STARTED and t >= (respTime + isiDuration + feedbackDuration + (actualItiDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixationITIText.setAutoDraw(False)
            # *ITI* period
            if t >= respTime + isiDuration + feedbackDuration and ITI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ITI.tStart = t  # underestimates by a little under one frame
                ITI.frameNStart = frameN  # exact frame index
                ITI.start(actualItiDuration)
            elif ITI.status == STARTED: #one frame should pass before updating params and completing
                ITI.complete() #finish the static period
            # *ISI* period
            if t >= respTime and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(isiDuration)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # log some times
        #
        train_trials.addData('trialEndWallTime', time.ctime())
        train_trials.addData('actualItiOffset', fmriClock.getTime())
        flushEntries()
        # check responses
        if responseKey.keys in ['', [], None]:  # No response was made
           responseKey.keys=None
           # was no response the correct answer?!
           if str(corrButton).lower() == 'none': responseKey.corr = 1  # correct non-response
           else: responseKey.corr = 0  # failed to respond (incorrectly)
        # store data for test_trials (TrialHandler)
        test_trials.addData('responseKey.keys',responseKey.keys)
        test_trials.addData('responseKey.corr', responseKey.corr)
        if responseKey.keys != None:  # we had a response
            test_trials.addData('responseKey.rt', responseKey.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'test_trials'
    
    
    #------Prepare to start Routine "Fixation_2"-------
    t = 0
    Fixation_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Fixation_2Components = []
    Fixation_2Components.append(fixationCross_2)
    for thisComponent in Fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Fixation_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationCross_2* updates
        if t >= 0.0 and fixationCross_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross_2.tStart = t  # underestimates by a little under one frame
            fixationCross_2.frameNStart = frameN  # exact frame index
            fixationCross_2.setAutoDraw(True)
        if fixationCross_2.status == STARTED and t >= (0.0 + (6.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixationCross_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Fixation_2"-------
    for thisComponent in Fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'runs'


#------Prepare to start Routine "thankyou"-------
t = 0
thankyouClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
thankyouComponents = []
thankyouComponents.append(thankYouText)
thankyouComponents.append(key_resp_2)
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thankyou"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = thankyouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *thankYouText* updates
    if t >= 0.0 and thankYouText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankYouText.tStart = t  # underestimates by a little under one frame
        thankYouText.frameNStart = frameN  # exact frame index
        thankYouText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thankyou"-------
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()








win.close()
core.quit()
