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

## Control processing

## Output

