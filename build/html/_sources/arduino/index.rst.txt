==============================================
Self-balancing robots with the pieces of a CNC
==============================================

3D printing machines are already ubiquitious. We will see how to resuse the parts of your CNC to make a self-balancing robot.


PARTS
=====
The parts that I have gathered are the following:

- 1 Arduino
- 1 driver shield for Arduino
- 2 Stepper motors Nema 15.

Additionally you will need:

- 2 Wheels 
- Gyro/.
 

CODE
====
The code is extracted from the Brobots evo that uses similar hardware.
In order to make use of the code with an Arduino UNO some registers have to be changed.

Timer/Counter
-----------
The TC0/1 in the Leonardo are more powerful than the Arduino UNO however we can adapt the values for the interruptions to....


