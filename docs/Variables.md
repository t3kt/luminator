## Variables
Variables are used to make values available to components within the various systems and components.
Variable values come from a combination of several sources, where each successive source can override values from the previous sources.

Variables can specify values that are calculated from expressions (in __TScript__), and can be based on the value of other variables. In order to avoid cyclic dependencies, a variables that are defined using the calculated value of another variable may not work correctly. To insert references to the variables, rather than using the standard $somevar syntax, the following format is used:
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
The values of variables may be different in different .toe files, but they all still mean the same thing. The term "directory path" refers to a filesystem path, relative to the current .toe file. The term "path" refers to an operator path within the current TouchDesigner project.

Variable | Description
---------|------------
environment | the name of the current environment (which is used to determine values of other variables)
ctrlhost | the hostname of the machine running the controller system
ctrlport | the port that the controller system is broadcasting on
ctrlprotocol | the protocol that the controller is using to broadcast settings
cells | the path to the grid cells definition table DAT
paramdefs | that path to the parameter definition table DAT
paramdefaults | the path to a CHOP that contains default values for all parameters
paramvals | the path to a CHOP that contains the current values for all parameters
rootdir | directory path of the root of the repository
shareddir | directory path of the [tektshared](http://www.github.com/t3kt/tektshared) common components
derezdir | directory path of the [DeRez](http://www.github.com/t3kt/DeRez) components
datadir | directory path for shared data (such as input recordings)
contentdir | directory path for externally hosted content
scriptsdir | directory path for shared Python scripts, generally intended to be used for Script CHOPs/DATs/etc
componentsdir | directory path for shared tox components
renderw<br/>renderh | width/height of the main renderer output (are these actually needed outside of the renderer?)
kinectplayers | TScript pattern for the Kinect player names that the control system pays attention to
kinectstatuses | TScript patterns for the "status" (non-coordinate) channels that are used from the Kinect
kinectpoints | TScript patterns for the "point" (coordinate) channels that are used from the Kinect
kinectscaledxmin<br/>kinectscaledxmax<br/>kinectscaledymin<br/>kinectscaledymax<br/>kinectscaledzmin<br/>kinectscaledzmax | Minimum/maximum X/Y/Z values of the range that coordinates are scaled to (see Coordinates section below)

### Controller Variables

These variables are only available within the controller .toe file.

Variable | Description
---------|------------
inputvals | path to the CHOP containing all the raw input values from the Kinect, with point coordinates in the __world space__ (see below)
depthstream | (unused - remove this for now...)
inputpoints | path to the CHOP containing all the input point coordinate values from the Kinect, scaled to the __normalized space__
inputdeltas | path to the CHOP containing distance moved since the previous frame for all points from the Kinect (currently unused), scaled to the __normalized space__
playerstatuses | path to the CHOP containing the active/inactive status for each player
activeplayers | path to a DAT containing a list of the names of only the currently active players
players | path to ... something?? TODO: update this
kinectrecordings | path to a DAT listing available Kinect input recordings
properties | path to a DAT containing current system property values (set from the control panel UI)

## Coordinates

Point coordinates are used in several places in the system. The meaning of these values depends on which coordinate space they were scaled to.

The raw values from the Kinect are first passed through a tranform, which can be used to correct for the positioning and angle of the Kinect. These corrected values are considered to be in __world space__, which means that they use whatever units the Kinect outputs natively, which correspond to some sort of physical unit of measure.

The __world space__ coordinates are then scaled to normalized ranges, such as -1 to 1 for X and Z, and 0 to 1 for Y (based on system/environment settings). These values are considered to be in the __normalized space__.

Within the control processing for each grid cell, the __normalized space__ values are scaled relative to the bounds of the cell. So, if a user is standing in a cell, and their hand is all the way to the left side of that cell, its X coordinate would be 1 and the right side would be -1. These values are considered to be in the __cell local space__. The per-cell values that the control system sends out to the other systems are in the __cell local space__.
