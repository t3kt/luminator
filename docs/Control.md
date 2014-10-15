# Input and Control System

The input/control system takes input from the kinect, analyzes it, and sends it out to the other systems. It consists of the following subsystems:

* Input (Kinect)
* Input Preprocessing
* Control Processing - takes input values and generates parameter values
* Output - takes parameter values and transmits them to external systems through various protocols, including MIDI, OSC, and TouchDesigner native DAT protocol

## Input (Kinect)
The input subsystem reads data from the Kinect (v2) using a [KinectCHOP](http://www.derivative.ca/wiki088/index.php?title=Kinect_CHOP).

## Input Preprocessing
The input preprocessing subsystem takes the raw values coming from the Kinect and prepares them for analysis by the Control Processing subsystem.

It removes extraneous data channels. The input from the Kinect is _very_ verbose. Since the control processor only uses a subset of that data, the preprocessor excludes the unused channels.

* Supported points: head, spine, hand\_l, hand\_r, ankle\_l, ankle\_r
* Each point has :tx, :ty, :tz, \_tracked

It then generates several CHOPs/DATs. The path to each of those CHOPs/DATs is available as a globally available variable (see also [Variables Documentation](Variables.md)). These variables can be used as the target of Select CHOPs/DATs, in expressions, etc.

Path Variable | Description | Type
--------------|-------------|------
$inputstatuses | Statuses primarily indicate whether each point is being tracked, and how confident the Kinect is about the position. Statuses are treated as integer values, which only cook when the incoming data is actually changing. | CHOP
$inputpoints | Points update on every frame, even if the values aren't changing. The cost of checking for modifications outweighs the cost of having OPs further downstream cook more frequently. | CHOP
$playerstatuses | Determines whether each player is active, based on whether the Kinect is confidently tracking their spine. | CHOP
$inputdeltas | Movement deltas for each point (currently unused) | CHOP
$scaledinputpoints | A version of the points that are scaled to $kinectxmin/xmax/etc | CHOP
$activeplayers | A list of the IDs of all the players that are currently active (unused... probably) | DAT

## Control Processing (Cells)
The control processing subsystem takes the values from the preprocessor and uses them to generate a set of control parameters. Parameters are grouped together into "cells". A cell is a zone in the Kinect input area, which allows users to control a specifc set of parameters. Each cell generates distinct parameters. Cell definitions do not include Y coordinates. They map to areas of the ground in front of the Kinect.

### Cell Definitions
Cells are defined in [cells.txt](../cells.txt), with a fixed set of base properties. The Setup Tool can be used to adjust these settings, but other than that, they don't change when the system is running. The cell definitions are available in a DAT, identified by the $cells variable.
Each cell has:

Property | Description
---------|------------
center[xz] | the "rest" location (X, Z) of the center of the cell, when the cell is inactive
size[xz] | the range of (X, Z) coordinate values that the cell spans

### Cell Runtime State
While running, the control system updates cell states based on input (see Cell Behavior). These updated values are available in a DAT, identified by the $cellstates variable.
Each cell has:

Property | Description
---------|------------
rest\_center[xz] | the "rest" location, which is just a copy of the center[xz] from the cell definition
size[xz] | the size of the cell, copied from the cell definition
rest\_[xz]min, rest\_[xz]max | low/high bounds of the X and Z coordinates for the cell, when it is resting, based on rest\_center[xz] and size[xz]
active | 0 or 1 - indicates whether the cell is being actively used by a player (see behavior section)
center[xz] | the current center position of the cell
[xz]min [xz]max | the current bounds of the cell
player | the id (p1, p2, etc) of the player currently using the cell


### Cell Behavior
Each cell does stuff!


## Output

