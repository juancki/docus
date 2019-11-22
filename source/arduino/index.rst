==============================================
Self-balancing robots with the pieces of a CNC
==============================================

3D printing machines are already ubiquitious. We will see how to resuse the motor parts of your CNC to make a self-balancing robot.

PARTS
=====
The parts that I have gathered from a old 3D machine are the following:

- 1 Arduino
- 1 CNC driver shield for Arduino
- 2 Stepper motors Nema 15

Additionally you will need:

- 2 Wheels 
- LiPo battery.
- Gyro


CONTROL
=======
Each stepper motor is controlled with the frequency of impulses (square signals) that are sent to the motor driver.
The way to calculate exactly which frequency is necessary to self-balance is done with discrete control techniques. 

The `control design`_ of the self balancing robot is similar to the inverted pendulum plus velocity control. The control is linear with two PID controllers in cascade.

The speed of the device is controlled with a PI controller which adjust the desired tilt angle :math:`\hat \theta` in function of the desired speed :math:`\hat v` and the robot speed :math:`v_r`.

The second controller is a PD control for stability which output is integrated. The inputs are  :math:`\hat \theta` and the actual titl angle :math:`\theta`
 
The steering is done throught standard differential steering.

Hardware
========
This project is based on the B-robot from JJrobots that uses similar hardware. 
Then, it makes sense to highlight the differences and similitudes:

- We will use Arduino UNO and they use Arduino Leonardo.
        - Which have different MCU ATmega328P and ATmega32u4 respectively.
- Even though we could print all the parts, to make it more different we will not use gears. The wheels will be directly attached to the motor shaft.
- Instead of using the jjRobots `Brain Shield` we are going to use an standard 3D printing control board.
- The stepper motor controller that we will use are the same.
- Same IMU (gyro+accelerometers).
- I have a 12V LiPo battery from a DIY plane and I will be using that but you can use the 6x AA batteries.


Software
========
The code I used is hosted in github_.

The ATMega328P(UNO) and ATMega32U4(Leonardo) are both in the AVR family and have 32K of flash memory. They differ in package and what peripherals are offered. From our point of view the **biggest difference between those two microcontrollers is the internal Timer/Counters (TC)** that are used for send the corresponding impulses to the stepper motor controllers. If you want to use the chip for a USB keyboard, the ATMega32U4, or any of the other USB equipped devices in the AVR family is a better choice.

- (UNO) Two 8-bit TCs with Separate Prescaler and Compare Mode. One 16-bit TC with Separate Prescaler, Compare Mode.
- (Leonardo) One 8-bit TC with Separate Prescaler and Compare Mode. Two 16-bit TCs with Separate Prescaler, Compare. And an extra 10-bit High-Speed TC.

Timer/Counter
.............
The TC0/1 in the Leonardo are more powerful than the Arduino UNO however we can adapt the values for the interruptions to....

+---------------+--------------------+--------------------+
| Motor M1      | ATMega328P         | ATMega32U4         |
+===============+====================+====================+
| Board         | Arduino UNO        | Arduino Leonardo   |
+               +                    +                    +
| Timer/Counter | TC1                | TC1                |
+               +                    +                    +
| Mode          | Interrupt on Match | Interrupt on Match |
+               +                    +                    +
| #bits         | 16                 | 16                 |
+               +                    +                    +
| pre scalers   | 1,8,64,256,1024    | 1,8,64,256,1024    |
+               +                    +                    +
| Ouput PORT    | PORTD, PD3         | PORTD, PD6         |
+               +                    +                    +
| Ouput PIN     | PIN 3              | PIN                |
+               +                    +                    +
| Max Fq (Hz)   | 0                  | 0                  |
+               +                    +                    +
| Min Fq (Hz)   | 0                  | 0                  |
+               +                    +                    +
| Docs Page     | 89                 | 99                 |
+---------------+--------------------+--------------------+

+---------------+--------------------+--------------------+
| Motor M2      | ATMega328P         | ATMega32U4         |
+===============+====================+====================+
| Board         | Arduino UNO        | Arduino Leonardo   |
+               +                    +                    +
| Timer/Counter | TC0                | TC3                |
+               +                    +                    +
| Mode          | Interrupt on Match | Interrupt on Match |
+               +                    +                    +
| #bits         | **8**              | 16                 |
+               +                    +                    +
| pre scalers   | 1,8,64,256,1024    | 1,8,64,256,1024    |
+               +                    +                    +
| Ouput PORT    | PORTD, PD3         | PORTD, PD6         |
+               +                    +                    +
| Ouput PIN     | PIN 3              | PIN                |
+               +                    +                    +
| Max Fq (Hz)   | 0                  | 0                  |
+               +                    +                    +
| Min Fq (Hz)   | 0                  | 0                  |
+---------------+--------------------+--------------------+
| Docs Page     | 74                 | 99                 |
+---------------+--------------------+--------------------+

Frequency function.
.. :math:
        f_{16bits} = \frac{f_{clk}}{2N(1+OCRnA}

Where N is the prescaler and OCRnA is the value at which the internal counter will trigger the interruption. OCRnA has the same number of bits as the TC. So, the TC0 used in M2 has half the bits than the others.


Previous implementation
-----------------------
The two 16-bit TCs are 
In order to make use of the code with an Arduino UNO some registers have to be changed.

My implementation
-----------------
I removed the Communication/Network files as I did not have the pieces to use them. I set the references velocity to 0.


.. _jjrobots: https://www.jjrobots.com/much-more-than-a-self-balancing-robot/
.. _`control design`: https://www.jjrobots.com/projects-2/b-robot/
.. _github: https://github.com/juancki/MySelfBalancing
