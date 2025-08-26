# VexBrainSimulator
This is a program created to help students in the Vex Robotics program. It is a python package that can simulate the vex brain, controller, motors, pneumatics, and even bumpers! It runs off of pygame, and by editing three lines (usually) of your code, you can download it right onto your robot!

The usage for this program is pretty complex and simple at the same time. There are just a couple of steps you need to go through to have your code ready to be simulated

1: Download pygame in the command terminal using "python3 -m pip install -U pygame --user" or "py -m pip install -U pygame --user". Further troubleshooting on the pygame website is sometimes necessary; this stuff can be troublesome.
THEN in the code you have written:
2: change the line "from vex import *" to be "from vexbrainsim02 import *" (or the numbers can be changed to use a different version.
3: change any lines that have a function that runs a while loop to be a thread (ex: main() turns into RunMain = Thread(main))
4: add the line at the VERY END of all of your code that says "initiateVexSimulator()"

Woohoo hopefully it's working! Now lets go through some of the features:
There is controller support! The Logitech Gamepad F310 is supported, and from what I've seen, it's a very common controller. Other controllers could be connected, but they might produce errors, or unexpected results. Keep in mind the vex controller's A and B buttons, and X and Y buttons are switched.
If you're not using a controller, you can use your keyboard. Left stick = RDFG. Right stick = IJKL. You can remember by keeping the H key in the middle. For the letter buttons, press the corresponding letter keys, and for the arrow keys, press the corresponding arrows. R1 and L1 are ; and ' . R2 and L2 are [ and ].
You can trigger driver control or autonomous by using the "back" and "start" buttons on the logitech controller, or by pressing < and > on the keyboard.
AS OF VERSON 02:
The competition class is supported, and works perfectly.
Motors and motor groups are supported, but as of this version, they are very glitchy. There's random commands that don't exist, that I haven't cleaned up from testing, and only some of the stored motor information comes out correctly.
Pneumatics are supported, and they work perfectly.
Potentiometers can be defined, but always return 0.
Bumpers are supported, and they work perfectly. They also have a special feature that allows them to be triggered by the user. You can add a second parameter as a number, and that bumper will be hooked up to that number key.

Now make sure to watch out, there are some confusing errors, where the simulator works just fine, but when converting it to the robot, it doesn't. Here are the ones I've encountered:
F-strings are not supported in vex. Instead try using the .format() method. (ex: f'The time is {time}.' would be 'The time is {}.'.format(time))
Ordered Dictionaries are not supported in vex. Instead try using a list with two parameters. (ex: info = {'number': 100,} would be info = [('number', 100),])
Controller communicated is delayed. It can only send a command once every 50 milliseconds. If you're printing to the screen in a loop, and then try to rumble the controller somewhere else, it will only have a small chance of getting through.

I hope this project helps!
