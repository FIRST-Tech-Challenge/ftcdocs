/*
This example is used in a tutorial on FTC myBlocks.
It shows how a non-myBlock shared 'utility' method can be called by myBlock methods.
This also has examples of Java constants and type casting.

In this example, the Java programmer has two goals:
1. Support two robots with different wheels and motors.
2. Keep the myBlocks very simple for the users.

Solution: one MyBlock per robot, specify only the distance to drive.
Each myBlock uses the appropriate wheel size and motor encoder CPR.
The myBlocks share a 'utility' method to convert distance to encoder counts.

*/

package org.firstinspires.ftc.teamcode;

// OBJ and Android Studio automatically create these import statements.
import org.firstinspires.ftc.robotcore.external.ExportToBlocks;
import org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion;

// BlocksOpModeCompanion provides many useful FTC objects to this class.
public class SampleMyBlocks_v04 extends BlocksOpModeCompanion {

    // This annotation must directly precede a myBlock method
    @ExportToBlocks (
        comment = "FOR ROBOT A ONLY. Enter inches to drive.",
        tooltip = "Robot A convert inches to encoder counts",
        parameterLabels = "Drive Distance (inches)"
        )
    // This is a myBlock method with one input and one output.
    // The keyword 'final' indicates a Java constant: a variable that cannot change value.
    // Java constants are traditionally ALL CAPS.
    public static int inchesToCountsRobotA (double inchesToDriveA) {
        final double WHEEL_DIAMETER_A = 4.0;        // inches
        final double COUNTS_PER_ROTATION_A = 1120;  // CPR for NeveRest 40
        // call the shared utility method
        int countsToDriveA = calculateCounts (inchesToDriveA, COUNTS_PER_ROTATION_A, WHEEL_DIAMETER_A);
        return countsToDriveA;                      // give the result to Blocks
    }   // end of method
    
    // This annotation must directly precede a myBlock method
    @ExportToBlocks (
        comment = "FOR ROBOT B ONLY. Enter inches to drive.",
        tooltip = "Robot B convert inches to encoder counts",
        parameterLabels = "Drive Distance (inches)"
        )
    // This is another myBlock method, also with one input and one output.
    // Both myBlocks will appear in the Blocks menu for this Java Class.
    public static int inchesToCountsRobotB (double inchesToDriveB) {
        final double WHEEL_DIAMETER_B = 3.0;        // inches
        final double COUNTS_PER_ROTATION_B = 537.6; // CPR for NeveRest Orbital 20
        // call the shared utility method
        int countsToDriveB = calculateCounts (inchesToDriveB, COUNTS_PER_ROTATION_B, WHEEL_DIAMETER_B);
        return countsToDriveB;                      // give the result to Blocks
    }   // end of method

    // This is NOT a myBlock, it's a shared 'utility' method that is called by other methods.
    // It has 3 inputs (decimal numbers) and one output (integer).
    // The keyword 'private' means this method can be called only within this class.
    private static int calculateCounts (double inchesToDrive, double countsPerWheelRotation, double wheelDiameter) {
        double circumference = wheelDiameter * Math.PI;
        double rotations = inchesToDrive / circumference;
        double encoderCounts = rotations * countsPerWheelRotation;
        return (int) encoderCounts;         // (int) casts or converts the decimal number to integer type
    }   // end of method
    
}       // end of class SampleMyBlocks_v04
