# Luminator
It does stuff. It's awesome.

## Input/Control System

The input/control system takes input from the kinect, analyzes it, and sends it out to the other systems. It consists of the following sub-systems:

* Input (Kinect)
* Input Processing - takes input values and generates parameter values
* Output - takes parameter values and transmits them to external systems through various protocols, including MIDI, OSC, and TouchDesigner native DAT protocol

## Renderer System

* ...

## Modes

!!! NOTE: the modes system is going to be removed - see issue #29

The system as a whole is in one of several distinct modes at any given time. It switches modes based periodically or in response to input.

Each mode has:
* Parameter/event definitions, including names, default values, and optional midi mappings
* An input processor module which takes input values and generates the parameters/events defined by the mode
* A renderer module (running in the renderer process), that takes the parameter/events as defined by the mode and generates a video stream
* Output sent to OSC/MIDI/DAT channels based on the mode's parameter/event definitions (this isn't really its own mode-specific component, but it's worth mentioning anyway)
* Additionally, other things...?

## Variables
Variables are used to make values available to components within the various systems and components.
Variable values come from a combination of several sources, where each successive source can override values from the previous sources.

Variable Sources (sources are overriden by those below them):

Source | Description
-------|------------
global settings | globally shared system settings
local settings | settings local to each system (Input/Control and Renderer), but not specific to a particular mode
environment settings | settings based on the environment in which a system is running, for things like host names and MIDI ports
mode settings - basic | settings based on the current system mode, based on the mode list file, which is mostly just paths to other settings files
mode settings - additional | settings based on the current system mode, based on the settings file referenced by the basic mode settings

Common Variables:
* TODO: list commonly used variables

## Files/Directories
File/Directory | Description
---------------|------------
controller/ | files related to the Input/Control system
controller/local_settings.txt | settings overrides specific to the Input/Control system
renderer/ | files related to the Renderer system
renderer/local_settings.txt | settings overrides specific to the Renderer system
shared/ | (sub-module) the [tektshared](http://www.github.com/t3kt/tektshared) common components
derez/ | (sub-module) the [DeRez](http://www.github.com/t3kt/DeRez) components for communicating with DeRez (ColorKinetics) LED panels
scripts/ | python scripts, mostly imported into TouchDesigner modules for Script DATs/CHOPs/etc
modes/ | definitions and components related to specific system modes, or shared between several modes
core.tox | the shared system core component which processes settings files, generates common tables, definitions, variables, etc
modes.tox | the shared system component which processes system modes and generates settings, etc based on the current mode
modelist.txt | list of the system modes, specifying which settings files and components each mode uses
param_defs.txt | definitions for system (not mode-specific) parameters
environments.txt | definitions for various environments in which the system can run, including settings for host names and MIDI ports
global_settings.txt | globally shared settings, which can be overridden by local settings, mode settings, environment settings, etc
