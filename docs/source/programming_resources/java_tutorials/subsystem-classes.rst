Subsystem Classes
=================

Why Subsystem Classes?
----------------------

Until now, we have defined all of our hardware in each OpMode.
However, that approach, while okay if you have only a few OpModes,
makes editing hardware difficult to maintain.

Take the following two OpModes.
The first, an autonomous OpMode,
raises the linear slides to a specific position and then stops.
The second, a teleop OpMode,
raises the linear slides to the same position whenever the ``a`` button is pressed,
and lowers them back to ``0`` whenever the ``b`` button is pressed.

.. code-block:: java

   @Autonomous
   public class MyAutonomous extends LinearOpMode {
       @Override
       public void runOpMode() throws InterruptedException {
           DcMotorEx slidesMotor = hardwareMap.get(DcMotorEx.class, "slides");

           slidesMotor.setDirection(DcMotorSimple.Direction.FORWARD);
           slidesMotor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);

           waitForStart();

           slidesMotor.setTargetPosition(1000);
           slidesMotor.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
           slidesMotor.setPower(1);

           while (slidesMotor.isBusy()) {
               telemetry.addData("Slides Position", slidesMotor.getCurrentPosition());
               telemetry.update();
           }
       }
   }

   @TeleOp
   public class MyTeleop extends LinearOpMode {
       @Override
       public void runOpMode() throws InterruptedException {
           DcMotorEx slidesMotor = hardwareMap.get(DcMotorEx.class, "slides");

           slidesMotor.setDirection(DcMotorSimple.Direction.FORWARD);
           slidesMotor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);

           waitForStart();

           while (opModeIsActive()) {
               if (gamepad1.aWasPressed()) {
                   slidesMotor.setTargetPosition(1000);
                   slidesMotor.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
                   slidesMotor.setPower(1);
               } else if (gamepad1.bWasPressed()) {
                   slidesMotor.setTargetPosition(0);
                   slidesMotor.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
                   slidesMotor.setPower(1);
               }

               telemetry.addData("Slides Position", slidesMotor.getCurrentPosition());
               telemetry.update();
           }
       }
   }

Notice that both of these OpModes have a lot of similarities.
For example, the first three lines of each ``runOpMode`` method are the same,
and the logic to set the target position is also repeated.

Now lets say your team decides to change the motor driving the slides.
This will likely mean that your target position to get to the same height changes,
and so you'll need to edit it in the OpModes.
With only two OpModes, that isn't difficult,
but as we increase the number of OpModes in the project,
it becomes easier to miss a call to ``setTargetPosition``.

To mitigate that, we can create a new class to represent our linear slides.
This guide will not explain what a class is; the `Oracle docs <https://docs.oracle.com/javase/tutorial/java/concepts/index.html>`__ provide a good introduction to objects, classes, and other programming concepts that, while not specific to FTC, are still very useful.

What Is A Subsystem Class?
--------------------------

A subsystem class is simply a class that represents a specific subsystem of a robot,
such as linear slides, which is what we will make in this tutorial.

To start, create a new file called ``LinearSlides.java``.
If you are using OnBot Java, make sure to select **"Not an OpMode"**
when creating the file.

Our file should look like this so far (excluding ``package`` and ``import`` statements,
which will be omitted in this tutorial):


.. code-block:: java

   public class LinearSlides {
   }

Now we will want a field for our motor.
This should be of type ``DcMotorEx``.
Since the motor doesn't change after creation,
we can use the ``final`` keyword.

.. code-block:: java
   :emphasize-lines: 2

   public class LinearSlides {
       public final DcMotorEx motor;
   }

Now, we want to create our constructor.
Because we need to use the ``HardwareMap``to create a ``DcMotorEx`` object,
we will make it a parameter of the constructor:

.. code-block:: java

   public LinearSlides(HardwareMap hardwareMap) {
        motor = hardwareMap.get(DcMotorEx.class, "slides");
   }

We will also want to set the direction of the motor and reset it,
so that we don't need to repeat that code in each OpMode.

.. code-block:: java

   public LinearSlides(HardwareMap hardwareMap) {
        motor = hardwareMap.get(DcMotorEx.class, "slides");

        motor.setDirection(DcMotorEx.Direction.FORWARD);
        motor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);
   }

Now that we're done with the constructor,
we can create some methods to represent what our LinearSlides can do.

First, we can create a ``runToPosition`` method that takes in a single parameter,
the target position,
and sets the target position, mode, and power of the motor:

.. code-block:: java

   public void runToPosition(int targetPosition) {
        motor.setTargetPosition(targetPosition);
        motor.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
        motor.setPower(1);
   }

In our OpModes from earlier,
we repeated the call to ``setTargetPosition(1000)``.
We can create an additional method that goes to position ``1000``
instead of using a parameter:

.. code-block:: java

   public void runToHigh() {
        runToPosition(1000);
   }

Now we're done!

In total, our ``LinearSlides`` class should look like this:

.. code-block:: java

   public class LinearSlides {
       public final DcMotorEx motor;

       public LinearSlides(HardwareMap hardwareMap) {
           motor = hardwareMap.get(DcMotorEx.class, "slides");

           motor.setDirection(DcMotorEx.Direction.FORWARD);
           motor.setMode(DcMotorEx.RunMode.STOP_AND_RESET_ENCODER);
       }

       public void runToPosition(int targetPosition) {
           motor.setTargetPosition(targetPosition);
           motor.setMode(DcMotorEx.RunMode.RUN_TO_POSITION);
           motor.setPower(1);
       }

       public void runToHigh() {
           runToPosition(1000);
       }
   }

Now that we have a class for our linear slides,
we can use it in our OpModes!
Here are the OpModes from before,
but updated to use our new ``LinearSlides`` class:

.. code-block:: java

   @Autonomous
   public class MyAutonomous extends LinearOpMode {
       @Override
       public void runOpMode() {
           LinearSlides slides = new LinearSlides(hardwareMap);

           waitForStart();

           slides.runToHigh();

           while (slides.motor.isBusy()) {
               telemetry.addData("Slides Position", slides.motor.getCurrentPosition());
               telemetry.update();
           }
       }
   }

   @TeleOp
   public class MyTeleop extends LinearOpMode {
       @Override
       public void runOpMode() throws InterruptedException {
          LinearSlides slides = new LinearSlides(hardwareMap);

           waitForStart();

           while (opModeIsActive()) {
               if (gamepad1.aWasPressed()) {
                   slides.runToHigh();
               } else if (gamepad1.bWasPressed()) {
                   slides.runToPosition(0);
               }

               telemetry.addData("Slides Position", slides.motor.getCurrentPosition());
               telemetry.update();
           }
       }
   }

Notice how in both OpModes,
we can access the `DcMotorEx` object using `slides.motor`,
and call methods such as `slides.runToHigh()`.

Now, if something about the motor changes,
or we need to change the high position,
we only need to edit one class!