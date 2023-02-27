Changing PIDF Coefficients
===========================

The REV Robotics Expansion Hub allows a user to change the PIDF
coefficients used for closed loop motor control. The PIDF coefficients
are specific to each channel (motor port) and to each RunMode.

The following sample OpMode uses an extended or enhanced DcMotor class
(called “DcMotorEx”) to change the PIDF coefficients for the
RUN_USING_ENCODER RunMode for a motor named “left_drive”. The OpMode
uses the setPIDFCoefficients method of the DcMotorEx class to change the
values. This method is not available with the standard DcMotor class.

Note that changes made to the PIDF coefficients do not persist if you
power cycle the REV Robotics Expansion Hub. If you need your changes to
persist, consider modifying your OpMode to store state information on
the Android phone. The Android Developer website has a tutorial on how
to save data from your app onto an Android device 
`here <https://developer.android.com/training/data-storage>`__

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDFCoefficients;

   /**
    * Created by Tom on 9/26/17.  Updated 9/24/2021 for PIDF.
    * This assumes that you are using a REV Robotics Expansion Hub
    * as your DC motor controller.  This OpMode uses the extended/enhanced
    * PIDF-related functions of the DcMotorEx class.  The REV Robotics Expansion Hub
    * supports the extended motor functions, but other controllers (such as the 
    * deprecated Modern Robotics and Hitechnic DC Motor Controllers) do not.
    */

   @Autonomous(name="Concept: Change PIDF", group = "Concept")
   public class ConceptChangePIDF extends LinearOpMode {

       // our DC motor
       DcMotorEx motorExLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;
       public static final double NEW_F = 0.5;
       // These values are for illustration only; they must be set 
       // and adjusted for each motor based on its planned usage.

       public void runOpMode() {
           // Get reference to DC motor.
           // Since we are using the Expansion Hub,
           // cast this motor to a DcMotorEx object.
           motorExLeft = (DcMotorEx)hardwareMap.get(DcMotor.class, "left_drive");

           // wait for start command
           waitForStart();

           // Get the PIDF coefficients for the RUN_USING_ENCODER RunMode.
           PIDFCoefficients pidfOrig = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // Change coefficients using methods included with DcMotorEx class.
           PIDFCoefficients pidfNew = new PIDFCoefficients(NEW_P, NEW_I, NEW_D, NEW_F);
           motorExLeft.setPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER, pidfNew);

           // Re-read coefficients and verify change.
           PIDFCoefficients pidfModified = motorExLeft.getPIDFCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // display info to user
           while(opModeIsActive()) {
               telemetry.addData("Runtime (sec)", "%.01f", getRuntime());
               telemetry.addData("P,I,D,F (orig)", "%.04f, %.04f, %.04f, %.04f",
                       pidfOrig.p, pidfOrig.i, pidfOrig.d, pidfOrig.f);
               telemetry.addData("P,I,D,F (modified)", "%.04f, %.04f, %.04f, %.04f",
                       pidfModified.p, pidfModified.i, pidfModified.d, pidfModified.f);
               telemetry.update();
           }
       }
   }

Note that the actual change of the PIDF coefficients occurs **on the
motor controller** that is controlling the selected motor. An alternate
way to adjust the PIDF coefficients is to use the extended/enhanced
**PIDF-related methods of the DcMotorControllerEx class**, as follows:

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorControllerEx;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDFCoefficients;

   /**
    * Created by Tom on 9/26/17.  Updated 9/24/2021 for PIDF.
    * This assumes that you are using a REV Robotics Expansion Hub
    * as your DC motor controller.  This OpMode uses the extended/enhanced
    * PIDF-related functions of the DcMotorControllerEx class.
    * The REV Robotics Expansion Hub supports the extended motor controller
    * functions, but other controllers (such as the deprecated Modern Robotics
    * and Hitechnic DC Motor Controllers) do not.
    */

   @Autonomous(name="Concept: Change PIDF Controller", group = "Concept")
   public class ConceptChangePIDFController extends LinearOpMode {

       // our DC motor
       DcMotor motorLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;
       public static final double NEW_F = 0.5;
       // These values are for illustration only; they must be set
       // and adjusted for each motor based on its planned usage.

       public void runOpMode() {
           // get reference to DC motor.
           motorLeft = hardwareMap.get(DcMotor.class, "left_drive");

           // wait for start command.
           waitForStart();

           // Get a reference to the motor controller and cast it as an extended functionality controller.
           // We assume it's a REV Robotics Expansion Hub, which supports the extended controller functions.
           DcMotorControllerEx motorControllerEx = (DcMotorControllerEx)motorLeft.getController();

           // Get the port number of our configured motor.
           int motorIndex = ((DcMotorEx)motorLeft).getPortNumber();

           // Get the PIDF coefficients for the RUN_USING_ENCODER RunMode.
           PIDFCoefficients pidfOrig = motorControllerEx.getPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

           // change coefficients
           PIDFCoefficients pidfNew = new PIDFCoefficients(NEW_P, NEW_I, NEW_D, NEW_F);
           motorControllerEx.setPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER, pidfNew);

           // Re-read coefficients and verify change.
           PIDFCoefficients pidfModified = motorControllerEx.getPIDFCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

           // Display info to user.
           while(opModeIsActive()) {
               telemetry.addData("Runtime (sec)", "%.01f", getRuntime());
               telemetry.addData("P,I,D,F (orig)", "%.04f, %.04f, %.04f, %.04f",
                       pidfOrig.p, pidfOrig.i, pidfOrig.d, pidfOrig.f);
               telemetry.addData("P,I,D,F (modified)", "%.04f, %.04f, %.04f, %.04f",
                       pidfModified.p, pidfModified.i, pidfModified.d, pidfModified.f);
               telemetry.update();
           }
       }
   }

Note 1: As of SDK 7.0, the former PID-only methods are still
available, but deprecated.

Note 2: the deprecated Modern Robotics and Hitechnic DC motor
controllers do not support adjustable PID or PIDF coefficients.
