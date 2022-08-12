/*
 * This example OpMode shows how existing webcam controls can affect 
 * TensorFlow Object Detection (TFOD) of FTC Freight Frenzy game elements.
 * It's a companion to the FTC wiki tutorial on Webcam Controls.
 * 
 * Put the Driver Station in Landscape Mode for this telemetry.
 *
 * The FTC SDK 7.0 includes up to 7 ways of controlling the preview image,
 * depending on webcam capability.  This OpMode uses 2 of those controls, 
 * Exposure and Gain, available on most webcams and offering good
 * potential for affecting TFOD recognition.
 * 
 * This OpMode simply adds ExposureControl and GainControl methods to the FTC
 * sample called "ConceptTensorFlowObjectDetectionWebcam.java".  Here, you can
 * use a gamepad to directly change the preview image and observe TFOD results.
 * 
 * Teams can use this to seek better recognition results from their existing
 * TFOD model -- whether the basic version in the 7.0 release, or their own
 * custom model created with the FTC Machine Learning toolchain.
 * 
 * Exposure, gain and other CameraControl values could be pre-programmed in
 * team autonomous OpModes.  It's also possible to manually enter such values
 * before a match begins, based on anticipated lighting, starting position and 
 * other game-time factors.
 * 
 * Add your own Vuforia key, where shown below.
 *
 * Questions, comments and corrections to westsiderobotics@verizon.net
 *
 * from v04 11/11/21 
 */
 
package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.ExposureControl;
import org.firstinspires.ftc.robotcore.external.hardware.camera.controls.GainControl;
import java.util.concurrent.TimeUnit;

import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import org.firstinspires.ftc.robotcore.external.navigation.VuforiaLocalizer;
import org.firstinspires.ftc.robotcore.external.tfod.TFObjectDetector;
import org.firstinspires.ftc.robotcore.external.tfod.Recognition;
import org.firstinspires.ftc.robotcore.external.hardware.camera.WebcamName;
import org.firstinspires.ftc.robotcore.external.ClassFactory;
import java.util.List;

@TeleOp(name = "W TFOD Webcam Exposure & Gain v04", group = "Webcam Controls")

public class W_TFOD_WebcamExpGain_v04 extends LinearOpMode {
  /* Note: This sample uses the all-objects Tensor Flow model (FreightFrenzy_BCDM.tflite), which contains
   * the following 4 detectable objects
   *  0: Ball,
   *  1: Cube,
   *  2: Duck,
   *  3: Marker (duck location tape marker)
   *
   *  Two additional model assets are available which only contain a subset of the objects:
   *  FreightFrenzy_BC.tflite  0: Ball,  1: Cube
   *  FreightFrenzy_DM.tflite  0: Duck,  1: Marker
   */
    private static final String TFOD_MODEL_ASSET = "FreightFrenzy_BCDM.tflite";
    private static final String[] LABELS = {
      "Ball",
      "Cube",
      "Duck",
      "Marker"
    };

    /*
     * IMPORTANT: You need to obtain your own license key to use Vuforia. The string below with which
     * 'parameters.vuforiaLicenseKey' is initialized is for illustration only, and will not function.
     * A Vuforia 'Development' license key, can be obtained free of charge from the Vuforia developer
     * web site at https://developer.vuforia.com/license-manager.
     *
     * Vuforia license keys are always 380 characters long, and look as if they contain mostly
     * random data. As an example, here is a example of a fragment of a valid key:
     *      ... yIgIzTqZ4mWjk9wd3cZO9T1axEqzuhxoGlfOOI2dRzKS4T0hQ8kT ...
     * Once you've obtained a license key, copy the string from the Vuforia web site
     * and paste it in to your code on the next line, between the double quotes.
     */
    private static final String VUFORIA_KEY =
            //"   INSERT YOUR VUFORIA KEY HERE  ";
            
