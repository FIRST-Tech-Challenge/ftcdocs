/*
v01 dated 12/20/2020

This FTC myBlocks example allows the Blocks user to modify the Telemetry
refresh rate from the standard 4 cycles per second (4 Hz or 250 ms interval).
A lower time interval can allow faster update of sensor or encoder data.
A higher interval can ease the RC-DS communication bandwidth load.

This feature is not available with regular Blocks, in FTC app version 6.1.

For more controls, click Telemetry in the left side column here:
https://first-tech-challenge.github.io/FtcRobotController/6.0.1/RobotCore/index.html

The top-level API Documentation for the FTC SDK is here:
https://first-tech-challenge.github.io/FtcRobotController/
*/

package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion;
import org.firstinspires.ftc.robotcore.external.ExportToBlocks;
// Don't need to import Telemetry class, provided with BlocksOpModeCompanion.

public class W_myBlocks extends BlocksOpModeCompanion {

    // This Annotation must appear immediately before any myBlock method.
    // Optional to add a comment, tooltip, and/or parameterLabels.
    // Comment must be a single text line, concatenation (+) allowed.
    @ExportToBlocks (
    comment = "Sets Telemetry refresh rate, which resets to default 250 ms " +
    "every time OpMode runs.  Optional: add pause in Blocks to view " +
    "confirming message.",
    tooltip = "Set Telemetry refresh rate",
    parameterLabels = {"Refresh rate (milliseconds)"}
    )
    // This method has 1 input and no outputs (keyword void).
    public static void setTelemetryRate (int myRate) {

        // Get and store the existing (default) minimum interval between
        // Telemetry transmissions from Robot Controller to Driver Station.
        int oldRate = telemetry.getMsTransmissionInterval();

        // Set the minimum interval, provided by the Blocks user.
        telemetry.setMsTransmissionInterval(myRate);

        // For confirmation, get and store the updated interval.
        int newRate = telemetry.getMsTransmissionInterval();

        telemetry.addData("TELEMETRY REFRESH RATE in milliseconds", null);
        telemetry.addData("Default/previous rate", oldRate);
        telemetry.addData("Requested rate", myRate);
        telemetry.addData("Confirmed new rate", newRate);
        telemetry.update();         // display info on Driver Station screen

    }   // end of method setTelemetryRate()

}   // end of class W_myBlocks

