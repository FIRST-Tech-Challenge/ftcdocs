.. meta::
   :title: FIRST Tech Challenge Glossary
   :description: Definitions of the hardware, software, programming and competition terms used throughout FIRST Tech Challenge documentation.
   :keywords: FTC Docs, FIRST Tech Challenge, FTC, Glossary, Terminology, Definitions

.. _glossary:

Glossary
========

This page collects the terms used throughout *FIRST* Tech Challenge documentation.
Terms are listed alphabetically. Throughout the rest of this site, the first
mention of a term in a page usually links back here, so you can check a
definition without losing your place.

.. note::

   Game-specific vocabulary (scoring elements, field features, award names and
   the like) changes every season and is defined in the
   :doc:`Competition Manual </manuals/game_manuals/game_manuals>` rather than
   here. Where a rule and this glossary disagree, the Competition Manual wins.

.. glossary::
   :sorted:

   ADB
   Android Debug Bridge
      A command-line tool, included with the Android platform tools, that lets a
      computer communicate with an Android device. Teams most often meet it
      indirectly: :term:`Android Studio` uses it to install the
      :term:`Robot Controller App` onto a :term:`Control Hub` or phone, either
      over USB or over the wireless network.

   Alliance
      The pair of teams that play a :term:`Match` together, either as the red
      Alliance or the blue Alliance. Alliance partners share a score.

   Analog Input
      A :term:`Hub` port that measures a continuous voltage rather than a simple
      on/off state. Used by sensors such as a :term:`Potentiometer` that report
      their reading as a voltage level.

   Android Studio
      Google's integrated development environment (:term:`IDE`) for Android
      apps. It is the most powerful of the three *FIRST* Tech Challenge
      programming tools: teams work from the ``FtcRobotController``
      :term:`Android Studio Project` on a laptop and build a customized
      :term:`Robot Controller App`, which gives access to version control,
      :term:`External Libraries` and a full debugger.
      See :doc:`/programming_resources/android_studio_java/Android-Studio-Tutorial`.

   Android Studio Project
      The ``FtcRobotController`` project published with each :term:`SDK`
      release. It contains the source of the :term:`Robot Controller App` plus a
      ``TeamCode`` module that teams add their own :term:`OpMode` classes to.

   AprilTag
      A fiducial marker — a square, high-contrast pattern, similar in spirit to a
      QR code but far simpler — developed at the University of Michigan. Because
      the physical size of a tag is known, detecting one in a camera image yields
      both its identity and its position and orientation relative to the camera.
      *FIRST* Tech Challenge places AprilTags on the :term:`Playing Field` so
      robots can locate themselves. See
      :doc:`/apriltag/vision_portal/apriltag_intro/apriltag-intro`.

   AUTO
   Autonomous
      The first phase of a :term:`Match`, during which the robot runs a
      pre-written :term:`OpMode` with no human input. Contrast with
      :term:`TELEOP`.

   Battery
      The 12V rechargeable battery that powers the :term:`Control Hub`,
      :term:`Expansion Hub`, motors, servos and sensors. The *FIRST* Tech
      Challenge battery has a 20A :term:`Fuse` built into its lead.
      See :doc:`/control_hard_compon/rc_components/power_distr/power-distr`.

   Blocks
   Blocks Programming Tool
      The visual, drag-and-drop programming tool built into the
      :term:`Robot Controller App`. Teams connect coloured blocks in a web
      browser to build an :term:`OpMode`, with no typing of Java required. It is
      the recommended starting point for new teams.
      See :doc:`/programming_resources/blocks/Blocks-Tutorial`.

   CAD
   Computer Aided Design
      Software used to design parts and assemblies in three dimensions before
      they are built. CAD models feed :term:`3D Printing`, :term:`CNC` machining
      and laser cutting, and let a team check that a mechanism fits before
      cutting metal. See :doc:`/cad_resources/index`.

   CNC
   Computer Numerical Control
      Machining in which a computer drives the cutting tool from a digital
      model, rather than a human turning handwheels. Mills, routers and lathes
      are all available in CNC form.
      See :doc:`/manufacturing/index`.

   Competition Manual
      The official rule book for the season, published by *FIRST*. It defines
      the game, the :term:`Playing Field`, robot construction rules,
      :term:`Inspection` requirements and tournament procedure, and it supersedes
      anything written on this site.
      See :doc:`/manuals/game_manuals/game_manuals`.

   Configuration File
   Robot Configuration
      A file stored on the :term:`Robot Controller` that lists every motor,
      servo and sensor attached to the robot, which port each one is plugged
      into, and the name a program should use to refer to it. An :term:`OpMode`
      looks up devices from this file through :term:`hardwareMap`, so a name
      typed in code must match the configuration exactly.
      See :doc:`/hardware_and_software_configuration/configuring/index`.

   Continuous Rotation Servo
      A :term:`Servo` modified to spin continuously in either direction instead
      of holding a commanded angle. Its power setting controls speed and
      direction, much like a small :term:`DC Motor`, but it has no position
      feedback.

   Control Hub
      The REV Robotics Control Hub: an Android-based device that combines a
      :term:`Robot Controller` and a :term:`Hub` in one package. It runs the
      :term:`Robot Controller App`, provides the motor, servo and sensor ports,
      and creates the wireless network the :term:`Driver Station` connects to.
      See :doc:`/control_hard_compon/rc_components/index`.

   Control System
      The collective name for the electronics and software that make a robot
      run: the :term:`Driver Station`, the :term:`Robot Controller`, the
      :term:`Hub` hardware, and the :term:`SDK` software on both ends.
      See :doc:`/programming_resources/shared/control_system_intro/The-FTC-Control-System`.

   DC Motor
      A motor that turns continuously when voltage is applied to it, used for
      drivetrains, lifts and intakes. Competition motors are supplied as a motor
      plus a gearbox and usually an :term:`Encoder`, and connect to a
      :term:`Hub` motor port.
      See :doc:`/control_hard_compon/rc_components/motors/motors`.

   Dead Wheel
      An unpowered wheel, fitted with an :term:`Encoder`, that rolls along the
      floor purely to measure how far the robot has travelled. Because it is not
      driven, it does not slip under load the way a drive wheel does, which makes
      it a more trustworthy source for :term:`Odometry`.

   Digital I/O
      A :term:`Hub` port that reads or writes a simple on/off signal. Used by
      devices such as a :term:`Touch Sensor` or an indicator LED.

   Driver Hub
      The REV Robotics Driver Hub: a purpose-built Android device with a screen
      and USB ports that runs the :term:`Driver Station App`. It is the most
      common :term:`Driver Station` hardware.
      See :doc:`/control_hard_compon/ds_components/index`.

   Driver Station
   DS
      The Android device that sits with the drivers and acts as the robot's
      remote control. It runs the :term:`Driver Station App`, has one or two
      :term:`Gamepad` controllers attached, and communicates with the
      :term:`Robot Controller` over a wireless link. Usually a
      :term:`Driver Hub`.

   Driver Station App
      The *FIRST* Tech Challenge app that runs on the :term:`Driver Station`.
      It selects and starts :term:`OpMode` programs, displays
      :term:`Telemetry`, forwards :term:`Gamepad` input to the robot, and hosts
      :term:`Self-Inspect` and the :term:`Configuration File` editor.

   EasyOpenCV
      A community-maintained library that made it straightforward to run
      :term:`OpenCV` vision pipelines on a camera stream in older versions of
      the :term:`SDK`. Newer code should generally use :term:`VisionPortal`
      instead, which provides equivalent camera handling in the SDK itself.

   Encoder
      A sensor built into or attached to a motor that counts shaft rotation,
      reporting position in "ticks" and allowing speed to be measured. Encoders
      are what make it possible to drive a known distance or hold an arm at a
      known angle. See
      :doc:`/control_hard_compon/rc_components/encoders/encoders`.

   End Game
      The final portion of :term:`TELEOP` in which additional scoring
      opportunities open up. What counts as End Game scoring is defined each
      season in the :term:`Competition Manual`.

   ESD
   Electrostatic Discharge
      The sudden flow of static electricity between two objects at different
      potentials — the spark you feel after walking across a carpet. On a robot
      it can reset or damage the :term:`Control Hub` and is a common cause of
      unexplained disconnections.
      See :doc:`/hardware_and_software_configuration/configuring/managing_esd/managing-esd`.

   Expansion Hub
      The REV Robotics Expansion Hub: a :term:`Hub` that adds a second set of
      motor, servo and sensor ports to a robot. It has no Android device inside,
      so it must be paired with a :term:`Control Hub` or a phone acting as the
      :term:`Robot Controller`.

   External Libraries
      Third-party code added to a team's project to provide functionality the
      :term:`SDK` does not. Libraries can be added as ``.aar``/``.jar`` files in
      :term:`OnBot Java`, or as Gradle dependencies in
      :term:`Android Studio`.

   Field Coordinate System
      The convention *FIRST* Tech Challenge uses to describe positions and
      headings on the :term:`Playing Field`, so that a robot's location can be
      expressed as X, Y and heading values that everyone interprets the same way.
      See :doc:`/game_specific_resources/field_coordinate_system/field-coordinate-system`.

   FIRST
      *For Inspiration and Recognition of Science and Technology*: the
      non-profit organization that runs *FIRST* Tech Challenge along with its
      other robotics programs.
      See :doc:`/overview/ftcoverview`.

   Firmware
      The low-level software running on a :term:`Hub`'s own microcontroller, as
      distinct from the Android operating system or the
      :term:`Robot Controller App`. Hub firmware occasionally needs updating to
      stay compatible with a new :term:`SDK`.
      See :doc:`/ftc_sdk/updating/hub_firmware/Updating-Hub-Firmware`.

   FTC Docs
      This documentation site, at
      `ftc-docs.firstinspires.org <https://ftc-docs.firstinspires.org/>`__. It
      is written and maintained by the *FIRST* Tech Challenge community; see
      :doc:`/contrib/index` if you would like to contribute.

   Fuse
      A deliberately weak link in a circuit that melts and breaks the connection
      if too much current flows, protecting everything downstream. The *FIRST*
      Tech Challenge :term:`Battery` carries a 20A automotive-style fuse in its
      lead.

   Gamepad
      A game controller, connected to the :term:`Driver Station` by USB, that a
      driver uses to command the robot during :term:`TELEOP`. An :term:`OpMode`
      reads its buttons and joysticks through the ``gamepad1`` and ``gamepad2``
      objects.

   Gear Ratio
      The ratio between the rotation of an input shaft and an output shaft in a
      gearbox or belt drive. Gearing down trades speed for torque; gearing up
      does the reverse. A motor's stated gear ratio must be accounted for when
      converting :term:`Encoder` ticks into real-world distance.

   Gracious Professionalism
      A core *FIRST* value: competing hard, while treating opponents,
      volunteers and teammates with respect, and helping others succeed even at
      a cost to yourself.
      See :doc:`/gracious_professionalism/gp`.

   hardwareMap
      The object available inside every :term:`OpMode` that looks up a physical
      device by the name given to it in the :term:`Configuration File`, for
      example ``hardwareMap.get(DcMotor.class, "left_drive")``. It is the bridge
      between a program and the robot's wiring.

   Heading
      The direction the robot is facing, measured as an angle within the
      :term:`Field Coordinate System`. Usually obtained from the :term:`IMU` or
      from :term:`Odometry`.

   Hub
      Shorthand for a :term:`Control Hub` or an :term:`Expansion Hub` — the
      electronic input/output module that lets the
      :term:`Robot Controller` talk to motors, servos and sensors.
      See :doc:`/control_hard_compon/rc_components/hub/hub`.

   I2C
      A two-wire communication bus used by many sensors, including the
      :term:`IMU` and most colour and distance sensors. Several devices can share
      one bus, but each needs a distinct address, so identical sensors normally
      go on separate :term:`Hub` I2C buses.

   IDE
   Integrated Development Environment
      An application that combines a code editor, a compiler and a debugger in
      one place. :term:`Android Studio` is the IDE used for *FIRST* Tech
      Challenge Java development.

   IMU
   Inertial Measurement Unit
      A sensor that measures rotation and acceleration, and so can report the
      robot's :term:`Heading`. An IMU is built into every :term:`Control Hub`
      and :term:`Expansion Hub`, and external IMUs are also available.
      See :doc:`/programming_resources/imu/imu`.

   Inspection
      The pre-competition check that a robot and its software meet the rules in
      the :term:`Competition Manual`. :term:`Self-Inspect` in the
      :term:`Driver Station App` covers the software half in advance.
      See :doc:`/hardware_and_software_configuration/self_inspect/self-inspect`.

   Iterative OpMode
      An :term:`OpMode` written by overriding the ``init``, ``loop`` and ``stop``
      methods of the ``OpMode`` class. The :term:`SDK` calls ``loop`` repeatedly
      for you. Contrast with :term:`LinearOpMode`.

   Javadoc
      Reference documentation generated from comments in the :term:`SDK` source
      code, describing every class and method available to an :term:`OpMode`.
      Published at `javadoc.io <https://javadoc.io/doc/org.firstinspires.ftc>`__.

   Judging
      The interview and evaluation process at a tournament through which teams
      are considered for awards, separate from :term:`Match` play.

   LinearOpMode
      An :term:`OpMode` written as a single ``runOpMode`` method that executes
      top to bottom, pausing at ``waitForStart()``. This style suits
      :term:`AUTO` programs, where steps happen in sequence. Contrast with
      :term:`Iterative OpMode`.

   Match
      One playing of the game between two :term:`Alliance` pairs, consisting of
      an :term:`AUTO` phase followed by a :term:`TELEOP` phase.

   Mecanum
   Mecanum Drive
      A drivetrain using wheels with rollers set at 45° around the rim. By
      driving the four wheels at different speeds the robot can move sideways
      and rotate without turning first — often called holonomic or
      omnidirectional movement.

   Odometry
      Estimating how far the robot has moved, and where it now is, by
      accumulating :term:`Encoder` readings over time. Accuracy depends on wheels
      not slipping, which is why :term:`Dead Wheel` pods are popular.

   OnBot Java
   OnBot Java Programming Tool
      A text-based Java editor built into the :term:`Robot Controller App` and
      used from a web browser. Code is compiled on the robot itself, so no
      laptop toolchain is needed — a middle step between :term:`Blocks` and
      :term:`Android Studio`.
      See :doc:`/programming_resources/onbot_java/OnBot-Java-Tutorial`.

   OpMode
   Op Mode
   Operational Mode
      A program that defines part of a robot's behaviour, written by the team and
      run on the :term:`Robot Controller`. OpModes are selected and started from
      the :term:`Driver Station`, and are declared as either :term:`AUTO` or
      :term:`TELEOP`. Each one is written as a :term:`LinearOpMode` or an
      :term:`Iterative OpMode`.
      See :doc:`/programming_resources/index`.

   OpenCV
      An open-source computer vision library, bundled with the :term:`SDK`, that
      provides the image-processing building blocks — colour conversion,
      thresholding, contour finding — used to detect objects in a camera frame.
      See :doc:`/color_processing/index`.

   OTG Adapter
      A small "USB On-The-Go" adapter that lets an Android phone act as a USB
      host, so that a :term:`Gamepad`, :term:`USB Hub` or
      :term:`Expansion Hub` can be plugged into it.

   PIDF
      A control algorithm — Proportional, Integral, Derivative, Feedforward —
      that adjusts motor power based on the difference between a target and the
      measured :term:`Encoder` value. The :term:`SDK` uses PIDF internally for
      motor velocity control, and its coefficients can be tuned.

   Playing Field
      The 12ft × 12ft tiled area, enclosed by field walls, on which a
      :term:`Match` is played. Its layout, including
      :term:`AprilTag` placement, changes each season.
      See :doc:`/game_specific_resources/playing_field_resources/playing_field_resources`.

   Potentiometer
      A sensor whose resistance varies with the position of a knob or shaft,
      read through an :term:`Analog Input`. Useful for measuring the angle of an
      arm across a limited range.

   PWM
   Pulse Width Modulation
      A technique for controlling how much power reaches a device by switching
      it on and off very rapidly and varying the fraction of time it spends on.
      :term:`Servo` position commands are sent as PWM signals.

   Referee
      The volunteer who enforces the rules of the :term:`Competition Manual`
      during a :term:`Match` and determines the final score.

   REV Hardware Client
      A Windows application from REV Robotics that updates the
      :term:`Firmware`, operating system and apps on a :term:`Control Hub`,
      :term:`Expansion Hub` or :term:`Driver Hub` over USB. It is the
      recommended way to keep hardware current.
      See :doc:`/ftc_sdk/updating/hardware_client/Updating-REV-Hardware-Client`.

   Robot Controller
   RC
      The Android device mounted on the robot that runs the team's
      :term:`OpMode` programs — the "brains" of the robot. Normally this is a
      :term:`Control Hub`; a supported Android phone paired with an
      :term:`Expansion Hub` also works.

   Robot Controller App
      The *FIRST* Tech Challenge app that runs on the
      :term:`Robot Controller`. It executes :term:`OpMode` programs, manages the
      :term:`Configuration File`, and serves the :term:`Blocks` and
      :term:`OnBot Java` programming tools to a web browser.

   Sample OpMode
      One of the ready-made example :term:`OpMode` programs shipped with the
      :term:`SDK`, found in the ``samples`` folder in
      :term:`Android Studio` or offered as a template in :term:`OnBot Java` and
      :term:`Blocks`. Samples are the fastest way to see a working example of a
      given sensor or technique.

   Scrimmage
      An informal practice competition, not part of the official tournament
      structure, where teams play :term:`Match` games to test robots and gain
      experience.

   SDK
   Software Development Kit
      The collection of *FIRST* Tech Challenge software tools: the
      :term:`Robot Controller App`, the :term:`Driver Station App`, the
      :term:`Android Studio Project`, the :term:`Javadoc` reference, and the
      season-specific assets. A new SDK is released each season.
      See :doc:`/ftc_sdk/overview/index`.

   Self-Inspect
      A screen in the :term:`Driver Station App` that checks the app versions,
      operating system versions and :term:`Firmware` on both the
      :term:`Driver Station` and the :term:`Robot Controller`, and reports
      whether they satisfy the requirements for competition.
      See :doc:`/hardware_and_software_configuration/self_inspect/new-self-inspect`.

   Sensor
      Any device that reports information about the robot or its surroundings —
      touch, distance, colour, rotation — to the :term:`Robot Controller`.
      Sensors attach to :term:`Digital I/O`, :term:`Analog Input` or
      :term:`I2C` ports on a :term:`Hub`.
      See :doc:`/control_hard_compon/rc_components/sensors/sensors`.

   Servo
      A motor that rotates to and holds a commanded position, typically over a
      limited range. Servos plug into dedicated :term:`Servo` ports on a
      :term:`Hub` and are commanded by position rather than power. See also
      :term:`Continuous Rotation Servo` and
      :doc:`/control_hard_compon/rc_components/servos/servos`.

   TELEOP
   Driver-Controlled Period
      The phase of a :term:`Match` after :term:`AUTO`, in which up to two human
      drivers control the robot using :term:`Gamepad` controllers connected to
      the :term:`Driver Station`.

   Telemetry
      Data sent from an :term:`OpMode` on the :term:`Robot Controller` to the
      :term:`Driver Station` screen, where it appears as lines of text.
      Telemetry is the primary way to see what a program is doing, and is
      therefore the primary debugging tool.

   TensorFlow
   TFOD
   TensorFlow Object Detection
      A machine-learning framework used to recognise objects in a camera image
      from a trained model. The :term:`SDK` ships a TFOD processor that can be
      run through :term:`VisionPortal`, along with season-specific models.

   Touch Sensor
      A simple switch that reports whether it is pressed, read through a
      :term:`Digital I/O` port. Commonly used as a limit switch to tell a
      mechanism it has reached the end of its travel.

   Tournament
      An official *FIRST* Tech Challenge event at which teams compete in
      :term:`Match` play and take part in :term:`Judging`.

   USB Hub
      A powered or unpowered splitter that provides extra USB ports. Needed when
      a :term:`Driver Station` phone must host two :term:`Gamepad` controllers
      at once, in which case it connects through an :term:`OTG Adapter`.

   VisionPortal
      The :term:`SDK` camera API. A VisionPortal opens a camera — a webcam or a
      phone's built-in camera — and feeds each frame to one or more vision
      processors, such as the :term:`AprilTag` or :term:`TFOD` processors, or a
      team's own :term:`OpenCV` pipeline.
      See :doc:`/apriltag/vision_portal/visionportal_overview/visionportal-overview`.

   Volunteer
      Anyone who gives their time to run a *FIRST* Tech Challenge event —
      :term:`Referee`, judge, inspector, queuer, scorekeeper and many more roles.
      Events cannot happen without them.

   Vuforia
      An image-target tracking library used in earlier seasons to locate the
      robot from printed picture targets on the field. It has been superseded by
      :term:`AprilTag` detection through :term:`VisionPortal`.

   Webcam
      A USB camera plugged into a :term:`Control Hub` or
      :term:`Robot Controller` phone and used for vision. Only cameras
      supporting the USB Video Class (UVC) standard work.
      See :doc:`/apriltag/vision_portal/visionportal_webcams/visionportal-webcams`.

   Wi-Fi Direct
      A peer-to-peer wireless standard that lets two devices connect without a
      router. It is how a :term:`Driver Station` phone pairs with a
      :term:`Robot Controller` phone. A :term:`Control Hub` instead creates its
      own wireless network for the Driver Station to join.

   3D Printing
      Building a part by depositing or curing material layer by layer from a
      :term:`CAD` model. The most common form in *FIRST* Tech Challenge is
      Fused Deposition Modeling (FDM), which extrudes melted plastic filament.
      See :doc:`/manufacturing/3d_printing/index`.
