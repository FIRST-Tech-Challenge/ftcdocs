Changing PID Coefficients
==========================

The REV Robotics Expansion Hub allows a user to change the PID
coefficients used for closed loop motor control. The PID coefficients
are channel and mode specific. Note that the Modern Robotics and
Hitechnic DC motor controllers do not support adjustable PID
coefficients.

The following op mode uses an extended or enhanced DcMotor class (called
“DcMotorEx”) to change the PID coefficients for the RUN_USING_ENCODER
mode for a motor named “left_drive”. The op mode uses the
setPIDCoefficients method of the DcMotorEx class to change the values.
This method is not available with the standard DcMotor class.

Note that changes made to the PID coefficients do not persist if you
power cycle the REV Robotics Expansion Hub. If you need your changes to
the PID to persist, you should consider modifying your op mode to store
state information on the Android phone. The Android Developer website
has a tutorial on how to save data from your app onto an Android device
`here <https://developer.android.com/training/data-storage>`__

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDCoefficients;

   /**
    * Created by tom on 9/26/17.
    * This assumes that you are using a REV Robotics Expansion Hub
    * as your DC motor controller.  This op mode uses the extended/enhanced
    * PID-related functions of the DcMotorEx class.  The REV Robotics Expansion Hub
    * supports the extended motor functions, but other controllers (such as the 
    * Modern Robotics and Hitechnic DC Motor Controllers) do not.
    */

   @Autonomous(name="Concept: Change PID", group = "Concept")
   public class ConceptChangePID extends LinearOpMode {

       // our DC motor.
       DcMotorEx motorExLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;

       public void runOpMode() {
           // get reference to DC motor.
           // since we are using the Expansion Hub,
           // cast this motor to a DcMotorEx object.
           motorExLeft = (DcMotorEx)hardwareMap.get(DcMotor.class, "left_drive");

           // wait for start command.
           waitForStart();

           // get the PID coefficients for the RUN_USING_ENCODER  modes.
           PIDCoefficients pidOrig = motorExLeft.getPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // change coefficients using methods included with DcMotorEx class.
           PIDCoefficients pidNew = new PIDCoefficients(NEW_P, NEW_I, NEW_D);
           motorExLeft.setPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER, pidNew);

           // re-read coefficients and verify change.
           PIDCoefficients pidModified = motorExLeft.getPIDCoefficients(DcMotor.RunMode.RUN_USING_ENCODER);

           // display info to user.
           while(opModeIsActive()) {
               telemetry.addData("Runtime", "%.03f", getRuntime());
               telemetry.addData("P,I,D (orig)", "%.04f, %.04f, %.0f",
                       pidOrig.p, pidOrig.i, pidOrig.d);
               telemetry.addData("P,I,D (modified)", "%.04f, %.04f, %.04f",
                       pidModified.p, pidModified.i, pidModified.d);
               telemetry.update();
           }
       }
   }

Note that the actual change of the PID coefficients occurs on the motor
controller that is controlling the selected motor. An alternate way to
adjust the PID coefficients is to use the extended/enhanced PID-related
methods of the DcMotorControllerEx class:

.. code-block:: java

   package org.firstinspires.ftc.teamcode;

   import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
   import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
   import com.qualcomm.robotcore.hardware.DcMotor;
   import com.qualcomm.robotcore.hardware.DcMotorControllerEx;
   import com.qualcomm.robotcore.hardware.DcMotorEx;
   import com.qualcomm.robotcore.hardware.PIDCoefficients;

   /**
    * Created by tom on 9/26/17.
    * This assumes that you are using a REV Robotics Expansion Hub
    * as your DC motor controller. This op mode uses the extended/enhanced
    * PID-related functions of the DcMotorControllerEx class.  
    * The REV Robotics Expansion Hub supports the extended motor controller
    * functions, but other controllers (such as the Modern Robotics and 
    * Hitechnic DC Motor Controllers) do not.
    */

   @Autonomous(name="Concept: Change PID Controller", group = "Examples")
   public class ConceptChangePIDController extends LinearOpMode {

       // our DC motor.
       DcMotor motorLeft;

       public static final double NEW_P = 2.5;
       public static final double NEW_I = 0.1;
       public static final double NEW_D = 0.2;

       public void runOpMode() {
           // get reference to DC motor.
           motorLeft = hardwareMap.get(DcMotor.class, "left_drive");

           // wait for start command.
           waitForStart();

           // get a reference to the motor controller and cast it as an extended functionality controller.
           // we assume it's a REV Robotics Expansion Hub (which supports the extended controller functions).
           DcMotorControllerEx motorControllerEx = (DcMotorControllerEx)motorLeft.getController();

           // get the port number of our configured motor.
           int motorIndex = ((DcMotorEx)motorLeft).getPortNumber();

           // get the PID coefficients for the RUN_USING_ENCODER  modes.
           PIDCoefficients pidOrig = motorControllerEx.getPIDCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

           // change coefficients.
           PIDCoefficients pidNew = new PIDCoefficients(NEW_P, NEW_I, NEW_D);
           motorControllerEx.setPIDCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER, pidNew);

           // re-read coefficients and verify change.
           PIDCoefficients pidModified = motorControllerEx.getPIDCoefficients(motorIndex, DcMotor.RunMode.RUN_USING_ENCODER);

           // display info to user.
           while(opModeIsActive()) {
               telemetry.addData("Runtime", "%.03f", getRuntime());
               telemetry.addData("P,I,D (orig)", "%.04f, %.04f, %.0f",
                       pidOrig.p, pidOrig.i, pidOrig.d);
               telemetry.addData("P,I,D (modified)", "%.04f, %.04f, %.04f",
                       pidModified.p, pidModified.i, pidModified.d);
               telemetry.update();
           }
       }
   }
