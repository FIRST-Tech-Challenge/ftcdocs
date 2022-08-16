package org.firstinspires.ftc.teamcode;

import org.firstinspires.ftc.robotcore.external.BlocksOpModeCompanion;
import org.firstinspires.ftc.robotcore.external.ExportToBlocks;


public class SampleMyBlocks_v00 extends BlocksOpModeCompanion {

@ExportToBlocks (
    comment = "Here is a greeting for you.",
    tooltip = "Greet a person or group.",
    parameterLabels = {"Recipient"}
)
public static String myGreeting (String greetingRecipient)  {
    return ("Hello " + greetingRecipient + "!");
}

}
