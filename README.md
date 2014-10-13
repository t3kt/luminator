# Luminator
It does stuff. It's awesome. It's also known as Kinetic Reflections.

## Input/Control System

The input/control system takes input from the kinect, analyzes it, and sends it out to the other systems.
See [Input and Control System Documentation](docs/Control.md)

## Renderer System(s)

* ...

## Variables
See [Variables Documentation](docs/Variables.md)

## Files/Directories
File/Directory | Description
---------------|------------
[components/](components/) | shared tox components and related files
[controller/](controller/) | files related to the Input/Control system
[controller/local_settings.txt](controller/local_settings.txt) | settings overrides specific to the Input/Control system
[renderer/](renderer/) | files related to the Renderer system
[renderer/local_settings.txt](renderer/local_settings.txt) | settings overrides specific to the Renderer system
shared/ | (sub-module) the [tektshared](http://www.github.com/t3kt/tektshared) common components
derez/ | (sub-module) the [DeRez](http://www.github.com/t3kt/DeRez) components for communicating with DeRez (ColorKinetics) LED panels
[scripts/](scripts/) | python scripts, mostly imported into TouchDesigner modules for Script DATs/CHOPs/etc
[core.tox](core.tox) | the shared system core component which processes settings files, generates common tables, definitions, variables, etc
[environments.txt](environments.txt) | definitions for various environments in which the system can run, including settings for host names and MIDI ports
[global_settings.txt](global_settings.txt) | globally shared settings, which can be overridden by local settings, mode settings, environment settings, etc
