# Luminator
It does stuff. It's awesome.

## Input/Control System

The input/control system takes the inputs that 

* Input (Kinect)
* Input Processing - takes input values and generates parameter values and events
* State - takes input/parameter values and events and generates state values, including the current system mode
* Output - takes parameter values, events, and state values and transmits them through various protocols to external systems, including MIDI, OSC, and TouchDesigner native DAT protocol

## Renderer System

* ...

## Modes

The system as a whole is in one of several distinct modes at any given time. It switches modes based periodically or in response to input.

Each mode has:
* Parameter/event definitions, including names, default values, and optional midi mappings
* An input processor module which takes input values and generates the parameters/events defined by the mode
* A renderer module (running in the renderer process), that takes the parameter/events as defined by the mode and generates a video stream
* Output sent to OSC/MIDI/DAT channels based on the mode's parameter/event definitions (this isn't really its own mode-specific component, but it's worth mentioning anyway)
* Additionally, other things...?
