Glossary
=================

.. glossary::
    :sorted:

    OpMode
        An Operational Mode (OpMode) is the heart of any *FIRST* Tech Challenge routine. This refers to a User Defined Class that outlines the behavior of the robot during a certain period of the game. 
        Users are able to utilize all manners of functionality from sensors to motors and servors to dictate the behavior of the robot.
        For example, there might be an OpMode that causes the robot to drive forward for 5 seconds and then stop.
    
    Class
        A Class is a blueprint for an object. It tells the program what variables and functions an object will have. 
        For example, a class might be called "Robot" and have variables such as "motorLeft" and "motorRight" and functions such as "driveForward" and "driveBackward".

    Object
        An Object is an instance of a class. It is a variable that is defined by a class. 
        For example, an object might be called "robot" and be defined by the class "Robot". 
        This object would have variables such as "motorLeft" and "motorRight" and functions such as "driveForward" and "driveBackward".
    
    Variable
        A Variable is a value that is held in memory by the robot. It has a type, value, and name. 
        The type refers to what kind of value the variable holds (integer, string, etc.). 
        The value is the actual value of the variable (1, "Hello World", etc.).
        The name is what the variable is called in the program (motorLeft, motorRight, etc.).

    Integer
        An Integer is a type of variable that holds a number with no decimal places. (Eg. -3, 0, 1, 2, 3, etc.)
    
    String
        A string is a type of variable that holds a sequence of characters. (Eg. "Hello World!", "Robot", "2023", etc.)

    CAD
        CAD stands for Computer Aided Design. It is a type of software that allows users to create 3D models of objects. 
        In the context of robotics, CAD is ofteb used to create 3D models of robots and robot parts. 
        This allows users to visualize their robot before they build it while making sure that everything fits together.

    AprilTag :bdg-primary:`GM1`
        A visual fiducial system, useful for a wide variety of tasks including augmented reality, robotics, and
        scamera calibration. Information about AprilTags may be found :doc:`here </apriltag/vision_portal/apriltag_intro/apriltag-intro>`.

    Logic Level Converter :bdg-primary:`GM1`
        An electronic device that allows an encoder or sensor, that operates using 5V logic
        levels, to work with the REV Expansion Hub and/or REV Control Hub, which operates using 3.3V logic levels.
        This device may contain a step-up voltage converter (from 3.3V to 5V) and a dual channel, bidirectional logic
        level converter. This device may be used directly with a 5V digital sensor or with an I2C Sensor Adaptor Cable
        to a 5V I2C sensor.
    
    I2C Sensor Adapter Cable :bdg-primary:`GM1`
        An adapter to change the pin orientation of the REV Robotics Logic Level
        Converter to match a Modern Robotics compatible I2C sensor.

    Mini USB to OTG (On-The-Go) Micro Cable :bdg-primary:`GM1`
        The connection between the Smartphone Android Device
        Robot Controller and the REV Expansion Hub.

    Op Mode :bdg-primary:`GM1`
        An Op Mode (short for "operational mode") is software that is used to customize the behavior of a
        Competition Robot. The Robot Controller executes a selected Op Mode to perform certain tasks during a
        Match.

    OTG Micro Adapter :bdg-primary:`GM1`
         Connects a USB hub to Micro USB OTG (On-The-Go) port on a smartphone Driver
        Station Android Device. 

    REV Control Hub :bdg-primary:`GM1`
        An integrated Android Device with four (4) DC motor channels, six (6) servo channels,
        eight (8) digital I/O channels, four (4) analog input channels, and four (4) independent I2C buses. 

    REV Driver Hub :bdg-primary:`GM1`
        A compact mobile Android Device designed specifically for use as part of the Driver Station.

    REV Expansion Hub :bdg-primary:`GM1`
        An integrated electronic device with four (4) DC motor channels, six (6) servo
        channels, eight (8) digital I/O channels, four (4) analog input channels, and four (4) independent I2C buses. 

    REV SPARKmini Motor Controller :bdg-primary:`GM1`
        An electronic device that accepts a PWM control signal (from a servo
        controller) and supplies 12V power to a DC motor.

    REV Servo Power Module :bdg-primary:`GM1`
        An electronic device that boosts the power supplied to 3-wire servos. A REV
        Servo Power Module has 6 input servo ports and 6 matching output ports. It draws power from a 12V source 
        and provides 6V power to each output servo port. A REV Servo Power Module can provide up to 15A of
        current across all output servo ports for a total of 90 Watts of power per module.

    Robot Controller :bdg-primary:`GM1`
        A REV Control Hub or an allowed smartphone Android Device connected to a REV
        Expansion Hub located on the Robot that processes Team written software, reads on-board sensors, and
        receives commands from the Drive Team by way of the Driver Station. The Robot Controller sends instructions
        to the motor and servo controllers to make the Robot move.

    VEX Motor Controller 29 :bdg-primary:`GM1`
        An electronic device that accepts a PWM control signal from a servo controller
        through a REV Servo Power Module to drive a VEX EDR 393 motor

    Vision Camera :bdg-primary:`GM1`
        COTS devices with exactly one image sensor able to stream captured images and/or video.
        Vision cameras must be UVC compatible and must connect directly to a REV Control Hub via USB or to the
        Robot Controller through a powered USB hub. Common Vision Cameras are the Logitech C270 HD, Logitech
        C920 HD PRO, and Microsoft Lifecam HD-3000.

    Vision Sensor :bdg-primary:`GM1`
        COTS devices with exactly one image sensor not able to stream captured images and/or
        video. Instead, the images and/or video is processed by on-board algorithms and only the results are
        communicated back to a computer or system. Vision Sensors must follow all sensor rules in <RE11>. Common
        Vision Sensors are the HuskyLens and Pixy2, though only the HuskyLens has included SDK support as of
        SDK 9.0.