# Luminator
It does stuff. It's awesome. It's also known as Kinetic Reflections.

## Input/Control System

The input/control system takes input from the kinect, analyzes it, and sends it out to the other systems. It consists of the following sub-systems:

* Input (Kinect)
* Input Processing - takes input values and generates parameter values
* Output - takes parameter values and transmits them to external systems through various protocols, including MIDI, OSC, and TouchDesigner native DAT protocol

## Renderer System(s)

* ...

## Variables
Variables are used to make values available to components within the various systems and components.
Variable values come from a combination of several sources, where each successive source can override values from the previous sources.
Variables can specify values that are calculated based on the value of other variables. In order to avoid cyclic dependencies, a variables that are defined using the calculated value of another variable may not work correctly. To insert references to the variables, rather than using the standard $somevar syntax, the following format is used:
```
somevar {anothervar} + 5
```

Variable | Defined value in settings file | Effective value
------|-----|-----
stuffwidth | 100 | 100
numpartsx | 4 | 4
partwidth | {stuffwidth} / {numpartsx} | 25
stuffroot | /things/stuff | /things/stuff
partpath | {stuffroot}/part | /things/stuff/part

### Variable Sources
Sources are overriden by those listed below them.

Source | Description
-------|------------
global settings | globally shared system settings
local settings | settings local to each system (Input/Control and Renderer), but not specific to a particular mode
environment settings | settings based on the environment in which a system is running, for things like host names and MIDI ports

### Common Variables
All directory paths are relative to the current .toe file. The values of variables may be different in different .toe files, but they all still mean the same thing.

Variable | Description | Available In
---------|-------------|-------------
environment | the name of the current environment (which is used to determine values of other variables) | All systems
ctrlhost | the hostname of the machine running the controller system | All systems
ctrlport | the port that the controller system is broadcasting on | All systems
ctrlprotocol | the protocol that the controller is using to broadcast settings | All systems
cells | the path to the grid cells definition table DAT | All systems
paramdefs | that path to the parameter definition table DAT | All systems
paramdefaults | the path to a CHOP that contains default values for all parameters | All systems
paramvals | the path to a CHOP that contains the current values for all parameters | All systems
rootdir | directory path of the root of the repository | All systems
shareddir | directory path of the [tektshared](http://www.github.com/t3kt/tektshared) common components | All systems
derezdir | directory path of the [DeRez](http://www.github.com/t3kt/DeRez) components | All systems
datadir | directory path of the directory used for storing shared data (such as input recordings) | All systems



* TODO: document more variables

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
core.tox | the shared system core component which processes settings files, generates common tables, definitions, variables, etc
environments.txt | definitions for various environments in which the system can run, including settings for host names and MIDI ports
global_settings.txt | globally shared settings, which can be overridden by local settings, mode settings, environment settings, etc
