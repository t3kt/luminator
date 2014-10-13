# Input and Control System

The input/control system takes input from the kinect, analyzes it, and sends it out to the other systems. It consists of the following subsystems:

* Input (Kinect)
* Input Preprocessing
* Control Processing - takes input values and generates parameter values
* Output - takes parameter values and transmits them to external systems through various protocols, including MIDI, OSC, and TouchDesigner native DAT protocol

## Input (Kinect)
The input subsystem reads data from the Kinect (v2) using a [KinectCHOP](http://www.derivative.ca/wiki088/index.php?title=Kinect_CHOP).

## Input Preprocessing
The input preprocessing subsystem takes the raw values coming from the Kinect and prepares them for analysis by the Control Processing subsystem. It performs several operations:

* Removing extraneous data channels - the input from the Kinect is _very_ verbose. Since the control processor only uses a subset of that data, the preprocessor excludes the unused channels.
* Separating channels into categories:
  * Statuses primarily indicate whether each point is being tracked, and how confident the Kinect is about the position. Statuses are treated as integer values, which only cook when the incoming data is actually changing.
  * Points update on every frame, even if the values aren't changing. The cost of checking for modifications outweighs the cost of having OPs further downstream cook more frequently.
* 

## Control processing

## Output

