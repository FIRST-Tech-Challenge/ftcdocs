/*
This is a sample Java program for an FTC myBlocks tutorial.  This class
contains methods that define myBlocks for FTC Blocks programming.

Demonstrates using 5 of the 6 objects inherited from BlocksOpModeCompanion:
linearOpMode, hardwareMap, telemetry, gamepad1, gamepad2.

Each of these 5 objects allows direct/convenient use of its commands (methods).
*/

// a myBlocks class must exist in the 'teamcode' folder/package
package org.firstinspires.ftc.teamcode;

// these are (usually!) automatically listed by OnBot Java when needed
import org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion;
import org.firstinspires.ftc.robotcore.external.ExportToBlocks;
import com.qualcomm.robotcore.hardware.Servo;

// BlocksOpModeCompanion provides 6 classes useful for myBlocks
public class SampleMyBlocks_v02 extends BlocksOpModeCompanion {

    // annotation required for method to be a myBlock; 3 features optional
    @ExportToBlocks (
    comment = "Move a conventional servo back and forth. Assumes servo starts" +
              " from position 0. Servo name must be in the active configuration.",
    tooltip = "Wiggle a user-designated servo.",
    parameterLabels = {"Servo name", "Duration (milliseconds)", "Number of cycles"}
    )
    // this is a myBlock method with 3 inputs and no outputs (void)
    public static void wiggleServo (String servoName, int duration, int cycles) {

        /*
        1. Declare new object called myServo, of type (class) Servo.
        2. Get properties of named servo from hardwareMap (configuration).
        3. Assign those properties to new object myServo.
        */
        Servo myServo = hardwareMap.get(Servo.class, servoName);

        // Display confirming messages and instructions for user.
        telemetry.addData("Servo name", servoName);
        telemetry.addData("Servo cycle duration", duration);
        telemetry.addData("Servo cycles to run", cycles);
        telemetry.addData(": : : : PRESS BUTTON X TO BEGIN : : :", null);
        telemetry.update();

        while ( !gamepad1.x && !gamepad2.x             // X buttons not pressed
                && linearOpMode.opModeIsActive() )   {
                  // empty while loop, waiting for operator input
                }   
    
        // Wiggle the servo using specified duration and cycles,
        // and while the opMode was not stopped.
        for (int i = 0; i < cycles && linearOpMode.opModeIsActive(); i++)  {

            telemetry.addData("Servo current cycle", i+1);
            telemetry.update();             // display progress to user

            myServo.setPosition(0.5);       // move servo clockwise
            linearOpMode.sleep(duration);   // hold for duration
            myServo.setPosition(0);         // move servo counterclockwise
            linearOpMode.sleep(duration);   // hold for duration
        }

        // Display final info for user.
        telemetry.addData("Servo name", servoName);
        telemetry.addData("Servo cycle duration", duration);
        telemetry.addData("Servo cycles completed", cycles);
        telemetry.update();

    }   // end method wiggleServo()

}       // end class SampleMyBlocks_v02