    /**
     * {@link #vuforia} is the variable we will use to store our instance of the Vuforia
     * localization engine.
     */
    private VuforiaLocalizer vuforia;

    /**
     * {@link #tfod} is the variable we will use to store our instance of the TensorFlow Object
     * Detection engine.
     */
    private TFObjectDetector tfod;

    // *** ADD WEBCAM CONTROLS -- SECTION START ***
    ExposureControl myExposureControl;  // declare exposure control object
    long minExp;
    long maxExp;
    long curExp;            // exposure is duration, in time units specified

    GainControl myGainControl;      // declare gain control object
    int minGain;
    int maxGain;
    int curGain;
    boolean wasSetGainSuccessful;   // returned from setGain()
    
    boolean isAEPriorityOn = false;
    // *** ADD WEBCAM CONTROLS -- SECTION END ***

    @Override
    public void runOpMode() {
        // The TFObjectDetector uses the camera frames from the VuforiaLocalizer, so we create that
        // first.
        initVuforia();
        initTfod();

        /**
         * Activate TensorFlow Object Detection before we wait for the start command.
         * Do it here so that the Camera Stream window will have the TensorFlow annotations visible.
         **/
        if (tfod != null) {
            tfod.activate();

            // The TensorFlow software will scale the input images from the camera to a lower resolution.
            // This can result in lower detection accuracy at longer distances (> 55cm or 22").
            // If your target is at distance greater than 50 cm (20") you can adjust the magnification value
            // to artificially zoom in to the center of image.  For best results, the "aspectRatio" argument
            // should be set to the value of the images used to create the TensorFlow Object Detection model
            // (typically 16/9).
            tfod.setZoom(1.0, 16.0/9.0);    // modified for testing Exposure & Gain
            // tfod.setZoom(2.5, 16.0/9.0); // original settings in Concept OpMode
        }

        // *** ADD WEBCAM CONTROLS -- SECTION START ***

        // Assign the exposure and gain control objects, to use their methods.
        myExposureControl = vuforia.getCamera().getControl(ExposureControl.class);
        myGainControl = vuforia.getCamera().getControl(GainControl.class);

        // get webcam exposure limits
        minExp = myExposureControl.getMinExposure(TimeUnit.MILLISECONDS);
        maxExp = myExposureControl.getMaxExposure(TimeUnit.MILLISECONDS);

        // get webcam gain limits
        minGain = myGainControl.getMinGain();
        maxGain = myGainControl.getMaxGain();

        // Change mode to Manual, in order to control directly.
        // A non-default setting may persist in the camera, until changed again.
        myExposureControl.setMode(ExposureControl.Mode.Manual);

        // Retrieve from webcam its current exposure and gain values
        curExp = myExposureControl.getExposure(TimeUnit.MILLISECONDS);
        curGain = myGainControl.getGain();

        // display exposure mode and starting values to user
        telemetry.addLine("\nTouch Start arrow to control webcam Exposure and Gain");
        telemetry.addData("\nCurrent exposure mode", myExposureControl.getMode());
        telemetry.addData("Current exposure value", curExp);
        telemetry.addData("Current gain value", curGain);
        telemetry.update();
        // *** ADD WEBCAM CONTROLS -- SECTION END ***


        waitForStart();

        if (opModeIsActive()) {
            while (opModeIsActive()) {
                  
                // *** ADD WEBCAM CONTROLS -- SECTION START ***
                // Driver Station in Landscape Mode for this telemetry.
                telemetry.addLine("Exposure: left stick Y; Gain: right stick Y");
                telemetry.addData("Exposure", "Min:%d, Max:%d, Current:%d", minExp, maxExp, curExp);
                telemetry.addData("Gain", "Min:%d, Max:%d, Current:%d", minGain, maxGain, curGain);
                telemetry.addLine("\nAutoExposure Priority: green A ON; red B OFF");
                telemetry.addData("AE Priority on?", isAEPriorityOn);
                // *** ADD WEBCAM CONTROLS -- SECTION END ***
    
                if (tfod != null) {
                    // getUpdatedRecognitions() will return null if no new information is available since
                    // the last time that call was made.
                    List<Recognition> updatedRecognitions = tfod.getUpdatedRecognitions();
                    if (updatedRecognitions != null) {
                      telemetry.addData("\n# Object Detected", updatedRecognitions.size());
                      // step through the list of recognitions and display boundary info.
                      int i = 0;
                      for (Recognition recognition : updatedRecognitions) {
                        telemetry.addData(String.format("label (%d)", i), recognition.getLabel());
                        telemetry.addData(String.format("  left,top (%d)", i), "%.03f , %.03f",
                                recognition.getLeft(), recognition.getTop());
                        telemetry.addData(String.format("  right,bottom (%d)", i), "%.03f , %.03f",
                                recognition.getRight(), recognition.getBottom());
                        i++;
                      }  // end for() loop
                      
                    }   // end if (updatedRecognitions)
                
                }   // end if (tfod)
                
                telemetry.update();
                
                // *** ADD WEBCAM CONTROLS -- SECTION START ***
                
                // manually adjust the webcam exposure & gain variables
                float changeExp = -gamepad1.left_stick_y;
                float changeGain = -gamepad1.right_stick_y;

                int changeExpInt = (int) (changeExp*2);     // was *5
                int changeGainInt = (int) (changeGain*2);   // was *5

                curExp += changeExpInt;
                curGain += changeGainInt;

                if (gamepad1.a) {           // AE Priority ON with green A
                    myExposureControl.setAePriority(true);
                    isAEPriorityOn = true;
                } else if (gamepad1.b) {    // AE Priority OFF with red B
                    myExposureControl.setAePriority(false);
                    isAEPriorityOn = false;
                }

                // ensure inputs are within webcam limits, if provided
                curExp = Math.max(curExp, minExp);
                curExp = Math.min(curExp, maxExp);
                curGain = Math.max(curGain, minGain);
                curGain = Math.min(curGain, maxGain);

                // update the webcam's settings
                myExposureControl.setExposure(curExp, TimeUnit.MILLISECONDS);
                wasSetGainSuccessful = myGainControl.setGain(curGain);

                sleep(50);             // slow down the main while() loop

                // *** ADD WEBCAM CONTROLS -- SECTION END ***

            }   // end main while() loop

        } // end if opModeIsActive()

    }  // end runOpMode()


