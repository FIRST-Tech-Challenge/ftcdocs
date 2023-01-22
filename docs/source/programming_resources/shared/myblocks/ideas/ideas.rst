Ideas for Other myBlocks
========================

MyBlocks offer great potential for creativity and robot capability.
Start by programming myBlocks for tasks that an existing group of Blocks
can do. Later, add functions that are **not available** with regular
Blocks. Here are some examples of both:

-  Set one or more program variables during INIT, **using the gamepad**.
   This can be done with regular Blocks, but a good User Interface (UI)
   requires multiple long and complex Functions.

-  Create driving actions with **multiple sensor controls**. For
   example, gyro-based steering towards a distance goal (ultrasonic or
   vision target). Or Run_To_Position while following a line. A myBlock
   can provide Blocks users with controls previously considered too
   complex.

-  Provide access to **External Libraries**, new for SDK 7.0. More
   info is :ref:`here <programming_resources/shared/external_libraries_blocks/external-libraries-blocks:external 
   libraries in onbot java and blocks>`.

-  One of the above examples controls a servo specified by the Blocks
   user. This could lead to a **family of separate myBlocks** to
   interact with 1 device, 2 devices, etc. Or a generic single myBlock
   could interact with, say, up to 4 DC motors. The Java method would
   process only those DC motors with a filled-in parameter name.

-  Control the **LED flashlight** on the RC phone?

-  Could **telemetry.speak** have a myBlock equivalent of the Boolean
   ``AndroidTextToSpeech.isSpeaking()``?

Looking for ideas? The top-level API Documentation for the SDK is
`here <https://javadoc.io/doc/org.firstinspires.ftc>`__. Click
**RobotCore** to see many commonly used classes in the left-side menu,
and you can also check other sections.

   Do you have suggestions or a good example to share? Send to
   westsiderobotics@verizon.net.

Here are some tips for efficiency, from the developer Liz Looney:

-  Limit the number of method calls. Calling a single myBlock that does
   5 tasks uses less overhead than calling 5 myBlocks that each do one
   task.

-  Limit the number of parameters. If your myBlock needs certain
   information that won’t change during the OpMode, use an **initialize
   method** that’s called once at the start of the OpMode. The
   initialize method stores that information, to avoid repeatedly
   passing the same parameter each time the myBlock is called.
