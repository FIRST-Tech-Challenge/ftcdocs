/* 

This example OpMode allows direct gamepad control of white balance temperature,
if supported.  It's a companion to the FTC wiki tutorial on Webcam Controls.

Put the Driver Station Layout in Landscape mode for this telemetry.

Add your own Vuforia key, where shown below.

Questions, comments and corrections to westsiderobotics@verizon.net

from v01 11/12/21
 */

package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.WhiteBalanceControl;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;

import org.firstinspires.ftc.robotcore.external.ClassFactory;
import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.robotcore.external.navigation.VuforiaLocalizer;

@TeleOp(name="Webcam Controls - White Balance v01", group ="Webcam Controls")

public class W_WebcamControls_WhiteBalance_v01 extends LinearOpMode {

    private static final String VUFORIA_KEY =
            //"   INSERT YOUR VUFORIA KEY HERE  ";
            
    // Class Members
    private VuforiaLocalizer vuforia    = null;
    private WebcamName webcamName       = null;

    WhiteBalanceControl myWBControl;  // declare White Balance Control object
    int minWhiteBalanceTemp;          // temperature in degrees Kelvin (K)
    int maxWhiteBalanceTemp;
    int curWhiteBalanceTemp;

    int tempIncrement = 100;          // for manual gamepad adjustment
    boolean wasTemperatureSet;        // did the set() operation succeed?
    boolean wasWhiteBalanceModeSet;   // did the setMode() operation succeed?
    boolean useTempLimits = true;
    
    @Override public void runOpMode() {
        
        telemetry.setMsTransmissionInterval(50);
        
        // Connect to the webcam, using exact name per robot Configuration.
        webcamName = hardwareMap.get(WebcamName.class, "Webcam 1");

        /*
         * Configure Vuforia by creating a Parameter object, and passing it to the Vuforia engine.
         * We pass Vuforia the handle to a camera preview resource (on the RC screen).
         */
        
        int cameraMonitorViewId = hardwareMap.appContext.getResources().getIdentifier("cameraMonitorViewId", "id", hardwareMap.appContext.getPackageName());
        VuforiaLocalizer.Parameters parameters = new VuforiaLocalizer.Parameters(cameraMonitorViewId);

        parameters.vuforiaLicenseKey = VUFORIA_KEY;

        // We also indicate which camera we wish to use.
        parameters.cameraName = webcamName;

        //  Set up the Vuforia engine
        vuforia = ClassFactory.getInstance().createVuforia(parameters);

        // Assign the white balance control object, to use its methods.
        myWBControl = vuforia.getCamera().getControl(WhiteBalanceControl.class);

        // display current white balance mode
        telemetry.addLine("\nTouch Start arrow to control white balance temperature.");
        telemetry.addLine("\nRecommended: put Driver Station Layout in Landscape.");
        telemetry.addData("\nCurrent white balance mode", myWBControl.getMode());
        telemetry.update();


        waitForStart();

        // set variable to current actual temperature, if supported
        curWhiteBalanceTemp = myWBControl.getWhiteBalanceTemperature();
        
        // get webcam temperature limits, if provided
        minWhiteBalanceTemp = myWBControl.getMinWhiteBalanceTemperature();
        maxWhiteBalanceTemp = myWBControl.getMaxWhiteBalanceTemperature();
        
        // Set white balance mode to Manual, for direct control.
        // A non-default setting may persist in the camera, until changed again.
        wasWhiteBalanceModeSet = myWBControl.setMode(WhiteBalanceControl.Mode.MANUAL);

        while (opModeIsActive()) {

            // manually adjust the color temperature variable
            if (gamepad1.x) {                  // increase with blue X (cooler)
                curWhiteBalanceTemp += tempIncrement;
            }  else if (gamepad1.b) {          // decrease with red B (warmer)
                curWhiteBalanceTemp -= tempIncrement;
            }
    
            // ensure inputs are within webcam limits, if provided
            if (useTempLimits) {
                curWhiteBalanceTemp = Math.max(curWhiteBalanceTemp, minWhiteBalanceTemp);
                curWhiteBalanceTemp = Math.min(curWhiteBalanceTemp, maxWhiteBalanceTemp);
            } 

            // update the color temperature setting
            wasTemperatureSet = myWBControl.setWhiteBalanceTemperature(curWhiteBalanceTemp);
            
            // display live feedback while user observes preview image
            telemetry.addLine("Adjust temperature with blue X (cooler) & red B (warmer)");
            
            telemetry.addData("\nWhite Balance Temperature",
                "Min: %d, Max: %d, Actual: %d",
                minWhiteBalanceTemp, maxWhiteBalanceTemp,
                myWBControl.getWhiteBalanceTemperature());

            telemetry.addData("\nProgrammed temperature", "%d", curWhiteBalanceTemp);
            telemetry.addData("Temperature set OK?", wasTemperatureSet);

            telemetry.addData("\nCurrent white balance mode", myWBControl.getMode());
            telemetry.addData("White balance mode set OK?", wasWhiteBalanceModeSet);
            telemetry.update();

            sleep(100);

        }   // end main while() loop

    }    // end OpMode

}   // end class