    /**
     * Initialize the Vuforia localization engine.
     */
    private void initVuforia() {
        /*
         * Configure Vuforia by creating a Parameter object, and passing it to the Vuforia engine.
         */
        VuforiaLocalizer.Parameters parameters = new VuforiaLocalizer.Parameters();

        parameters.vuforiaLicenseKey = VUFORIA_KEY;
        parameters.cameraName = hardwareMap.get(WebcamName.class, "Webcam 1");

        //  Instantiate the Vuforia engine
        vuforia = ClassFactory.getInstance().createVuforia(parameters);

        // Loading trackables is not necessary for the TensorFlow Object Detection engine.

    }   // end method initVuforia()

    /**
     * Initialize the TensorFlow Object Detection engine.
     */
    private void initTfod() {
        int tfodMonitorViewId = hardwareMap.appContext.getResources().getIdentifier(
            "tfodMonitorViewId", "id", hardwareMap.appContext.getPackageName());
        TFObjectDetector.Parameters tfodParameters = new TFObjectDetector.Parameters(tfodMonitorViewId);
       tfodParameters.minResultConfidence = 0.8f;
       tfodParameters.isModelTensorFlow2 = true;
       tfodParameters.inputSize = 320;
       tfod = ClassFactory.getInstance().createTFObjectDetector(tfodParameters, vuforia);
       tfod.loadModelFromAsset(TFOD_MODEL_ASSET, LABELS);
    }  // end method initTfod()

}  //end class

