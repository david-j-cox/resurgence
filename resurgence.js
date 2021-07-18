/******************* 
 * Resurgence Test *
 *******************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'resurgence';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin, practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);
flowScheduler.add(begin_iciRoutineBegin());
flowScheduler.add(begin_iciRoutineEachFrame());
flowScheduler.add(begin_iciRoutineEnd());
const ph_1_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ph_1_trialsLoopBegin, ph_1_trialsLoopScheduler);
flowScheduler.add(ph_1_trialsLoopScheduler);
flowScheduler.add(ph_1_trialsLoopEnd);
flowScheduler.add(ici_1RoutineBegin());
flowScheduler.add(ici_1RoutineEachFrame());
flowScheduler.add(ici_1RoutineEnd());
const ph_2_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ph_2_trialsLoopBegin, ph_2_trialsLoopScheduler);
flowScheduler.add(ph_2_trialsLoopScheduler);
flowScheduler.add(ph_2_trialsLoopEnd);
flowScheduler.add(ici_2RoutineBegin());
flowScheduler.add(ici_2RoutineEachFrame());
flowScheduler.add(ici_2RoutineEnd());
const ph_3_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ph_3_trialsLoopBegin, ph_3_trialsLoopScheduler);
flowScheduler.add(ph_3_trialsLoopScheduler);
flowScheduler.add(ph_3_trialsLoopEnd);
flowScheduler.add(end_textRoutineBegin());
flowScheduler.add(end_textRoutineEachFrame());
flowScheduler.add(end_textRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'chime.wav', 'path': 'chime.wav'},
    {'name': 'condition_file.csv', 'path': 'condition_file.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  new util.Clock()
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In the following phases, you will see three colored squares on the screen. Clicking on the squares may or may not result in points. Your point total will be shown in the upper right-hand corner of the screen. \n\nAt the end of the task, you will be awarded $0.01 per point earned. For example, if you earn 1000 points, you will receive $10.00. If you close the program, we will lose all data and your session will end. When you are ready to begin, press the space bar to begin this experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  exp_instr_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice"
  practiceClock = new util.Clock();
  target_p = new visual.Rect ({
    win: psychoJS.window, name: 'target_p', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), 1]),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  alternative_p = new visual.Rect ({
    win: psychoJS.window, name: 'alternative_p', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 0.294117647058824, (- 1)]),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  control_p = new visual.Rect ({
    win: psychoJS.window, name: 'control_p', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  mouse_p = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_p.mouseClock = new util.Clock();
  ovr_bank = 0;
  
  mask_p = new visual.Rect ({
    win: psychoJS.window, name: 'mask_p', 
    width: [10, 10][0], height: [10, 10][1],
    ori: 0, pos: [0, 0],
    lineWidth: 0, lineColor: new util.Color('grey'),
    fillColor: new util.Color('grey'),
    opacity: 1.0, depth: -5, interpolate: true,
  });
  
  consequence_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'consequence_p',
    text: '+1 Point',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -6.0 
  });
  
  bank_amount_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_amount_p',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.85, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  bank_text_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_text_p',
    text: 'Current Bank: ',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  consume_p = new visual.TextStim({
    win: psychoJS.window,
    name: 'consume_p',
    text: 'Click to collect. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -9.0 
  });
  
  // Initialize components for Routine "begin_ici"
  begin_iciClock = new util.Clock();
  begin_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'begin_text',
    text: 'It looks like you’re getting the hang of this!\n\nPlease wait while Phase 1 loads. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  click_ph1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'click_ph1',
    text: 'Press the space bar to continue to Phase 1. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  begin_ph1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "phase_1"
  phase_1Clock = new util.Clock();
  target = new visual.Rect ({
    win: psychoJS.window, name: 'target', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), 1]),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  alternative = new visual.Rect ({
    win: psychoJS.window, name: 'alternative', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 0.294117647058824, (- 1)]),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  control = new visual.Rect ({
    win: psychoJS.window, name: 'control', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  mask = new visual.Rect ({
    win: psychoJS.window, name: 'mask', 
    width: [10, 10][0], height: [10, 10][1],
    ori: 0, pos: [0, 0],
    lineWidth: 0, lineColor: new util.Color('grey'),
    fillColor: new util.Color('grey'),
    opacity: 1.0, depth: -4, interpolate: true,
  });
  
  ovr_bank = 0;
  
  consequence = new visual.TextStim({
    win: psychoJS.window,
    name: 'consequence',
    text: '+1 Point',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -6.0 
  });
  
  bank_amount = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_amount',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.85, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  bank_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_text',
    text: 'Phase 1 Bank: ',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  consume = new visual.TextStim({
    win: psychoJS.window,
    name: 'consume',
    text: 'Click to collect. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -9.0 
  });
  
  // Initialize components for Routine "ici_1"
  ici_1Clock = new util.Clock();
  ici_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ici_1_text',
    text: 'Phase 1 has ended. \nPlease wait while Phase 2 loads.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  click_ph2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'click_ph2',
    text: 'Press the space bar to begin Phase 2. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  begin_ph2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "phase_2"
  phase_2Clock = new util.Clock();
  target_2 = new visual.Rect ({
    win: psychoJS.window, name: 'target_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), 1]),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  alternative_2 = new visual.Rect ({
    win: psychoJS.window, name: 'alternative_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 0.294117647058824, (- 1)]),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  control_2 = new visual.Rect ({
    win: psychoJS.window, name: 'control_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  mask_2 = new visual.Rect ({
    win: psychoJS.window, name: 'mask_2', 
    width: [10, 10][0], height: [10, 10][1],
    ori: 0, pos: [0, 0],
    lineWidth: 0, lineColor: new util.Color('grey'),
    fillColor: new util.Color('grey'),
    opacity: 1.0, depth: -4, interpolate: true,
  });
  
  consequence_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'consequence_2',
    text: '+1 Point',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -6.0 
  });
  
  bank_amount_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_amount_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.85, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  bank_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_text_2',
    text: 'Phase 2 Bank: ',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  consume_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'consume_2',
    text: 'Click to collect. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1.0,
    depth: -9.0 
  });
  
  // Initialize components for Routine "ici_2"
  ici_2Clock = new util.Clock();
  ici_2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ici_2_text',
    text: 'Phase 2 has ended. \nPlease wait while Phase 3 loads.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  click_ph3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'click_ph3',
    text: 'Press the space bar to begin Phase 3. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  begin_ph3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "phase_3"
  phase_3Clock = new util.Clock();
  target_3 = new visual.Rect ({
    win: psychoJS.window, name: 'target_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  alternative_3 = new visual.Rect ({
    win: psychoJS.window, name: 'alternative_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 0.294117647058824, (- 1)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  control_3 = new visual.Rect ({
    win: psychoJS.window, name: 'control_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  
  
  bank_amount_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_amount_3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.85, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  bank_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'bank_text_3',
    text: 'Phase 3 Bank: ',
    font: 'Arial',
    units: undefined, 
    pos: [0.65, 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "end_text"
  end_textClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'Thank you for participating! This experiment has ended. The total amount of points you earned was: ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ovr_bank_amount = new visual.TextStim({
    win: psychoJS.window,
    name: 'ovr_bank_amount',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    exp_instr_resp.keys = undefined;
    exp_instr_resp.rt = undefined;
    _exp_instr_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text);
    instructionsComponents.push(exp_instr_resp);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.5 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *exp_instr_resp* updates
    if (t >= 0.5 && exp_instr_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exp_instr_resp.tStart = t;  // (not accounting for frame time here)
      exp_instr_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { exp_instr_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { exp_instr_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { exp_instr_resp.clearEvents(); });
    }

    if (exp_instr_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = exp_instr_resp.getKeys({keyList: ['space'], waitRelease: false});
      _exp_instr_resp_allKeys = _exp_instr_resp_allKeys.concat(theseKeys);
      if (_exp_instr_resp_allKeys.length > 0) {
        exp_instr_resp.keys = _exp_instr_resp_allKeys[_exp_instr_resp_allKeys.length - 1].name;  // just the last key pressed
        exp_instr_resp.rt = _exp_instr_resp_allKeys[_exp_instr_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('exp_instr_resp.keys', exp_instr_resp.keys);
    if (typeof exp_instr_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('exp_instr_resp.rt', exp_instr_resp.rt);
        routineTimer.reset();
        }
    
    exp_instr_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practice_trialsLoopBegin(practice_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_file.csv',
    seed: undefined, name: 'practice_trials'
  });
  psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
  currentLoop = practice_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice_trial of practice_trials) {
    const snapshot = practice_trials.getSnapshot();
    practice_trialsLoopScheduler.add(importConditions(snapshot));
    practice_trialsLoopScheduler.add(practiceRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(practiceRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(practiceRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(endLoopIteration(practice_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practice_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(practice_trials);

  return Scheduler.Event.NEXT;
}

function ph_1_trialsLoopBegin(ph_1_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ph_1_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_file.csv',
    seed: undefined, name: 'ph_1_trials'
  });
  psychoJS.experiment.addLoop(ph_1_trials); // add the loop to the experiment
  currentLoop = ph_1_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPh_1_trial of ph_1_trials) {
    const snapshot = ph_1_trials.getSnapshot();
    ph_1_trialsLoopScheduler.add(importConditions(snapshot));
    ph_1_trialsLoopScheduler.add(phase_1RoutineBegin(snapshot));
    ph_1_trialsLoopScheduler.add(phase_1RoutineEachFrame(snapshot));
    ph_1_trialsLoopScheduler.add(phase_1RoutineEnd(snapshot));
    ph_1_trialsLoopScheduler.add(endLoopIteration(ph_1_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function ph_1_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(ph_1_trials);

  return Scheduler.Event.NEXT;
}

function ph_2_trialsLoopBegin(ph_2_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ph_2_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_file.csv',
    seed: undefined, name: 'ph_2_trials'
  });
  psychoJS.experiment.addLoop(ph_2_trials); // add the loop to the experiment
  currentLoop = ph_2_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPh_2_trial of ph_2_trials) {
    const snapshot = ph_2_trials.getSnapshot();
    ph_2_trialsLoopScheduler.add(importConditions(snapshot));
    ph_2_trialsLoopScheduler.add(phase_2RoutineBegin(snapshot));
    ph_2_trialsLoopScheduler.add(phase_2RoutineEachFrame(snapshot));
    ph_2_trialsLoopScheduler.add(phase_2RoutineEnd(snapshot));
    ph_2_trialsLoopScheduler.add(endLoopIteration(ph_2_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function ph_2_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(ph_2_trials);

  return Scheduler.Event.NEXT;
}

function ph_3_trialsLoopBegin(ph_3_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ph_3_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_file.csv',
    seed: undefined, name: 'ph_3_trials'
  });
  psychoJS.experiment.addLoop(ph_3_trials); // add the loop to the experiment
  currentLoop = ph_3_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPh_3_trial of ph_3_trials) {
    const snapshot = ph_3_trials.getSnapshot();
    ph_3_trialsLoopScheduler.add(importConditions(snapshot));
    ph_3_trialsLoopScheduler.add(phase_3RoutineBegin(snapshot));
    ph_3_trialsLoopScheduler.add(phase_3RoutineEachFrame(snapshot));
    ph_3_trialsLoopScheduler.add(phase_3RoutineEnd(snapshot));
    ph_3_trialsLoopScheduler.add(endLoopIteration(ph_3_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function ph_3_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(ph_3_trials);

  return Scheduler.Event.NEXT;
}

function practiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice'-------
    t = 0;
    practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_p
    // current position of the mouse:
    mouse_p.x = [];
    mouse_p.y = [];
    mouse_p.leftButton = [];
    mouse_p.midButton = [];
    mouse_p.rightButton = [];
    mouse_p.time = [];
    mouse_p.clicked_name = [];
    mouse_p.clicked_pos = [];
    gotValidClick = false; // until a click is received
    mouse_p.mouseClock.reset();
    import {Sound} from 'psychopy/sound';
    var alt_count, bank, con_count, consume_position, curr_opacity, duration, mask_opacity, tar_count, timer;
    function play_sound() {
        var beep;
        beep = new sound.Sound("A", {"secs": 0.3});
        beep.setVolume(1);
        beep.play();
        core.wait(0.3);
    }
    duration = new util.Clock();
    timer = new util.CountdownTimer(60);
    tar_count = 0;
    alt_count = 0;
    con_count = 0;
    bank = 0;
    curr_opacity = 0;
    mask_opacity = 0;
    consume_position = [10, 0];
    
    // keep track of which components have finished
    practiceComponents = [];
    practiceComponents.push(target_p);
    practiceComponents.push(alternative_p);
    practiceComponents.push(control_p);
    practiceComponents.push(mouse_p);
    practiceComponents.push(mask_p);
    practiceComponents.push(consequence_p);
    practiceComponents.push(bank_amount_p);
    practiceComponents.push(bank_text_p);
    practiceComponents.push(consume_p);
    
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice'-------
    // get current time
    t = practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_p* updates
    if (t >= 0.5 && target_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_p.tStart = t;  // (not accounting for frame time here)
      target_p.frameNStart = frameN;  // exact frame index
      
      target_p.setAutoDraw(true);
    }

    
    if (target_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target_p.setOpacity(1, false);
      target_p.setPos([((- Math.cos((t * 0.5))) * 0.75), (Math.cos((t * 0.25)) * 0.4)], false);
    }
    
    // *alternative_p* updates
    if (t >= 0.5 && alternative_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      alternative_p.tStart = t;  // (not accounting for frame time here)
      alternative_p.frameNStart = frameN;  // exact frame index
      
      alternative_p.setAutoDraw(true);
    }

    
    if (alternative_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      alternative_p.setOpacity(1, false);
      alternative_p.setPos([(Math.cos((t * 0.5)) * 0.75), (Math.cos(((t * (- 0.25)) + 2.57)) * (- 0.4))], false);
    }
    
    // *control_p* updates
    if (t >= 0.5 && control_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      control_p.tStart = t;  // (not accounting for frame time here)
      control_p.frameNStart = frameN;  // exact frame index
      
      control_p.setAutoDraw(true);
    }

    
    if (control_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      control_p.setOpacity(1, false);
      control_p.setPos([(Math.cos(((t + 2.57) * 0.5)) * 0.75), (Math.cos((t * (- 0.25))) * (- 0.4))], false);
    }
    // *mouse_p* updates
    if (t >= 0.5 && mouse_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_p.tStart = t;  // (not accounting for frame time here)
      mouse_p.frameNStart = frameN;  // exact frame index
      
      mouse_p.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_p.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_p.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_p.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_p.getPos();
          mouse_p.x.push(_mouseXYs[0]);
          mouse_p.y.push(_mouseXYs[1]);
          mouse_p.leftButton.push(_mouseButtons[0]);
          mouse_p.midButton.push(_mouseButtons[1]);
          mouse_p.rightButton.push(_mouseButtons[2]);
          mouse_p.time.push(mouse_p.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [target, alternative, control]) {
            if (obj.contains(mouse_p)) {
              gotValidClick = true;
              mouse_p.clicked_name.push(obj.name)
              mouse_p.clicked_pos.push(obj.pos)
            }
          }
        }
      }
    }
    if (mouse.isPressedIn(target_p)) {
        consume_position = [0, 0];
        curr_opacity = 1;
        mask_opacity = 1;
        play_sound();
        tar_count += 1;
    }
    if (mouse.isPressedIn(alternative_p)) {
        consume_position = [0, 0];
        curr_opacity = 1;
        mask_opacity = 1;
        play_sound();
        alt_count += 1;
    }
    if (mouse.isPressedIn(consume_p)) {
        consume_position = [100, 0];
        curr_opacity = 0;
        mask_opacity = 0;
        bank += 1;
        con_count += 1;
    }
    if ((timer.getTime() <= 40)) {
        if ((tar_count > 8)) {
            if ((alt_count > 8)) {
                if ((con_count > 8)) {
                    continueRoutine = false;
                }
            }
        }
    }
    if ((timer.getTime() <= 0)) {
        continueRoutine = false;
    }
    
    
    // *mask_p* updates
    if (t >= 0.0 && mask_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_p.tStart = t;  // (not accounting for frame time here)
      mask_p.frameNStart = frameN;  // exact frame index
      
      mask_p.setAutoDraw(true);
    }

    
    if (mask_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mask_p.setOpacity(mask_opacity, false);
    }
    
    // *consequence_p* updates
    if (t >= 0.5 && consequence_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consequence_p.tStart = t;  // (not accounting for frame time here)
      consequence_p.frameNStart = frameN;  // exact frame index
      
      consequence_p.setAutoDraw(true);
    }

    
    if (consequence_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consequence_p.setOpacity(curr_opacity, false);
    }
    
    // *bank_amount_p* updates
    if (t >= 0.0 && bank_amount_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_amount_p.tStart = t;  // (not accounting for frame time here)
      bank_amount_p.frameNStart = frameN;  // exact frame index
      
      bank_amount_p.setAutoDraw(true);
    }

    
    if (bank_amount_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      bank_amount_p.setText(bank, false);
    }
    
    // *bank_text_p* updates
    if (t >= 0.0 && bank_text_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_text_p.tStart = t;  // (not accounting for frame time here)
      bank_text_p.frameNStart = frameN;  // exact frame index
      
      bank_text_p.setAutoDraw(true);
    }

    
    // *consume_p* updates
    if (t >= 0.0 && consume_p.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consume_p.tStart = t;  // (not accounting for frame time here)
      consume_p.frameNStart = frameN;  // exact frame index
      
      consume_p.setAutoDraw(true);
    }

    
    if (consume_p.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consume_p.setOpacity(mask_opacity, false);
      consume_p.setPos(consume_position, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice'-------
    for (const thisComponent of practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse_p.x', mouse_p.x);
    psychoJS.experiment.addData('mouse_p.y', mouse_p.y);
    psychoJS.experiment.addData('mouse_p.leftButton', mouse_p.leftButton);
    psychoJS.experiment.addData('mouse_p.midButton', mouse_p.midButton);
    psychoJS.experiment.addData('mouse_p.rightButton', mouse_p.rightButton);
    psychoJS.experiment.addData('mouse_p.time', mouse_p.time);
    psychoJS.experiment.addData('mouse_p.clicked_name', mouse_p.clicked_name);
    psychoJS.experiment.addData('mouse_p.clicked_pos', mouse_p.clicked_pos);
    
    // the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function begin_iciRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'begin_ici'-------
    t = 0;
    begin_iciClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    begin_ph1.keys = undefined;
    begin_ph1.rt = undefined;
    _begin_ph1_allKeys = [];
    // keep track of which components have finished
    begin_iciComponents = [];
    begin_iciComponents.push(begin_text);
    begin_iciComponents.push(click_ph1);
    begin_iciComponents.push(begin_ph1);
    
    for (const thisComponent of begin_iciComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function begin_iciRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'begin_ici'-------
    // get current time
    t = begin_iciClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *begin_text* updates
    if (t >= 0.5 && begin_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_text.tStart = t;  // (not accounting for frame time here)
      begin_text.frameNStart = frameN;  // exact frame index
      
      begin_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((begin_text.status === PsychoJS.Status.STARTED || begin_text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      begin_text.setAutoDraw(false);
    }
    
    // *click_ph1* updates
    if (t >= 6.0 && click_ph1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_ph1.tStart = t;  // (not accounting for frame time here)
      click_ph1.frameNStart = frameN;  // exact frame index
      
      click_ph1.setAutoDraw(true);
    }

    
    // *begin_ph1* updates
    if (t >= 6.0 && begin_ph1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_ph1.tStart = t;  // (not accounting for frame time here)
      begin_ph1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { begin_ph1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { begin_ph1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { begin_ph1.clearEvents(); });
    }

    if (begin_ph1.status === PsychoJS.Status.STARTED) {
      let theseKeys = begin_ph1.getKeys({keyList: ['space'], waitRelease: false});
      _begin_ph1_allKeys = _begin_ph1_allKeys.concat(theseKeys);
      if (_begin_ph1_allKeys.length > 0) {
        begin_ph1.keys = _begin_ph1_allKeys[_begin_ph1_allKeys.length - 1].name;  // just the last key pressed
        begin_ph1.rt = _begin_ph1_allKeys[_begin_ph1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of begin_iciComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function begin_iciRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'begin_ici'-------
    for (const thisComponent of begin_iciComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begin_ph1.keys', begin_ph1.keys);
    if (typeof begin_ph1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('begin_ph1.rt', begin_ph1.rt);
        routineTimer.reset();
        }
    
    begin_ph1.stop();
    // the Routine "begin_ici" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function phase_1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'phase_1'-------
    t = 0;
    phase_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    mouse.clicked_pos = [];
    gotValidClick = false; // until a click is received
    mouse.mouseClock.reset();
    import {Sound} from 'psychopy/sound';
    var all_count, alt_count, bank, con_count, consume_position, curr_opacity, duration, mask_opacity, tar_count, timer;
    function play_sound() {
        var beep;
        beep = new sound.Sound("A", {"secs": 0.3});
        beep.setVolume(1);
        beep.play();
        core.wait(0.3);
    }
    timer = new util.CountdownTimer(5);
    duration = new util.Clock();
    bank = 0;
    curr_opacity = 0;
    mask_opacity = 0;
    consume_position = [10, 0];
    //tar_count = 0;
    //alt_count = 0;
    //con_count = 0;
    //all_count = 0;
    //
    // keep track of which components have finished
    phase_1Components = [];
    phase_1Components.push(target);
    phase_1Components.push(alternative);
    phase_1Components.push(control);
    phase_1Components.push(mouse);
    phase_1Components.push(mask);
    phase_1Components.push(consequence);
    phase_1Components.push(bank_amount);
    phase_1Components.push(bank_text);
    phase_1Components.push(consume);
    
    for (const thisComponent of phase_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function phase_1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'phase_1'-------
    // get current time
    t = phase_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target* updates
    if (t >= 0.5 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }

    
    if (target.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target.setOpacity(1, false);
      target.setPos([((- Math.cos((t * 0.5))) * 0.75), (Math.cos((t * 0.25)) * 0.4)], false);
    }
    
    // *alternative* updates
    if (t >= 0.5 && alternative.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      alternative.tStart = t;  // (not accounting for frame time here)
      alternative.frameNStart = frameN;  // exact frame index
      
      alternative.setAutoDraw(true);
    }

    
    if (alternative.status === PsychoJS.Status.STARTED){ // only update if being drawn
      alternative.setOpacity(1, false);
      alternative.setPos([(Math.cos((t * 0.5)) * 0.75), (Math.cos(((t * (- 0.25)) + 2.57)) * (- 0.4))], false);
    }
    
    // *control* updates
    if (t >= 0.5 && control.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      control.tStart = t;  // (not accounting for frame time here)
      control.frameNStart = frameN;  // exact frame index
      
      control.setAutoDraw(true);
    }

    
    if (control.status === PsychoJS.Status.STARTED){ // only update if being drawn
      control.setOpacity(1, false);
      control.setPos([(Math.cos(((t + 2.57) * 0.5)) * 0.75), (Math.cos((t * (- 0.25))) * (- 0.4))], false);
    }
    // *mouse* updates
    if (t >= 0.5 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [target, alternative, control]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
              mouse.clicked_pos.push(obj.pos)
            }
          }
        }
      }
    }
    
    // *mask* updates
    if (t >= 0.0 && mask.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask.tStart = t;  // (not accounting for frame time here)
      mask.frameNStart = frameN;  // exact frame index
      
      mask.setAutoDraw(true);
    }

    
    if (mask.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mask.setOpacity(mask_opacity, false);
    }
    if (mouse.isPressedIn(target)) {
    //    tar_count += 1;
    //    all_count += 1;
        consume_position = [0, 0];
        curr_opacity = 1;
        mask_opacity = 1;
        play_sound();
    }
    //if (mouse.isPressedIn(alternative)) {
    //    alt_count += 1;
    //    all_count += 1;
    //}
    //if (mouse.isPressedIn(control)) {
    //    con_count += 1;
    //    all_count += 1;
    //}
    if (mouse.isPressedIn(consume)) {
        consume_position = [10, 0];
        curr_opacity = 0;
        mask_opacity = 0;
        bank += 1;
        ovr_bank += 1;
    }
    if ((timer.getTime() <= 0)) {
        continueRoutine = false;
    }
    
    
    // *consequence* updates
    if (t >= 0.5 && consequence.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consequence.tStart = t;  // (not accounting for frame time here)
      consequence.frameNStart = frameN;  // exact frame index
      
      consequence.setAutoDraw(true);
    }

    
    if (consequence.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consequence.setOpacity(curr_opacity, false);
    }
    
    // *bank_amount* updates
    if (t >= 0.0 && bank_amount.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_amount.tStart = t;  // (not accounting for frame time here)
      bank_amount.frameNStart = frameN;  // exact frame index
      
      bank_amount.setAutoDraw(true);
    }

    
    if (bank_amount.status === PsychoJS.Status.STARTED){ // only update if being drawn
      bank_amount.setText(bank, false);
    }
    
    // *bank_text* updates
    if (t >= 0.0 && bank_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_text.tStart = t;  // (not accounting for frame time here)
      bank_text.frameNStart = frameN;  // exact frame index
      
      bank_text.setAutoDraw(true);
    }

    
    // *consume* updates
    if (t >= 0.0 && consume.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consume.tStart = t;  // (not accounting for frame time here)
      consume.frameNStart = frameN;  // exact frame index
      
      consume.setAutoDraw(true);
    }

    
    if (consume.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consume.setOpacity(mask_opacity, false);
      consume.setPos(consume_position, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of phase_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function phase_1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'phase_1'-------
    for (const thisComponent of phase_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    psychoJS.experiment.addData('mouse.clicked_pos', mouse.clicked_pos);
    
    // the Routine "phase_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function ici_1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ici_1'-------
    t = 0;
    ici_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    begin_ph2.keys = undefined;
    begin_ph2.rt = undefined;
    _begin_ph2_allKeys = [];
    // keep track of which components have finished
    ici_1Components = [];
    ici_1Components.push(ici_1_text);
    ici_1Components.push(click_ph2);
    ici_1Components.push(begin_ph2);
    
    for (const thisComponent of ici_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ici_1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ici_1'-------
    // get current time
    t = ici_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ici_1_text* updates
    if (t >= 0.5 && ici_1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ici_1_text.tStart = t;  // (not accounting for frame time here)
      ici_1_text.frameNStart = frameN;  // exact frame index
      
      ici_1_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ici_1_text.status === PsychoJS.Status.STARTED || ici_1_text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ici_1_text.setAutoDraw(false);
    }
    
    // *click_ph2* updates
    if (t >= 6.0 && click_ph2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_ph2.tStart = t;  // (not accounting for frame time here)
      click_ph2.frameNStart = frameN;  // exact frame index
      
      click_ph2.setAutoDraw(true);
    }

    
    // *begin_ph2* updates
    if (t >= 6.0 && begin_ph2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_ph2.tStart = t;  // (not accounting for frame time here)
      begin_ph2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { begin_ph2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { begin_ph2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { begin_ph2.clearEvents(); });
    }

    if (begin_ph2.status === PsychoJS.Status.STARTED) {
      let theseKeys = begin_ph2.getKeys({keyList: ['space'], waitRelease: false});
      _begin_ph2_allKeys = _begin_ph2_allKeys.concat(theseKeys);
      if (_begin_ph2_allKeys.length > 0) {
        begin_ph2.keys = _begin_ph2_allKeys[_begin_ph2_allKeys.length - 1].name;  // just the last key pressed
        begin_ph2.rt = _begin_ph2_allKeys[_begin_ph2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ici_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ici_1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ici_1'-------
    for (const thisComponent of ici_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begin_ph2.keys', begin_ph2.keys);
    if (typeof begin_ph2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('begin_ph2.rt', begin_ph2.rt);
        routineTimer.reset();
        }
    
    begin_ph2.stop();
    // the Routine "ici_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function phase_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'phase_2'-------
    t = 0;
    phase_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    mouse_2.clicked_name = [];
    mouse_2.clicked_pos = [];
    gotValidClick = false; // until a click is received
    mouse_2.mouseClock.reset();
    import {Sound} from 'psychopy/sound';
    var all_count, alt_count, bank, con_count, consume_position, curr_opacity, mask_opacity, tar_count, timer;
    function play_sound() {
        var beep;
        beep = new sound.Sound("A", {"secs": 0.3});
        beep.setVolume(1);
        beep.play();
        core.wait(0.3);
    }
    timer = new util.CountdownTimer(5);
    bank = 0;
    curr_opacity = 0;
    mask_opacity = 0;
    consume_position = [10, 0];
    //tar_count = 0;
    //alt_count = 0;
    //con_count = 0;
    //all_count = 0;
    //
    // keep track of which components have finished
    phase_2Components = [];
    phase_2Components.push(target_2);
    phase_2Components.push(alternative_2);
    phase_2Components.push(control_2);
    phase_2Components.push(mouse_2);
    phase_2Components.push(mask_2);
    phase_2Components.push(consequence_2);
    phase_2Components.push(bank_amount_2);
    phase_2Components.push(bank_text_2);
    phase_2Components.push(consume_2);
    
    for (const thisComponent of phase_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function phase_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'phase_2'-------
    // get current time
    t = phase_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_2* updates
    if (t >= 0.5 && target_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_2.tStart = t;  // (not accounting for frame time here)
      target_2.frameNStart = frameN;  // exact frame index
      
      target_2.setAutoDraw(true);
    }

    
    if (target_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target_2.setOpacity(1, false);
      target_2.setPos([((- Math.cos((t * 0.5))) * 0.75), (Math.cos((t * 0.25)) * 0.4)], false);
    }
    
    // *alternative_2* updates
    if (t >= 0.5 && alternative_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      alternative_2.tStart = t;  // (not accounting for frame time here)
      alternative_2.frameNStart = frameN;  // exact frame index
      
      alternative_2.setAutoDraw(true);
    }

    
    if (alternative_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      alternative_2.setOpacity(1, false);
      alternative_2.setPos([(Math.cos((t * 0.5)) * 0.75), (Math.cos(((t * (- 0.25)) + 2.57)) * (- 0.4))], false);
    }
    
    // *control_2* updates
    if (t >= 0.5 && control_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      control_2.tStart = t;  // (not accounting for frame time here)
      control_2.frameNStart = frameN;  // exact frame index
      
      control_2.setAutoDraw(true);
    }

    
    if (control_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      control_2.setOpacity(1, false);
      control_2.setPos([(Math.cos(((t + 2.57) * 0.5)) * 0.75), (Math.cos((t * (- 0.25))) * (- 0.4))], false);
    }
    // *mouse_2* updates
    if (t >= 0.5 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_2.getPos();
          mouse_2.x.push(_mouseXYs[0]);
          mouse_2.y.push(_mouseXYs[1]);
          mouse_2.leftButton.push(_mouseButtons[0]);
          mouse_2.midButton.push(_mouseButtons[1]);
          mouse_2.rightButton.push(_mouseButtons[2]);
          mouse_2.time.push(mouse_2.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [target, alternative, control]) {
            if (obj.contains(mouse_2)) {
              gotValidClick = true;
              mouse_2.clicked_name.push(obj.name)
              mouse_2.clicked_pos.push(obj.pos)
            }
          }
        }
      }
    }
    
    // *mask_2* updates
    if (t >= 0.0 && mask_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mask_2.tStart = t;  // (not accounting for frame time here)
      mask_2.frameNStart = frameN;  // exact frame index
      
      mask_2.setAutoDraw(true);
    }

    
    if (mask_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      mask_2.setOpacity(mask_opacity, false);
    }
    //if (mouse.isPressedIn(target_2)) {
    //    tar_count += 1;
    //    all_count += 1;
    //}
    if (mouse.isPressedIn(alternative_2)) {
        consume_position = [0, 0];
        curr_opacity = 1;
        mask_opacity = 1;
    //    alt_count += 1;
    //    all_count += 1;
        play_sound();
    }
    //if (mouse.isPressedIn(control_2)) {
    //    con_count += 1;
    //    all_count += 1;
    //}
    if (mouse.isPressedIn(consume_2)) {
        consume_position = [10, 0];
        curr_opacity = 0;
        mask_opacity = 0;
        bank += 1;
        ovr_bank += 1;
    }
    if ((timer.getTime() <= 0)) {
        continueRoutine = false;
    }
    
    
    // *consequence_2* updates
    if (t >= 0.5 && consequence_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consequence_2.tStart = t;  // (not accounting for frame time here)
      consequence_2.frameNStart = frameN;  // exact frame index
      
      consequence_2.setAutoDraw(true);
    }

    
    if (consequence_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consequence_2.setOpacity(curr_opacity, false);
    }
    
    // *bank_amount_2* updates
    if (t >= 0.0 && bank_amount_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_amount_2.tStart = t;  // (not accounting for frame time here)
      bank_amount_2.frameNStart = frameN;  // exact frame index
      
      bank_amount_2.setAutoDraw(true);
    }

    
    if (bank_amount_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      bank_amount_2.setText(bank, false);
    }
    
    // *bank_text_2* updates
    if (t >= 0.0 && bank_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_text_2.tStart = t;  // (not accounting for frame time here)
      bank_text_2.frameNStart = frameN;  // exact frame index
      
      bank_text_2.setAutoDraw(true);
    }

    
    // *consume_2* updates
    if (t >= 0.0 && consume_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consume_2.tStart = t;  // (not accounting for frame time here)
      consume_2.frameNStart = frameN;  // exact frame index
      
      consume_2.setAutoDraw(true);
    }

    
    if (consume_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      consume_2.setOpacity(mask_opacity, false);
      consume_2.setPos(consume_position, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of phase_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function phase_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'phase_2'-------
    for (const thisComponent of phase_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse_2.x', mouse_2.x);
    psychoJS.experiment.addData('mouse_2.y', mouse_2.y);
    psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton);
    psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton);
    psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton);
    psychoJS.experiment.addData('mouse_2.time', mouse_2.time);
    psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name);
    psychoJS.experiment.addData('mouse_2.clicked_pos', mouse_2.clicked_pos);
    
    // the Routine "phase_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function ici_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ici_2'-------
    t = 0;
    ici_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    begin_ph3.keys = undefined;
    begin_ph3.rt = undefined;
    _begin_ph3_allKeys = [];
    // keep track of which components have finished
    ici_2Components = [];
    ici_2Components.push(ici_2_text);
    ici_2Components.push(click_ph3);
    ici_2Components.push(begin_ph3);
    
    for (const thisComponent of ici_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ici_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ici_2'-------
    // get current time
    t = ici_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ici_2_text* updates
    if (t >= 0.5 && ici_2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ici_2_text.tStart = t;  // (not accounting for frame time here)
      ici_2_text.frameNStart = frameN;  // exact frame index
      
      ici_2_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ici_2_text.status === PsychoJS.Status.STARTED || ici_2_text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ici_2_text.setAutoDraw(false);
    }
    
    // *click_ph3* updates
    if (t >= 6.0 && click_ph3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_ph3.tStart = t;  // (not accounting for frame time here)
      click_ph3.frameNStart = frameN;  // exact frame index
      
      click_ph3.setAutoDraw(true);
    }

    
    // *begin_ph3* updates
    if (t >= 6.0 && begin_ph3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_ph3.tStart = t;  // (not accounting for frame time here)
      begin_ph3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { begin_ph3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { begin_ph3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { begin_ph3.clearEvents(); });
    }

    if (begin_ph3.status === PsychoJS.Status.STARTED) {
      let theseKeys = begin_ph3.getKeys({keyList: ['space'], waitRelease: false});
      _begin_ph3_allKeys = _begin_ph3_allKeys.concat(theseKeys);
      if (_begin_ph3_allKeys.length > 0) {
        begin_ph3.keys = _begin_ph3_allKeys[_begin_ph3_allKeys.length - 1].name;  // just the last key pressed
        begin_ph3.rt = _begin_ph3_allKeys[_begin_ph3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ici_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ici_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ici_2'-------
    for (const thisComponent of ici_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begin_ph3.keys', begin_ph3.keys);
    if (typeof begin_ph3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('begin_ph3.rt', begin_ph3.rt);
        routineTimer.reset();
        }
    
    begin_ph3.stop();
    // the Routine "ici_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function phase_3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'phase_3'-------
    t = 0;
    phase_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    // current position of the mouse:
    mouse_3.x = [];
    mouse_3.y = [];
    mouse_3.leftButton = [];
    mouse_3.midButton = [];
    mouse_3.rightButton = [];
    mouse_3.time = [];
    mouse_3.clicked_name = [];
    mouse_3.clicked_pos = [];
    gotValidClick = false; // until a click is received
    mouse_3.mouseClock.reset();
    timer = new util.CountdownTimer(5);
    bank = 0;
    curr_opacity = 0;
    mask_opacity = 0;
    consume_position = [10, 0];
    //target_count = 0;
    //alt_count = 0;
    //control_count = 0;
    //
    // keep track of which components have finished
    phase_3Components = [];
    phase_3Components.push(target_3);
    phase_3Components.push(alternative_3);
    phase_3Components.push(control_3);
    phase_3Components.push(mouse_3);
    phase_3Components.push(bank_amount_3);
    phase_3Components.push(bank_text_3);
    
    for (const thisComponent of phase_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function phase_3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'phase_3'-------
    // get current time
    t = phase_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_3* updates
    if (t >= 0.5 && target_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_3.tStart = t;  // (not accounting for frame time here)
      target_3.frameNStart = frameN;  // exact frame index
      
      target_3.setAutoDraw(true);
    }

    
    if (target_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      target_3.setPos([((- Math.cos((t * 0.5))) * 0.75), (Math.cos((t * 0.25)) * 0.4)], false);
    }
    
    // *alternative_3* updates
    if (t >= 0.5 && alternative_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      alternative_3.tStart = t;  // (not accounting for frame time here)
      alternative_3.frameNStart = frameN;  // exact frame index
      
      alternative_3.setAutoDraw(true);
    }

    
    if (alternative_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      alternative_3.setPos([(Math.cos((t * 0.5)) * 0.75), (Math.cos(((t * (- 0.25)) + 2.57)) * (- 0.4))], false);
    }
    
    // *control_3* updates
    if (t >= 0.5 && control_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      control_3.tStart = t;  // (not accounting for frame time here)
      control_3.frameNStart = frameN;  // exact frame index
      
      control_3.setAutoDraw(true);
    }

    
    if (control_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      control_3.setPos([(Math.cos(((t + 2.57) * 0.5)) * 0.75), (Math.cos((t * (- 0.25))) * (- 0.4))], false);
    }
    // *mouse_3* updates
    if (t >= 0.5 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_3.getPos();
          mouse_3.x.push(_mouseXYs[0]);
          mouse_3.y.push(_mouseXYs[1]);
          mouse_3.leftButton.push(_mouseButtons[0]);
          mouse_3.midButton.push(_mouseButtons[1]);
          mouse_3.rightButton.push(_mouseButtons[2]);
          mouse_3.time.push(mouse_3.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [target, alternative, control]) {
            if (obj.contains(mouse_3)) {
              gotValidClick = true;
              mouse_3.clicked_name.push(obj.name)
              mouse_3.clicked_pos.push(obj.pos)
            }
          }
        }
      }
    }
    //if (mouse.isPressedIn(target_3)) {
    //    target_count += 1;
    //    control_count;
    //}
    //if (mouse.isPressedIn(alternative_3)) {
    //    alt_count += 1;
    //}
    //if (mouse.isPressedIn(control_3)) {
    //    control_count += 1;
    //}
    if ((timer.getTime() <= 0)) {
        continueRoutine = false;
    }
    
    
    // *bank_amount_3* updates
    if (t >= 0.0 && bank_amount_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_amount_3.tStart = t;  // (not accounting for frame time here)
      bank_amount_3.frameNStart = frameN;  // exact frame index
      
      bank_amount_3.setAutoDraw(true);
    }

    
    if (bank_amount_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      bank_amount_3.setText(bank, false);
    }
    
    // *bank_text_3* updates
    if (t >= 0.0 && bank_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bank_text_3.tStart = t;  // (not accounting for frame time here)
      bank_text_3.frameNStart = frameN;  // exact frame index
      
      bank_text_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of phase_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function phase_3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'phase_3'-------
    for (const thisComponent of phase_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse_3.x', mouse_3.x);
    psychoJS.experiment.addData('mouse_3.y', mouse_3.y);
    psychoJS.experiment.addData('mouse_3.leftButton', mouse_3.leftButton);
    psychoJS.experiment.addData('mouse_3.midButton', mouse_3.midButton);
    psychoJS.experiment.addData('mouse_3.rightButton', mouse_3.rightButton);
    psychoJS.experiment.addData('mouse_3.time', mouse_3.time);
    psychoJS.experiment.addData('mouse_3.clicked_name', mouse_3.clicked_name);
    psychoJS.experiment.addData('mouse_3.clicked_pos', mouse_3.clicked_pos);
    
    // the Routine "phase_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function end_textRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end_text'-------
    t = 0;
    end_textClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_textComponents = [];
    end_textComponents.push(end_text);
    end_textComponents.push(ovr_bank_amount);
    
    for (const thisComponent of end_textComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function end_textRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end_text'-------
    // get current time
    t = end_textClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.5 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((end_text.status === PsychoJS.Status.STARTED || end_text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      end_text.setAutoDraw(false);
    }
    
    // *ovr_bank_amount* updates
    if (t >= 0.5 && ovr_bank_amount.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ovr_bank_amount.tStart = t;  // (not accounting for frame time here)
      ovr_bank_amount.frameNStart = frameN;  // exact frame index
      
      ovr_bank_amount.setAutoDraw(true);
    }

    frameRemains = 0.5 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ovr_bank_amount.status === PsychoJS.Status.STARTED || ovr_bank_amount.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ovr_bank_amount.setAutoDraw(false);
    }
    
    if (ovr_bank_amount.status === PsychoJS.Status.STARTED){ // only update if being drawn
      ovr_bank_amount.setText(ovr_bank, false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_textComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function end_textRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end_text'-------
    for (const thisComponent of end_textComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
