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

### Variable Sources
(sources are overriden by those below them)

Source | Description
-------|------------
global settings | globally shared system settings
local settings | settings local to each system (Input/Control and Renderer), but not specific to a particular mode
environment settings | settings based on the environment in which a system is running, for things like host names and MIDI ports

### Common Variables

Variable | Description | Available In
---------|-------------|-------------
environment | the name of the current environment (which is used to determine values of other variables) | All systems
ctrlhost | the hostname of the machine running the controller system | All systems
ctrlport | the port that the controller system is broadcasting on | All systems
ctrlprotocol | the protocol that the controller is using to broadcast settings | All systems

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
